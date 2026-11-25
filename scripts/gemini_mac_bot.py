#!/usr/bin/env python3
"""
Automated 16:9 Widescreen Infographic Generator using Google Gemini Pro Web UI
Drives the active Chrome session (sumanzfilms@gmail.com) via AppleScript + CoreGraphics.
"""

import ctypes
import glob
import json
import os
import subprocess
import sys
import time
from PIL import Image

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROMPTS_FILE = os.path.join(BASE_DIR, "scripts", "image_prompts.json")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")

WIN_X, WIN_Y, WIN_W, WIN_H = 22, 47, 1046, 768

cg = ctypes.CDLL("/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics")


class CGPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]


cg.CGEventCreateMouseEvent.restype = ctypes.c_void_p
cg.CGEventCreateMouseEvent.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint32,
    CGPoint,
    ctypes.c_uint32,
]
cg.CGEventPost.argtypes = [ctypes.c_uint32, ctypes.c_void_p]
cg.CGWarpMouseCursorPosition.argtypes = [CGPoint]


def click(x, y):
    pt = CGPoint(x, y)
    cg.CGWarpMouseCursorPosition(pt)
    time.sleep(0.1)
    cg.CGEventPost(0, cg.CGEventCreateMouseEvent(None, 5, pt, 0))
    time.sleep(0.1)
    cg.CGEventPost(0, cg.CGEventCreateMouseEvent(None, 1, pt, 0))
    time.sleep(0.06)
    cg.CGEventPost(0, cg.CGEventCreateMouseEvent(None, 2, pt, 0))


def osascript(script):
    return subprocess.check_output(["osascript", "-e", script]).decode("utf-8").strip()


def focus_and_reset_gemini():
    osascript(
        f"""
        tell application "Google Chrome"
          activate
          set w to first window whose URL of active tab contains "gemini.google.com"
          set index of w to 1
          set bounds of w to {{{WIN_X}, {WIN_Y}, {WIN_X + WIN_W}, {WIN_Y + WIN_H}}}
          set URL of active tab of w to "https://gemini.google.com/app"
        end tell
        """
    )


def focus_gemini():
    osascript(
        f"""
        tell application "Google Chrome"
          activate
          set w to first window whose URL of active tab contains "gemini.google.com"
          set index of w to 1
          set bounds of w to {{{WIN_X}, {WIN_Y}, {WIN_X + WIN_W}, {WIN_Y + WIN_H}}}
        end tell
        """
    )


def find_download_button():
    """
    Captures the lightbox toolbar strip and locates the Download (down-arrow) icon
    immediately to the left of the white 'Save' pill button.
    Returns (screen_x, screen_y) or None if lightbox isn't open.
    """
    strip_path = "/tmp/gemini_toolbar_strip.png"
    # Toolbar sits around screen y = 145..200 in a 1046x768 window at (22, 47)
    subprocess.run(
        ["screencapture", "-R22,140,1046,65", strip_path],
        check=True,
    )
    im = Image.open(strip_path).convert("RGB")
    w, h = im.size

    # 1. Detect the white 'Save' pill on the right (x > 850): dense bright pixels
    save_cols = []
    for x in range(850, w - 10):
        bright = sum(1 for y in range(10, h - 10) if sum(im.getpixel((x, y))) > 650)
        if bright > 15:
            save_cols.append(x)

    if len(save_cols) < 30:
        return None

    save_left = min(save_cols)

    # 2. Scan left of save_left for white icon clusters (Share, Copy, Download)
    # Each icon is ~18-24px wide, separated by ~20-30px dark gaps
    clusters = []
    in_cluster = False
    c_start = 0
    for x in range(max(600, save_left - 250), save_left - 12):
        col_bright = sum(1 for y in range(12, h - 12) if sum(im.getpixel((x, y))) > 420)
        if col_bright >= 2 and not in_cluster:
            in_cluster = True
            c_start = x
        elif col_bright < 2 and in_cluster:
            in_cluster = False
            if x - c_start >= 6:
                clusters.append((c_start, x - 1))

    if not clusters:
        return None

    # In clean lightbox (no edits), Download is the rightmost icon before Save.
    # If Undo/Redo exist (unlikely), there would be 5 clusters and Download is index 2.
    if len(clusters) >= 5:
        target = clusters[2]
    else:
        target = clusters[-1]

    icon_x = (target[0] + target[1]) // 2
    # Find vertical center of bright pixels in this cluster
    ys = [
        y
        for x in range(target[0], target[1] + 1)
        for y in range(10, h - 10)
        if sum(im.getpixel((x, y))) > 420
    ]
    icon_y = (min(ys) + max(ys)) // 2 if ys else 27

    return (WIN_X + icon_x, 140 + icon_y)


