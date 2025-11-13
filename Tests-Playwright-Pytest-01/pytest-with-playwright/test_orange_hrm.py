from playwright.sync_api import Page
import time

def test_orange_hrm_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username = page.get_by_placeholder("Username")
    username.fill("Admin")
    password = page.get_by_placeholder("Password")
    password.fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_selector("css=canvas[height='265']", state='attached')
    assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"