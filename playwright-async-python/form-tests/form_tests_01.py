import asyncio
from math import exp
from playwright.async_api import async_playwright, expect

async def test_go_to():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto('https://www.testmu.ai/selenium-playground/simple-form-demo/')
        await expect(page).to_have_title("Selenium Grid Online | Run Selenium Test On Cloud")

        await page.close()
        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_go_to())