import { chromium, Browser, Page } from 'playwright';

(async () => {
  const browser: Browser = await chromium.launch();
  const page: Page = await browser.newPage();

  try {
    // Navigate to the website
    await page.goto('https://ghope.cloud');

    // Wait for the text "Gil D. Hope" to appear on the page
    await page.waitForSelector('text="Gil D. Hope"');

    console.log('Website opened, and it displays "Gil D. Hope".');
  } catch (error) {
    console.error('Error:', error);
  } finally {
    // Close the browser
    await browser.close();
  }
})();


// Current dilemma: ' Error: Cannot find module 'fs/promises' '
