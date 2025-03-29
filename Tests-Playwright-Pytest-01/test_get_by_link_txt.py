from playwright.sync_api import sync_playwright

# Same as: playwright = sync_playwright().start()
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)

    page = browser.new_page()

    page.goto("https://playwright.dev/python")

    docs_btn = page.get_by_role('link', name='Docs')

    docs_btn.highlight()

    print("The Current URL Is: ", page.url)

    docs_btn.click()

    print("The Current URL Is: ", page.url)

    browser.close()
    # Here as we use with, then close()-method will call automatically
    # playwright.close()