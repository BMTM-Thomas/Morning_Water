import time
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
m_id = 8

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
    expect(page.locator("xpath=//h1[normalize-space()='Hello Nymph Names']")).to_be_visible(timeout= 0) # ""Hello Nymph Names""

    # Extract Credit
    credit = page.locator(f"xpath=/html/body/div[1]/div[3]/div/div[3]/div/div[2]/div/p/span").text_content()
    credit = credit.replace('$', "")
    credit = credit.replace(" ","")

    # MongoDB Update Data
    mangos_id = {'_id': ObjectId(mongodb_id[m_id])}
    collection.update_one(mangos_id, {"$set": {"Credit": credit}})
    print(f"Namecheap: {credit}")

    # Screenshot
    ImageGrab.grab().save('./早班水位/ven388.png')

    time.sleep(1)

    page.close()
    browser.close()
    


