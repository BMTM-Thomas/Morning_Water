import asyncio
from playwright.async_api import async_playwright

EXTENSION_PATH = "/Users/n02-19/Downloads/lastPass"  # Path to Chrome extension

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,  # Run in visible mode
            args=[
                f"--disable-extensions-except={EXTENSION_PATH}",
                f"--load-extension={EXTENSION_PATH}",
                "--disable-infobars",
                "--disable-blink-features=AutomationControlled",
                "--disable-popup-blocking",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--start-maximized",
                "--no-default-browser-check",
                "--no-first-run",
                "--hide-crash-restore-bubble"
            ],
        )

        # Save cookies
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()

        await page.goto("https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A%2F%2Fusercenter2-intl.aliyun.com%2Fbilling%2F#/account/overview", timeout=60000)
        await context.storage_state(path="auth.json")

        await page.wait_for_timeout(5000)

        # ---------------------
        await page.close()
        await context.close()
        await browser.close()

# Run the async function
asyncio.run(run())
