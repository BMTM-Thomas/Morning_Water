from playwright.sync_api import sync_playwright
import time

EXTENSION_PATH = "/Users/n02-19/Downloads/lastPass"  # Path to Chrome extension

with sync_playwright() as p:
    browser = p.chromium.launch(
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

    # save cookies
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://console.tencentcloud.com/live/resources/package", timeout=0)
    time.sleep(30)
    context.storage_state(path="ven295.json")

    time.sleep(11111)

    # ---------------------
    page.close()
    context.close()
    browser.close()
