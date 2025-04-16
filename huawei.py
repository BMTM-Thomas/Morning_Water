import time
import re
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
    page.goto("https://auth.huaweicloud.com/authui/login.html?id=hid_vz7bw73fbmbylhj&locale=zh-cn#/login", wait_until="domcontentloaded")
    
    # Waiting for specific text to be appear
    expect(page.locator(".loginTypeDiv")).to_contain_text("IAM用户登录", timeout=30000) # "IAM用户登录"
    expect(page.locator(".accountLogin")).to_contain_text("密码登录", timeout=30000) # "密码登录"

    # click lastpass extension 
    pyautogui.click(x=1359, y=62)

    # Wait for lastpass vault button image to appear
    image_vault = None
    while image_vault is None:
        image_vault = pyautogui.locateOnScreen("./image/vault.png", grayscale = True)

    # lastpass search ven and click 
    time.sleep(1)
    # import huawei_id
    pyautogui.write(huawei_ID)
    time.sleep(1)
    pyautogui.click(x=1175, y=179)
    time.sleep(1)

    # Button click Login
    b_Login = page.locator("xpath=//span[@id='btn_submit']").click(force=True)  # "登录"

    # if 登录验证 appear
    try:
        # 登录验证
        huawei_auth = expect(page.locator("xpath=//p[@class='ng-binding']")).to_be_visible(timeout= 2000) # "登录验证"
        
        # Waiting for specific text to be appear
        expect(page.locator("xpath=//div[@class='device-type ng-binding']")).to_be_visible(timeout= 30000) # "MFA设备类型"

        # mark checkbox
        page.check("//input[@id='promptBindAndEnableCheckbox']")

        # Button click 暂不绑定
        b_nonLock = page.locator("xpath=//div[@id='promptBindAndEnableCancelBtn']").click(force=True)  
    except:
        pass
    
    # Waiting for specific text to be appear
    expect(page.locator("xpath=//div[@class='cloud-title title-font']")).to_be_visible(timeout= 30000) # "安全概览"
    expect(page.locator("xpath=//span[contains(text(),'新手入门')]")).to_be_visible(timeout= 30000) # "新手入门"

    # page go to 内容分发网络 CDN
    page.goto("https://console-intl.huaweicloud.com/cdn/?agencyId=8ce23e76ae5d4581bba8ff627db33ab5&region=cn-north-4&locale=zh-cn#/cdn/overview", wait_until="load")

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//span[@class='ti-service-header-card-left-title']")).to_be_visible(timeout= 30000) # "总览"
    expect(page.locator("xpath=/html/body/div[3]/app-root/ti-app-layout/div[2]/div[2]/layout-default/ti-app-layout-main/div[2]/div[2]/div[1]/ti-app-layout-main-content/tp-layout-content/app-overview/app-overview-data-trends/tp-layout-content-body/tp-layout-column[2]/div/tp-layout-section[2]/app-resource-package/div/div[1]/div")).to_be_visible(timeout= 30000) # 资源包
    expect(page.locator("xpath=//div[normalize-space()='CDN']")).to_be_visible(timeout= 30000) # "CDN中国大陆流量包 （25个）"

    # Extract Credit
    credit = page.locator(f"xpath=/html/body/div[3]/app-root/ti-app-layout/div[2]/div[2]/layout-default/ti-app-layout-main/div[2]/div[2]/div[1]/ti-app-layout-main-content/tp-layout-content/app-overview/app-overview-data-trends/tp-layout-content-body/tp-layout-column[2]/div/tp-layout-section[2]/app-resource-package/div/div[2]/div[1]/div/div[1]/div[1]/div[2]").text_content()
    match = re.search(r"剩余\s+([0-9.]+)\s+TB", credit)
    credit = float(match.group(1))

    # MongoDB Update Data
    mangos_id = {'_id': ObjectId(mongodb_id[m_id])}
    collection.update_one(mangos_id, {"$set": {"Credit": credit}})
    print(f"ven388= {credit} TB")
    m_id +=1

    # hover to menu
    pyautogui.moveTo(1492, 155)

    # delay 0.5s
    time.sleep(0.5)

    # Screenshot
    ImageGrab.grab().save('./早班水位/ven388.png')

    # Waiting for specific text to be appear
    expect(page.locator("xpath=//a[@id='cf_user_info_securitySettings_common']")).to_be_visible(timeout= 0) # "安全设置"

    # Button click logout
    b_nonLock = page.locator("xpath=//span[@id='cf_user_info_logout']").click(force=True)  

    page.close()
    browser.close()
    


