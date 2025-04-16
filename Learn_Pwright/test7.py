import re
import time
import math
import certifi
import pyautogui
from playwright.sync_api import sync_playwright, expect
from PIL import ImageGrab
from bson import ObjectId 
from List_Zentao import *

# Chrome Extension
EXTENSION_PATH = "/Users/n02-19/Desktop/playWright/chrome_Extension/lastPass"  # Extension 1
EXTENSION_PATH2 = "/Users/n02-19/Desktop/playWright/chrome_Extension/SelectorHub"  # Extension 2
USER_DATA_DIR = "/Users/n02-19/PlaywrightProfile"  # User Profile

# mongodb id
m_id = 0

with sync_playwright() as p:    
    browser = p.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,  # Extensions do NOT work in headless mode
        args=[
            f"--disable-extensions-except={EXTENSION_PATH},{EXTENSION_PATH2}", # Adding Multiple Extensions, dont add any space after "," , else not working
            f"--load-extension={EXTENSION_PATH},{EXTENSION_PATH2}", # Adding Multiple Extensions, dont add any space after "," , else not working
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

    # Launch a new browser page
    page = browser.pages[0] 
    page.goto("https://zr-zentao2023.cccqx.com/zentao/execution-kanban-26.html")


    # switch to iframe
    iframe = page.frame_locator("#appIframe-project")

    expect(iframe.locator("xpath=//span[@title='已關閉']")).to_be_visible(timeout= 0) # "已關閉"
    expect(iframe.locator("xpath=//span[@title='已關閉']")).to_be_visible(timeout= 0) # "已關閉"
    
    pyautogui.click(1515,788)
    pyautogui.click(1515,788)

    time.sleep(1)

    for i in range(999):
        pyautogui.moveTo(1496,377)
        time.sleep(1)
        pyautogui.click(1496,377)
        time.sleep(1)
        pyautogui.click(1538,510)
        time.sleep(3)
        pyautogui.click(964,189)
        time.sleep(31111)





 


    