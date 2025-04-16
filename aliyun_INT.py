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
    page.goto("https://account.alibabacloud.com/login/login.htm?oauth_callback=https%3A%2F%2Fusercenter2-intl.aliyun.com%2Fri%2Fsummary%3FcommodityCode%3D", wait_until="domcontentloaded")
    
    time.sleep(1)

    for ven_id in aliyun_ID:

        # switch to iframe
        iframe = page.frame_locator("#alibaba-login-box")
        # Waiting for specific text to be appear
        expect(iframe.locator("#login-title")).to_contain_text("登录阿里云账号", timeout=30000) # "登录阿里云账号"

        # get title
        # print(page.title())

        # click lastpass extension       
        pyautogui.click(x=1359, y=62)

        # Wait for lastpass vault button image to appear
        image_vault = None
        while image_vault is None:
            image_vault = pyautogui.locateOnScreen("./image/vault.png", grayscale = True)

        # lastpass search ven and click 
        time.sleep(1)
        # import aliyun_id from List_zentao.py, ven_id = ven293, ven324, ven319, ven365 ...
        pyautogui.write(ven_id)
        time.sleep(1)
        pyautogui.click(x=1175, y=179)
        time.sleep(1)

        # click 登陆
        # switch to iframe
        iframe.locator('xpath=//*[@id="fm-login-submit"]').click()
        
        # Waiting for specific text to be appear
        expect(page.locator("xpath=//span[@class='title']")).to_be_visible(timeout= 30000) # "资源实例管理"
        expect(page.locator("xpath=//div[contains(text(),'实例名称')]")).to_be_visible(timeout= 30000) # "实例名称"

        # delay 0.5seconds, this function similar to time.sleep()
        page.wait_for_timeout(1000) 

        # Extract Credit 
        try:
            credit_CN = float(0.0)
            credit_AP1 = float(0.0)
            credit_AP2 = float(0.0)
    
            # Count 资源包 total number of tr
            total_rows = len(page.locator("//tbody/tr").all()) 

            # Using total rows to loop
            for item in range(1, total_rows+1):
                
                # Check Area
                area = page.locator(f"xpath=//tbody/tr[{item}]/td[7]/div[1]").text_content()
                # Extract Credit
                credit_Extract = page.locator(f"xpath=//tbody/tr[{item}]/td[11]/div[1]").text_content()
                
                # if is GB, then divide to 1024
                if "GB" in credit_Extract:
                    credit_Extract = float(credit_Extract.replace(" GB", "").strip()) / 1024  # Convert GB to TB
                # if is TB, then remain
                elif "TB" in credit_Extract:
                    credit_Extract = float(credit_Extract.replace(" TB", "").strip())
                else:
                    pass
                
                # if is CN or AP1 or AP2, then do something....     
                match area:
                    case "CN":
                        # Subtotal
                        credit_CN += float(credit_Extract)
                        # Convert to 3 decimal places, without Rounding
                        credit_CN = math.floor(credit_CN * 1000) / 1000
                    case "AP1":
                        # Subtotal
                        credit_AP1 += float(credit_Extract)
                        # Convert to 3 decimal places, without Rounding
                        credit_AP1 = math.floor(credit_AP1 * 1000) / 1000
                    case "AP2":
                        # Subtotal
                        credit_AP2 += float(credit_Extract)
                        # Convert to 3 decimal places, without Rounding
                        credit_AP2 = math.floor(credit_AP2 * 1000) / 1000
            
            # Group into tuple
            credits = (credit_CN, credit_AP1, credit_AP2)
            print(f"【{ven_id}】")
            print(f"CN= {credit_CN} TB, AP1= {credit_AP1} TB, AP2= {credit_AP2} TB")

            # MongoDB Update Data
            for index, credit in enumerate(credits):
                if credit != 0.0:
                    # MongoDB Update Data
                    mangos_id = {'_id': ObjectId(mongodb_id[m_id])}
                    collection.update_one(mangos_id, {"$set": {"Credit": credit}})
                    m_id += 1
                else: 
                    pass

        except Exception as e:  # Catch any error
            print(f"Error occurred: {e}")
            pass
        
        # wait for specific text to be appear, then only hover to menu
        expect(page.locator("xpath=//button[contains(text(),'简体')]")).to_be_visible(timeout= 30000) # "简体"
        expect(page.locator("xpath=/html/body/div[1]/div/div[1]/nav/div[10]/span/div/div/div/div[2]")).to_be_visible(timeout= 30000)

        # delay 0.5seconds
        page.wait_for_timeout(1000)

        # hover to menu
        pyautogui.moveTo(1525, 158)

        # Waiting for specific text to be appear
        expect(page.locator("xpath=//span[contains(text(),'安全设置')]")).to_be_visible(timeout = 30000) # "安全设置"

        # delay 0.5seconds
        page.wait_for_timeout(500)

        # Screenshot
        ImageGrab.grab().save(f'./早班水位/{ven_id}.png')
        
        # delay 0.5seconds
        page.wait_for_timeout(500)

        # Button click Logout
        b_Logout = page.locator("xpath=//a[contains(text(),'退出登录')]")  # "退出登录"
        b_Logout.click(force=True)

        page.wait_for_timeout(1000)
    
    page.close()
    browser.close()
    


