import time
import pyautogui
import pyperclip
from pynput.keyboard import Controller
from List_Zentao import ID, mongodb_id, zen_noc_tuple
from List_Noctool import n_webpage
from bson.objectid import ObjectId  
from function import *

#noctool
def noctool(driver):
    driver.get('http://10.77.1.196/stocks/')
    wait(driver, '/html/body/div[1]/div/main/div/h3') 
    driver.get('http://10.77.1.196/stocks/')
    time.sleep(1)

    try:
        for i in range(zen_noc_tuple):
 
            driver.get(n_webpage[i])
            wait(driver, '/html/body/div[1]/div/main/div/div[3]/div[2]/div/div[1]/h5')       
            time.sleep(1)
            if i == 0:       
                pyautogui.click(x=879, y=346)
                time.sleep(1)

            
            while True:
                if pyautogui.locateOnScreen('./image/current_water.png') is None:
                    pyautogui.click(x=1595, y=812)
                    time.sleep(1)
                    pyautogui.scroll(-100)
                    continue
                else:
                    break

            # Click
            pyautogui.click(x=168, y=671)

            # Previous Credit / Data
            pre_credit = find_element_text(driver, "/html/body/div/div/main/div/div[3]/div[1]/div/div[2]/div/table/tbody/tr[1]/td[2]")

            # Search for Database
            mangos_id = {'_id': ObjectId(mongodb_id[i])}
            documents = find_one(mangos_id)
            credit_value = documents.get('Credit', 'N/A') 
            pyperclip.copy(credit_value)

            # Print out Previous and Actual Data
            print(f"{ID[i]}= Previous: {pre_credit}, Actual: {credit_value} \n") 

            # Write Credit Value
            pyautogui.write(credit_value)
            # pyautogui.hotkey("Command", "V")

            # button click (新增记录)
            pyautogui.hotkey("Enter")
            time.sleep(1)

    except:
        while True:
            time.sleep(1)

def low_water ():
    print("\n【低于安全水位】\n")
    collection = mongodb_atlas()
    documents = collection.find()

    for doc in documents:
        if float(doc.get("Credit", 0)) < float(doc.get("Secure_Credit", 0)):
            print(f"{doc.get('Ven_Machine')} 已低于安全流量 (当前存量：{doc.get('Credit')} {doc.get('Unit')}, 安全存量：{doc.get('Secure_Credit')} {doc.get('Unit')})")
    print("\n\n")

driver = chrome()
driver = next(driver)
noctool(driver)
low_water()