def generate_one(item):
    target_path = os.path.join(ASSETS_DIR, item["filename"])
    print(f"\n[{item['id']}/11] Generating: {item['filename']}")
    print(f"       Title: {item['title']}")

    focus_and_reset_gemini()
    time.sleep(4.0)

    # Click 'Ask Gemini' input box
    focus_gemini()
    time.sleep(0.3)
    click(622, 475)
    time.sleep(0.4)

    # Copy prompt and paste + Enter
    prompt_text = "Generate a 16:9 widescreen image: " + item["prompt"]
    subprocess.run(["pbcopy"], input=prompt_text.encode("utf-8"), check=True)
    osascript('tell application "System Events" to keystroke "v" using command down')
    time.sleep(0.5)
    osascript('tell application "System Events" to key code 36')

    print("       Prompt submitted. Waiting 32s for Imagen 3 generation...")
    time.sleep(32.0)

    # Try opening Lightbox and finding Download button (up to 3 attempts)
    dl_coords = None
    for attempt in range(3):
        focus_gemini()
        time.sleep(0.4)
        click(422, 447)
        time.sleep(1.8)
        dl_coords = find_download_button()
        if dl_coords:
            break
        print(f"       Lightbox not ready yet (attempt {attempt + 1}/3), waiting 12s...")
        time.sleep(12.0)

    if not dl_coords:
        print(f"  [ERROR] Could not locate Download button for {item['filename']}. Skipping.")
        return False

    print(f"       Found Download button at {dl_coords}. Downloading...")
    before = set(glob.glob(os.path.join(DOWNLOADS_DIR, "*")))
    focus_gemini()
    time.sleep(0.2)
    click(*dl_coords)

    # Wait up to 20s for new complete image file in ~/Downloads
    downloaded_file = None
    for _ in range(40):
        time.sleep(0.5)
        after = set(glob.glob(os.path.join(DOWNLOADS_DIR, "*")))
        diff = [
            f
            for f in (after - before)
            if not f.endswith(".crdownload")
            and not f.endswith(".tmp")
            and os.path.splitext(f)[1].lower() in (".png", ".jpg", ".jpeg", ".webp")
        ]
        if diff:
            downloaded_file = sorted(diff, key=os.path.getmtime)[-1]
            # Wait briefly to make sure write finished
            time.sleep(0.5)
            break

    if not downloaded_file:
        print(f"  [ERROR] Download timed out for {item['filename']}.")
        return False

    im = Image.open(downloaded_file).convert("RGB")
    im.save(target_path, "JPEG", quality=92)
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"  [OK] Saved {target_path} ({im.size[0]}x{im.size[1]}, {size_kb:.1f} KB)")
    return True


def main():
    force = "--force" in sys.argv
    with open(PROMPTS_FILE, "r", encoding="utf-8") as f:
        prompts = json.load(f)

    os.makedirs(ASSETS_DIR, exist_ok=True)
    ok_count = 0
    fail_count = 0

    for item in prompts:
        target_path = os.path.join(ASSETS_DIR, item["filename"])
        if os.path.exists(target_path) and not force:
            print(f"[{item['id']}/11] Skipping existing {item['filename']}")
            ok_count += 1
            continue
        if generate_one(item):
            ok_count += 1
        else:
            fail_count += 1

    print(f"\n=== COMPLETE: {ok_count}/11 succeeded, {fail_count} failed ===")


if __name__ == "__main__":
    main()
