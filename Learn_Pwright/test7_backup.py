import re
import time
import math
import pyautogui
import certifi
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

# 安全加速流量
def security_Traffics():
     # Extract 安全 加速流量
    credit = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/main/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/span[2]").text_content()
    # 域名
    domain_Name = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/div/div/div/div[1]/h2/div/div/span").text_content()
    # 域名
    zone_ID = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/div/div/div/div[1]/p/span[3]/span").text_content()
    
    # Filter
    match = re.search(r"([\d.]+)\s*([MGK]B)", credit) 
    security_Traffic = float(match.group(1))
    unit = match.group(2)

    # Convert MB to GB, if have...
    if unit == "MB":
        security_Traffic /= 1024

    return credit, domain_Name, zone_ID, security_Traffic
# 安全加速请求
def security_Requests():
    # Extract 安全 加速请求
    credit = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/main/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[3]/span[2]").text_content()
    match = re.search(r"([\d.]+) 万次", credit)

    # Filter
    security_Request = match.group(1)
    print(f"安全加速请求: {security_Request} 万次")  

    return security_Request

# Chrome Extension
EXTENSION_PATH = "/Users/n02-19/Desktop/playWright/chrome_Extension/lastPass"  # Extension 1
# EXTENSION_PATH2 = "/Users/n02-19/Desktop/playWright/chrome_Extension/SelectorHub"  # Extension 2
USER_DATA_DIR = "/Users/n02-19/PlaywrightProfile"  # User Profile

# mongodb id
m_id = 0

with sync_playwright() as p:    
    browser = p.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,  # Extensions do NOT work in headless mode
        args=[
            f"--disable-extensions-except={EXTENSION_PATH}", # Adding Multiple Extensions, dont add any space after "," , else not working
            f"--load-extension={EXTENSION_PATH}", # Adding Multiple Extensions, dont add any space after "," , else not working
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
    page.goto("https://www.tencentcloud.com/zh/account/login?s_url=https%3A%2F%2Fconsole.tencentcloud.com%2Fedgeone%2Fpackage", wait_until="domcontentloaded")


    for ven_id in range(1,3):

        # Waiting for specific text to be appear
        expect(page.locator("xpath=//div[@class='LoginCommonBox_clg-mod-title__gpSTl']")).to_be_visible(timeout= 0) # "邮箱登录"
        expect(page.locator("xpath=//button[@type='submit']//span[contains(text(),'登录')]")).to_be_visible(timeout= 0) # "登录"

        # click lastpass extension       
        pyautogui.click(x=1395, y=64)

        # Wait for lastpass vault button image to appear
        image_vault = None
        while image_vault is None:
            image_vault = pyautogui.locateOnScreen("./image/vault.png", grayscale = True)

        # lastpass search ven and click 
        time.sleep(1)
        # import aliyun_id from List_zentao.py, ven_id = ven293, ven324, ven319, ven365 ...
        pyautogui.write(tencent_Int_ID[ven_id])
        time.sleep(1)
        pyautogui.click(x=1175, y=179)
        time.sleep(1)

        # Button click, Login
        click_1 = page.locator("xpath=//button[@type='submit']").click(force=True) # "Login"

        # Waiting for specific text to be appear
        expect(page.locator("xpath=//h2[contains(text(),'套餐管理')]")).to_be_visible(timeout= 0) # "套餐管理"

        for edgeone_Link in tencent_EdgeOne:
            page.goto(edgeone_Link, wait_until="domcontentloaded")

            # Waiting for specific text to be appear
            expect(page.locator("xpath=//span[contains(text(),'站点概览')]")).to_be_visible(timeout= 0) # "站点概览"
            expect(page.locator("xpath=//span[contains(text(),'访问数据概览')]")).to_be_visible(timeout= 0) # "访问数据概览"
            expect(page.locator("xpath=//h4[contains(text(),'基础配额')]")).to_be_visible(timeout= 0) # "基础配额"
            expect(page.locator("xpath=//i[@aria-label='refresh']")).to_be_visible(timeout= 0) # "refresh logo"
            
            print("")

            # Extract 安全 加速流量 
            credit = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/main/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/span[2]").text_content()
            # 域名
            domain_Name = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/div/div/div/div[1]/h2/div/div/span").text_content()
            # Zone_ID
            zone_ID = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/div/div/div/div[1]/p/span[3]/span").text_content()

            # Filter
            match = re.search(r"([\d.]+)\s*([MGK]B)", credit) 
            security_Traffic = float(match.group(1))
            unit = match.group(2)

            # Convert MB to GB, if have...
            if unit == "MB":
                security_Traffic /= 1024

            print(tencent_Int_ID[ven_id])
            print(f"域名: {domain_Name}")
            print(zone_ID)
            print(f"安全加速流量: {security_Traffic} GB")  

            # # MongoDB Update Data
            # mangos_id = {'_id': ObjectId(mongodb_id[m_id])}
            # collection.update_one(mangos_id, {"$set": {"Credit": security_Traffic}})
            # m_id += 1

            # Extract 安全 加速请求
            credit = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/main/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[3]/span[2]").text_content()
            match = re.search(r"([\d.]+) 万次", credit)
            
            # Filter
            security_Request = match.group(1)
            print(f"安全加速请求: {security_Request} 万次")  

            # # MongoDB Update Data
            # mangos_id = {'_id': ObjectId(mongodb_id[m_id])}
            # collection.update_one(mangos_id, {"$set": {"Credit": security_Request}})
            # m_id += 1

            # Screenshot
            ImageGrab.grab().save(f'./早班水位/{ven_id}_{edgeone_Link}.png')
            time.sleep(0.5)

        # hover to menu
        pyautogui.moveTo(1544, 162)

        # Waiting for specific text to be appear
        expect(page.locator("xpath=//a[contains(text(),'账号信息')]")).to_be_visible(timeout= 0) # "账号信息"

        # Button click Logout
        b_Logout = page.locator("xpath=//a[contains(text(),'退出')]").click(force=True) # "click 退出"


        time.sleep(11111)












    