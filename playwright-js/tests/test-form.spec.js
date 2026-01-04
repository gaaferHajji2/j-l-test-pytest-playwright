import { test, expect } from "@playwright/test"

test("check the msg", async ({ page }) => {
    await page.goto("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    await page.locator("#user-message").fill("Jafar Loka")
    await page.locator("#showInput").click()
    expect(page.locator("message")).toHaveText("Jafar Loka")
})

test("Check sum", async ({ page }) => {
    await page.goto("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    await page.locator("#sum1").fill(1)
    await page.locator("#sum2").fill(2)
    expect(page.locator("#addmessage")).toHaveText("3")
})