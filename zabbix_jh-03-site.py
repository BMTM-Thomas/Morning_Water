import time
import certifi
import pyautogui
import pyperclip
import re
from playwright.sync_api import sync_playwright, expect
from pymongo import MongoClient
from PIL import ImageGrab
from bson import ObjectId 
from List_Zentao import *

# Serverless
def mongodb_atlas():
    # MongoDB Atlas (Server)
    client = MongoClient("mongodb+srv://thomasleong:8zvnWrT3sf8N2u7x@cluster0.ef0wowh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",tlsCAFile=certifi.where())
    # Access Database
    db = client["Thomas"]
    # Access Collection
    return db["Morning_Database"]

# Chrome Extension
EXTENSION_PATH = "/Users/n02-19/Desktop/playWright/chrome_Extension/lastPass"  # Extension
EXTENSION_PATH2 = "/Users/n02-19/Desktop/playWright/chrome_Extension/SelectorHub"  # Extension
USER_DATA_DIR = "/Users/n02-19/PlaywrightProfile"  # User Profile

# mongodb id
m_id = 24

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

    # Launch MongoDB Atlas
    collection = mongodb_atlas()

    # Launch a new browser page
    page = browser.pages[0] 
    page.goto("https://zr-zbx-pfedge.cccqx.com/index.php?request=zabbix.php%3Fname%3D243%26evaltype%3D0%26tags%255B0%255D%255Btag%255D%3D%26tags%255B0%255D%255Boperator%255D%3D0%26tags%255B0%255D%255Bvalue%255D%3D%26show_tags%3D3%26tag_name_format%3D0%26tag_priority%3D%26filter_name%3D%26filter_show_counter%3D0%26filter_custom_time%3D0%26sort%3Dname%26sortorder%3DASC%26show_details%3D0%26action%3Dlatest.view", wait_until="domcontentloaded")
    
    # wait for logo appear
    expect(page.locator("xpath=//div[@class='zabbix-logo']")).to_be_visible(timeout= 0) # wait for logo appear

    # click lastpass extension       
    pyautogui.click(x=1359, y=62)

    # Wait for lastpass vault button image to appear
    image_vault = None
    while image_vault is None:
        image_vault = pyautogui.locateOnScreen("./image/vault.png", grayscale = True)

    # lastpass search ven and click 
    time.sleep(1)
    # import zabbix from List_zentao.py
    pyperclip.copy(zabbix)
    pyautogui.hotkey("command", "v")
    time.sleep(1)
    pyautogui.click(x=1165, y=177)
    time.sleep(1)

    # Button click  
    nc_click_login = page.locator("xpath=//button[@id='enter']")
    nc_click_login.click(force=True) # "click sign in "

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//a[normalize-space()='Ven243(all sites): total throughput this month']")).to_be_visible(timeout= 0) # "Ven243(all sites): total throughput this month"
    expect(page.locator("xpath=//h1[@id='page-title-general']")).to_be_visible(timeout= 0) # Latest data

    pyautogui.click(1594, 799)

    # Extract Credit
    credit = page.locator(f"//tbody/tr[5]/td[5]").text_content()
    match = re.findall(r'(\d+\.\d+)\s*([TGMK]B)', credit)
    credit = match[0][0]
    unit = match[0][1]
    time.sleep(0.5)

    # Screenshot
    ImageGrab.grab().save(f'./早班水位/zabbix.png')
    time.sleep(0.5)

    # MongoDB Update Data
    mangos_id = {'_id': ObjectId(mongodb_id[m_id])}
    collection.update_one(mangos_id, {"$set": {"Credit": credit}})
    print(f"zabbix: {credit} {unit}")

    pyautogui.moveTo(22, 798)

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//a[normalize-space()='Sign out']")).to_be_visible(timeout= 0) # "sign out"
    time.sleep(1)

    # Button click  
    click_logout = page.locator("xpath=//a[normalize-space()='Sign out']")
    click_logout.click(force=True) # "sign out"
    
    time.sleep(1)

    page.close()
    browser.close()
    


