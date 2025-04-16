import re
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

# for tencent_int_ID tuple
x = 0

# credit purpose
unused_credit = 0.0

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
    page.goto("https://intl.cloud.tencent.com/account/login", wait_until="load")

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//div[@class='LoginCommonBox_clg-mod-title__gpSTl']")).to_be_visible(timeout= 0) # "邮箱登录"
    expect(page.locator("xpath=//button[@type='submit']")).to_be_visible(timeout= 0) # "登陆"
    
    # click lastpass extension       
    pyautogui.click(x=1359, y=62)

    # Wait for lastpass vault button image to appear
    image_vault = None
    while image_vault is None:
        image_vault = pyautogui.locateOnScreen("./image/vault.png", grayscale = True)

    # lastpass search ven and click 
    time.sleep(1)
    # import aliyun_id from List_zentao.py, ven_id = ven293, ven324, ven319, ven365 ...
    pyautogui.write(tencent_Int_ID[x])
    time.sleep(1)
    pyautogui.click(x=1175, y=179)
    time.sleep(1)

    # Button click  
    b_login = page.locator("xpath=//button[@type='submit']")
    b_login.click(force=True) # "click 登录"

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//div[@class='intl-product-service__title']")).to_be_visible(timeout= 0) # "产品与服务"
    time.sleep(1)

    # go to 资源包/插件管理
    page.goto("https://console.tencentcloud.com/live/resources/package?language=zh", wait_until="load")

    # Button click  
    b_login = page.locator("xpath=//a[contains(text(),'流量包')]")
    b_login.click(force=True) # "click 流量包"
    
    # Waiting for specific text to be appear
    expect(page.locator("xpath=//div[contains(text(),'自动续购状态')]")).to_be_visible(timeout= 0) # "自动续购状态"
    expect(page.locator("xpath=//tbody/tr[3]/td[2]/div[1]/span[1]")).to_be_visible(timeout= 0) # ""云直播流量包""
    
    # Count 资源包 total number of tr
    total_rows = len(page.locator("//tbody/tr").all()) 
    print(total_rows)

    # Extract Credit
    try:
        for item in range(1, total_rows):
            # Check Status, 未使用 or 使用中
            check_Status = page.locator(f"xpath=//tbody/tr[{item}]/td[6]").text_content()
            # Check Credit
            check_Credit = page.locator(f"xpath=//tbody/tr[{item}]/td[3]").text_content()
            
            # if is "未使用" then do something...
            if check_Status == "未使用":
                # filter unused credit
                match = re.search(r'总量：([\d.]+)\s*TB', check_Credit)
                if match:
                    unused_credit = float(match.group(1))
                    print(f"Non-Used_Credit: {unused_credit} TB" )  

            # else if is "使用中" then do something...
            elif check_Status == "使用中":
                # filter unused credit
                used_Credit = re.search(r'已使用：([\d.]+)\s*([TG]B)', check_Credit)
                total_Credit = re.search(r'总量：([\d.]+)\s*TB', check_Credit)

                # Arrange unit and number to the exact variable
                unit = used_Credit.group(2)
                used_Credit = float(used_Credit.group(1))
                total_Credit = float(total_Credit.group(1))

                # Convert GB to TB, if have...
                if unit == "GB":
                    used_Credit /= 1024

                # math 总量 - 已使用
                used_Credit = total_Credit - used_Credit
                print(f"Used_Credit: {used_Credit} TB")
            else:
                pass
        
        # Final Total/Result = 未使用 + 使用中, and convert to 3 decimal place
        total = unused_credit + used_Credit
        # Convert to 3 decimal places, without Rounding
        total = math.floor(total * 1000) / 1000

        # MongoDB Update Data
        mangos_id = {'_id': ObjectId(mongodb_id[m_id])}
        collection.update_one(mangos_id, {"$set": {"Credit": total}})
        print(f"ven295: {total} TB")
        m_id += 1

        pyautogui.moveTo(1551, 163)
        expect(page.locator("xpath=//a[contains(text(),'账号信息')]")).to_be_visible(timeout= 0) # "账号信息"

        # Screenshot
        ImageGrab.grab().save(f'./早班水位/{tencent_Int_ID[x]}.png')
        time.sleep(0.5)

        # Button Click Logout
        b_logout = page.locator("xpath=//a[contains(text(),'退出')]")
        b_logout.click(force=True) # "click 退出"
        time.sleep(2)

    except Exception as e:  # Catch any error
            print(f"Error occurred: {e}")
            pass



    