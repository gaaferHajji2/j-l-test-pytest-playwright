from playwright.sync_api import sync_playwright

import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto('https://bootswatch.com/flatly/')
    xpath_locator = "//a[@id='themes']"
    t1 = page.locator(f"xpath={xpath_locator}")
    t1.click()
    t1.dblclick()
    time.sleep(2)