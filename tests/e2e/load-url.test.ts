import { test, expect } from '@playwright/test';

test('Smoke Test', async ({ page }) => {
  await page.goto('https://ghope.cloud/');
  const title = await page.title();
  // Update the expected title to match the actual title
  expect(title).toBe('Gil D. Hope');
});
