import time
import math
import certifi
import pyautogui
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

    # Launch MongoDB Atlas
    collection = mongodb_atlas()

    # Launch a new browser page
    page = browser.pages[0] 
    page.goto("https://ap.www.namecheap.com/", wait_until="domcontentloaded")
    
    # Waiting for specific text to be appear
    expect(page.locator("xpath=//h1[normalize-space()='Log In to Your Account']")).to_be_visible(timeout= 0) # "Log in to your account"

    # click lastpass extension       
    pyautogui.click(x=1359, y=62)

    # Wait for lastpass vault button image to appear
    image_vault = None
    while image_vault is None:
        image_vault = pyautogui.locateOnScreen("./image/vault.png", grayscale = True)

    # lastpass search ven and click 
    time.sleep(1)
    # import aliyun_id from List_zentao.py, ven_id = ven293, ven324, ven319, ven365 ...
    pyautogui.write(namecheap)
    time.sleep(1)
    pyautogui.click(x=1145, y=240)
    time.sleep(1)

    # Button click  
    nc_click_login = page.locator("xpath=/html/body/form[1]/div[3]/div/div/div/ul/li/fieldset/div[4]/input")
    nc_click_login.click(force=True) # "click 登录"

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//h2[normalize-space()='Account Balance']")).to_be_visible(timeout= 0) # "Account Balance"

    # Extract Credit
    credit = page.locator(f"//span[normalize-space()='$3 075.42']").text_content()
    credit = credit.replace('$', "")

    # MongoDB Update Data
    mangos_id = {'_id': ObjectId(mongodb_id[m_id])}
    collection.update_one(mangos_id, {"$set": {"Credit": credit}})
    print(f"{tencent_CN_ID[0]}= {credit}")

    page.close()
    browser.close()
    


