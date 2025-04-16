from playwright.sync_api import sync_playwright
import time

EXTENSION_PATH = "/Users/n02-19/Downloads/lastPass"  # Path to Chrome extension

try:
    cookies_list = ["ven128", "ven137", "ven231", "ven244"]

    for index, item in enumerate(cookies_list):
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
        
            # load cookies
            context = browser.new_context(storage_state=f"./store_Cookies/ven295.json", no_viewport=True)
            storage_state={"cookies": []}

            page = context.new_page()

            page.goto("https://console.tencentcloud.com/live/resources/package")
            time.sleep(11111)

            # ---------------------
            page.close()
            context.close()
            browser.close()

except Exception as e:
    print(f"Error: {e}")

    

    






    
