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
m_id = 6

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
    page.goto("https://cloud.tencent.com/login/?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2Fcdn%2Fpackage", wait_until="load")

    # if "子用户登录" appear, change to 邮箱登录
    if page.locator("xpath=//h3[contains(text(),'子用户登录')]"): # "子用户登录"
        # Button click 
        b_switch = page.locator("xpath=//button[@class='accsys-control-panel__header-back']")
        b_switch.click(force=True) # "切换登录方式"

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//div[contains(text(),'邮箱登录')]")).to_be_visible(timeout= 0) # "邮箱登录"
    expect(page.locator("xpath=//div[contains(text(),'微信登录')]")).to_be_visible(timeout= 0) # "微信登录"

    time.sleep(1)

    # Button click 
    c_email = page.locator("xpath=//div[contains(text(),'邮箱登录')]") 
    c_email.click(force=True) # "click 邮箱登录上次登录"

    time.sleep(1)
    
    # click lastpass extension       
    pyautogui.click(x=1359, y=62)

    # Wait for lastpass vault button image to appear
    image_vault = None
    while image_vault is None:
        image_vault = pyautogui.locateOnScreen("./image/vault.png", grayscale = True)

    # lastpass search ven and click 
    time.sleep(1)
    # import aliyun_id from List_zentao.py, ven_id = ven293, ven324, ven319, ven365 ...
    pyautogui.write(tencent_CN_ID)
    time.sleep(1)
    pyautogui.click(x=1175, y=179)
    time.sleep(1)

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//span[@class='accsys-tp-btn__text'][contains(text(),'登录')]")).to_be_visible(timeout= 0) # "登录"

    # Button click  
    c_email = page.locator("xpath=//span[@class='accsys-tp-btn__text'][contains(text(),'登录')]")
    c_email.click(force=True) # "click 登录"

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//h2[contains(text(),'资源包管理')]")).to_be_visible(timeout= 0) # "资源包管理"
    expect(page.locator("xpath=//div[contains(text(),'剩余流量包')]")).to_be_visible(timeout= 0) # "剩余流量包"

    time.sleep(1)

    # Extract Credit
    credit = page.locator(f"//span[normalize-space()='10']").text_content()

    # MongoDB Update Data
    mangos_id = {'_id': ObjectId(mongodb_id[m_id])}
    collection.update_one(mangos_id, {"$set": {"Credit": credit}})
    print(f"{tencent_CN_ID[0]}= {credit}")

    # delay 1second
    page.wait_for_timeout(1000)

    # hover to menu
    pyautogui.moveTo(1505, 158)

    # wait for specific text to be appear
    expect(page.locator("xpath=//span[contains(text(),'账号信息')]")).to_be_visible(timeout= 0)

    # Screenshot
    ImageGrab.grab().save(f'./早班水位/{tencent_CN_ID}.png')

    # delay 1second
    page.wait_for_timeout(500)

    # Button click Logout
    b_Logout = page.locator("xpath=//button[contains(text(),'退出')]").click(force=True) # "click 退出"
    
    # delay 1second
    page.wait_for_timeout(1000)