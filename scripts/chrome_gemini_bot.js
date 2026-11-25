#!/usr/bin/env node

/**
 * Autonomous Gemini Pro Image Generation Bot using Chrome DevTools Protocol & Puppeteer
 *
 * Connects to Google Chrome running with:
 * /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 &
 */

const fs = require('fs');
const path = require('path');
const puppeteer = require('/Users/kalyan/Downloads/2026/Sep2026/Data Centers and Way Head/node_modules/puppeteer-core');

const BASE_DIR = path.resolve(__dirname, '..');
const PROMPTS_FILE = path.join(BASE_DIR, 'scripts', 'image_prompts.json');
const ASSETS_DIR = path.join(BASE_DIR, 'assets');

// Parse CLI Arguments
const args = process.argv.slice(2);
let port = 9222;
let filterId = null;
let filterFilename = null;
let forceOverwrite = false;

args.forEach(arg => {
  if (arg.startsWith('--port=')) {
    port = parseInt(arg.replace('--port=', '').trim(), 10);
  } else if (arg.startsWith('--id=')) {
    filterId = parseInt(arg.replace('--id=', '').trim(), 10);
  } else if (arg.startsWith('--filename=')) {
    filterFilename = arg.replace('--filename=', '').trim();
  } else if (arg === '--force') {
    forceOverwrite = true;
  }
});

if (!fs.existsSync(PROMPTS_FILE)) {
  console.error(`Error: Prompts file not found at ${PROMPTS_FILE}`);
  process.exit(1);
}

if (!fs.existsSync(ASSETS_DIR)) {
  fs.mkdirSync(ASSETS_DIR, { recursive: true });
}

const allPrompts = JSON.parse(fs.readFileSync(PROMPTS_FILE, 'utf8'));
const allowedFiles = filterFilename ? filterFilename.split(',').map(s => s.trim()) : null;
const queue = allPrompts.filter(item => {
  if (allowedFiles && !allowedFiles.includes(item.filename)) return false;
  if (filterId !== null && item.id !== filterId) return false;
  const targetPath = path.join(ASSETS_DIR, item.filename);
  if (fs.existsSync(targetPath) && !forceOverwrite) {
    return false;
  }
  return true;
});

console.log('\n=============================================================');
console.log('🤖 CHROME GEMINI PRO AUTOMATION BOT (PUPPETEER CDP)');
console.log('=============================================================');
console.log(`🔌 Target Chrome Port      : ${port}`);
console.log(`📁 Target Assets Directory : ${ASSETS_DIR}`);
console.log(`📋 Total Prompts in Queue  : ${queue.length} of ${allPrompts.length}`);
if (filterId !== null) console.log(`🔍 Filter ID               : Item ${filterId}`);
if (filterFilename) console.log(`🔍 Filter Filename          : ${filterFilename}`);
console.log('=============================================================\n');

