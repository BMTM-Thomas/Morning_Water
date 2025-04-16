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
def filter_Security_Traffics(credit_Traffic):
    # Filter
    match = re.search(r"([\d.]+)\s*([MGK]B)", credit_Traffic) 
    
    if match:
        security_Traffic = float(match.group(1))
        st_unit = match.group(2)

        # Convert MB to GB, if have...
        if st_unit == "MB":
            security_Traffic /= 1024
        elif st_unit == "KB":
            security_Traffic /= (1024 * 1024)

        # Convert to 3 decimal place, without rounding
        security_Traffic  = math.floor(security_Traffic * 1000) / 1000

        return security_Traffic
    else:
        return None
    
# 安全加速请求
def filter_Security_Requests(credit_Request):
    # Filter
    match = re.search(r"([\d.]+)\s*([万次|次]+)", credit_Request)

    if match:
        security_Request = match.group(1)
        sr_unit = match.group(2) # (万次 or 次)

        return security_Request, sr_unit
    else:
        return None, None

# Chrome Extension
EXTENSION_PATH = "/Users/n02-19/Desktop/playWright/chrome_Extension/lastPass"  # Extension 1
EXTENSION_PATH2 = "/Users/n02-19/Desktop/playWright/chrome_Extension/SelectorHub"  # Extension 2
USER_DATA_DIR = "/Users/n02-19/PlaywrightProfile"  # User Profile

# Launch MongoDB Atlas
collection = mongodb_atlas()

# mongodb id
m_id = 0

# use to loop tencent_edgeOne Tuple
x = 0

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
    
    for ven_id in range(1,3):

        # Launch a new browser page
        page = browser.pages[0] 
        time.sleep(1)
        page.goto(tencent_edgeOne_ID[x], wait_until="domcontentloaded", timeout=0)

        # ven414
        if ven_id == 1: 
            # if text_element == "CAM用户登录", do something...
            if page.locator(f"xpath=//div[@class='LoginCommonBox_clg-mod-title__gpSTl']").text_content() == "CAM用户登录":

                # Waiting for specific text to be appear
                expect(page.locator("xpath=//div[@class='LoginCommonBox_clg-mod-title__gpSTl']")).to_be_visible(timeout= 0) # "CAM用户登录"
                expect(page.locator("xpath=//button[@type='submit']")).to_be_visible(timeout= 0) # "登录"

                # Button click, "主账号登录"
                click_1 = page.locator("xpath=//a[contains(text(),'主账号登录')]").click(force=True) # "主账号登录"
                
                # Waiting for specific text to be appear
                expect(page.locator("xpath=//div[@class='LoginCommonBox_clg-mod-title__gpSTl']")).to_be_visible(timeout= 0) # "邮箱登录"
                expect(page.locator("xpath=//button[@type='submit']//span[contains(text(),'登录')]")).to_be_visible(timeout= 0) # "登录"
            else:
                # Waiting for specific text to be appear
                expect(page.locator("xpath=//div[@class='LoginCommonBox_clg-mod-title__gpSTl']")).to_be_visible(timeout= 0) # "邮箱登录"
                expect(page.locator("xpath=//button[@type='submit']//span[contains(text(),'登录')]")).to_be_visible(timeout= 0) # "登录"
        # ven469
        else: 
            # else Waiting for specific text to be appear
            expect(page.locator("xpath=//div[@class='LoginCommonBox_clg-mod-title__gpSTl']")).to_be_visible(timeout= 0) # "CAM用户登录"
            expect(page.locator("xpath=//button[@type='submit']")).to_be_visible(timeout= 0) # "登录"

        # click lastpass extension       
        pyautogui.click(x=1359, y=62)

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
        expect(page.locator("xpath=//h2[contains(text(),'站点列表')]")).to_be_visible(timeout= 0) # "站点列表"

        for index, edgeOne_URL in enumerate(tencent_EdgeOne[x]):
            
            # navigate to a link
            page.goto(edgeOne_URL, wait_until="domcontentloaded")

            # Waiting for specific text to be appear
            expect(page.locator("xpath=//span[contains(text(),'站点概览')]")).to_be_visible(timeout= 0) # "站点概览"
            expect(page.locator("xpath=//span[contains(text(),'访问数据概览')]")).to_be_visible(timeout= 0) # "访问数据概览"
            expect(page.locator("xpath=//h4[contains(text(),'基础配额')]")).to_be_visible(timeout= 0) # "基础配额"
            expect(page.locator("xpath=//i[@aria-label='refresh']")).to_be_visible(timeout= 0) # "refresh logo"
            
            print("")
            
            # Extract 安全 加速流量
            credit_Traffic = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/main/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/span[2]").text_content()
            # Extract 安全 加速请求
            credit_Request = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/main/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[3]/span[2]").text_content()
            # 域名
            domain_Name = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/div/div/div/div[1]/h2/div/div/span").text_content()
            # Zone_ID
            zone_ID = page.locator(f"xpath=/html/body/div[2]/div[2]/div[2]/div/section/section/section/section/main/div/div/div/div/div[1]/p/span[3]/span").text_content()

            # Filter 安全 加速流量
            security_Traffic = filter_Security_Traffics(credit_Traffic)
            # Filter 安全 加速请求
            security_Request, sr_unit = filter_Security_Requests(credit_Request)

            print(tencent_Int_ID[ven_id])
            print(f"域名: {domain_Name}")
            print(zone_ID)
            print(f"安全加速流量: {security_Traffic} GB")  
            print(f"安全加速请求: {security_Request} {sr_unit}")  

            # Screenshot
            ImageGrab.grab().save(f'./早班水位/{tencent_Int_ID[ven_id]}_{index+1}.png')
            time.sleep(0.5)

            # MongoDB Update Data
            mangos_id_1 = {'_id': ObjectId(mongodb_id[m_id])}
            collection.update_one(mangos_id_1, {"$set": {"Credit": security_Traffic}})
            m_id + 1
            mangos_id_2 = {'_id': ObjectId(mongodb_id[m_id])}
            collection.update_one(mangos_id_2, {"$set": {"Credit": security_Request}})
            m_id + 1

        # use to loop tencent_edgeOne Tuple
        x+=1

        # hover to menu
        pyautogui.moveTo(1544, 162)

        # Waiting for specific text to be appear
        expect(page.locator("xpath=//a[contains(text(),'账号信息')]")).to_be_visible(timeout= 0) # "账号信息"

        # Button click Logout
        b_Logout = page.locator("xpath=//a[contains(text(),'退出')]").click(force=True) # "click 退出"

        time.sleep(1)











    