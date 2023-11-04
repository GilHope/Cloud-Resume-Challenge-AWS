import { test, expect } from '@playwright/test';

test('Smoke Test', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  const title = await page.title();
  // Update the expected title to match the actual title
  expect(title).toBe('Fast and reliable end-to-end testing for modern web apps | Playwright');
});