if (queue.length === 0) {
  console.log('✨ All images in queue already exist in assets/! Use --force to regenerate.\n');
  process.exit(0);
}

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
  let browser;
  try {
    console.log(`⏳ Connecting to Chrome on http://127.0.0.1:${port}...`);
    browser = await puppeteer.connect({
      browserURL: `http://127.0.0.1:${port}`,
      defaultViewport: null
    });
    console.log(`✅ Connected successfully to Google Chrome!`);
  } catch (err) {
    console.error(`\n❌ Could not connect to Google Chrome on port ${port}.`);
    console.error(`Error: ${err.message}`);
    process.exit(1);
  }

  // Find or create Gemini tab
  const pages = await browser.pages();
  let geminiPage = pages.find(p => p.url().includes('gemini.google.com'));

  if (!geminiPage) {
    console.log(`🌐 Opening a new tab navigating to https://gemini.google.com/app...`);
    geminiPage = await browser.newPage();
    await geminiPage.goto('https://gemini.google.com/app', { waitUntil: 'networkidle2' });
  } else {
    console.log(`🌐 Found active Gemini tab: ${geminiPage.url()}`);
    await geminiPage.bringToFront();
  }

  console.log(`⏳ Checking Gemini chat interface...`);
  await geminiPage.waitForSelector('rich-textarea, div[contenteditable="true"], textarea', { timeout: 30000 })
    .catch(() => console.log('⚠️ Notice: Make sure you are logged into your Gemini Pro account on the opened browser window.'));

  let successCount = 0;
  let failureCount = 0;

  for (let i = 0; i < queue.length; i++) {
    const item = queue[i];
    const targetFile = path.join(ASSETS_DIR, item.filename);

    console.log(`\n-------------------------------------------------------------`);
    console.log(`[${i + 1}/${queue.length}] 🎨 Generating Item ${item.id} (${item.section})`);
    console.log(`   📄 Output File : ${item.filename}`);
    console.log(`   🎯 Subject     : ${item.title}`);
    console.log(`-------------------------------------------------------------`);

    let promptSent = false;
    let attempts = 0;

    while (attempts < 2 && !promptSent) {
      attempts++;
      try {
        await geminiPage.goto('https://gemini.google.com/app', { waitUntil: 'networkidle2' });
        await sleep(3000);
        await geminiPage.waitForSelector('rich-textarea, div[contenteditable="true"], textarea', { timeout: 20000 }).catch(() => {});

        // Record existing image URLs in DOM before sending prompt
        const existingImageUrls = await geminiPage.evaluate(() => {
          return Array.from(document.querySelectorAll('img')).map(img => img.src).filter(Boolean);
        });

        // Focus and type prompt into Gemini input box
        const promptFull = `Generate a high-quality 16:9 widescreen technological architectural infographic image: ${item.prompt}`;
        
        await geminiPage.evaluate((text) => {
          const input = document.querySelector('rich-textarea p, rich-textarea div[contenteditable="true"], div[contenteditable="true"] p, div[contenteditable="true"], textarea');
          if (input) {
            input.focus();
            input.innerText = text;
            input.dispatchEvent(new Event('input', { bubbles: true }));
          }
        }, promptFull);

        await sleep(1500);

        // Click Send button
        const clicked = await geminiPage.evaluate(() => {
          const sendBtn = document.querySelector('button[aria-label="Send message"], button.send-button, mat-icon[data-mat-icon-name="send"]')?.closest('button');
          if (sendBtn && !sendBtn.disabled) {
            sendBtn.click();
            return true;
          }
          return false;
        });

        if (!clicked) {
          await geminiPage.keyboard.press('Enter');
        }

        console.log(`   📤 Prompt submitted. Waiting for Imagen 3 generation...`);
        promptSent = true;

        // Wait for new generated image to appear in DOM
        let imageBuffer = null;
        let waitAttempts = 0;

        while (!imageBuffer && waitAttempts < 40) {
          await sleep(3000);
          waitAttempts++;

          const newImageData = await geminiPage.evaluate((existingUrls) => {
            const allImages = Array.from(document.querySelectorAll('img'));
            const candidates = allImages.filter(img => 
              img.src && 
              !existingUrls.includes(img.src) &&
              (img.src.includes('googleusercontent.com') || img.src.startsWith('blob:') || img.src.startsWith('data:image')) &&
              img.naturalWidth > 350
            );

            if (candidates.length > 0) {
              const latest = candidates[candidates.length - 1];
              return { src: latest.src, width: latest.naturalWidth, height: latest.naturalHeight };
            }
            return null;
          }, existingImageUrls);

          if (newImageData) {
            console.log(`   🖼️ Image detected in chat (${newImageData.width}x${newImageData.height})! Fetching raw image bytes...`);
            
            // Extract base64 image data directly from browser canvas
            const base64Data = await geminiPage.evaluate((imgSrc) => {
              const img = Array.from(document.querySelectorAll('img')).find(i => i.src === imgSrc);
              if (!img || !img.complete || img.naturalWidth === 0) return null;
              try {
                const canvas = document.createElement('canvas');
                canvas.width = img.naturalWidth;
                canvas.height = img.naturalHeight;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);
                const dataUrl = canvas.toDataURL('image/jpeg', 0.95);
                return dataUrl.split(',')[1];
              } catch (e) {
                return null;
              }
            }, newImageData.src);

            if (base64Data) {
              imageBuffer = Buffer.from(base64Data, 'base64');
            }
          }
        }

        if (imageBuffer) {
          fs.writeFileSync(targetFile, imageBuffer);
          const stats = fs.statSync(targetFile);
          console.log(`   ✅ Successfully saved: assets/${item.filename} (${(stats.size / 1024 / 1024).toFixed(2)} MB)`);
          successCount++;
        } else {
          console.error(`   ⚠️ Timed out waiting for ${item.filename} (120s). Skipping to next...`);
          failureCount++;
        }

      } catch (err) {
        console.error(`   ❌ Error during attempt ${attempts}: ${err.message}`);
        await sleep(3000);
      }
    }

    // Cooling pause between generations
    if (i < queue.length - 1) {
      console.log(`   ☕ Pausing 4 seconds before next prompt...`);
      await sleep(4000);
    }
  }

  console.log('\n=============================================================');
  console.log(`🎉 GENERATION SUMMARY`);
  console.log(`   ✅ Successful : ${successCount}`);
  console.log(`   ⚠️ Failed     : ${failureCount}`);
  console.log(`   📁 Output Dir : ${ASSETS_DIR}`);
  console.log('=============================================================\n');
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
