from playwright.sync_api import sync_playwright
import time
import re

EXTENSION_PATH = "/Users/n02-19/Downloads/lastPass"  # Extension
USER_DATA_DIR = "/Users/n02-19/PlaywrightProfile"  # User Profile

with sync_playwright() as p:    
    browser = p.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,  # Extensions do NOT work in headless mode
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
        no_viewport=True,
    )

    page = browser.pages[0] 

    page.goto("https://www.aliyun.com/en")
    page.wait_for_timeout(90000) 
    # get text
    page_text = page.content()

    # get title
    title = page.title()

    # wait
    page.wait_for_timeout(2000) 


    page.close()
    


