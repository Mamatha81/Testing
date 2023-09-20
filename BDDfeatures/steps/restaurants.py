import pdb
import time
from behave import *
from selenium.webdriver.common.by import By

@when('i have open restaurants on google page')
def hp_restr(context):
    context.driver.get("https://www.google.com/maps/search/restaurants/@12.9388475,77.7108679,15z?entry=ttu")

@then('I save the nearby restaurants')
def near_reasr(context):
    results=context.driver.find_elements(By.XPATH,"//div[contains(@class,'Nv2PK')]")
    for i in range(1,len(results)+1):
        # pdb.set_trace()
        try:
            name = context.driver.find_element(By.XPATH,f"(//div[contains(@class,'Nv2PK')])[{i}]//div[@class='NrDZNb']").text
            print(name)
        except:
            print("***no name***")
            time.sleep(3)

        try:
            rating = context.driver.find_element(By.XPATH,f"(//div[contains(@class,'Nv2PK')])[{i}]//span[@class='ZkP5Je']").text
            print(rating)
        except:
            print("***no rating***")
            time.sleep(3)
        try:
            address = context.driver.find_element(By.XPATH,f"(//div[contains(@class,'Nv2PK')])[{i}]//div[@class='W4Efsd'][2]//div[@class='W4Efsd'][1]").text
            print(address)
        except:
            print("***no address***")

        try:
            timings = context.driver.find_element(By.XPATH,f"(//div[contains(@class,'Nv2PK')])[{i}]//div[@class='W4Efsd'][2]//div[@class='W4Efsd'][3]").text
            print(timings)
        except:
            print("***no timings***")
            time.sleep(3)
            # pdb.set_trace()

        try:
            ss_rstr=context.driver.find_element(By.XPATH,f"(//div[contains(@class,'Nv2PK')])[{i}]//div[contains(@class,'xwpmRb')]")
            ss_rstr.screenshot(f"food_{i}.png")
            time.sleep(2)
        except:
            print("***no food images***")

        context.driver.find_element(By.XPATH, f"(//div[contains(@class,'Nv2PK')])[{i}]").click()
        time.sleep(2)

        # scroll = context.driver.find_element(By.XPATH,f"(//div[contains(@class,'Nv2PK')])[{i}](//div[@class='rogA2c '])[2]")
        #
        # context.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        # time.sleep(2)

        # try:
        #     phn_no=context.driver.find_element(By.XPATH,f"(//div[contains(@class,'Nv2PK')])[{i}](//div[@class='rogA2c '])[2]").text
        #     print(phn_no)
        #     time.sleep(2)
        # except:
        #     print("*** no phn_no")











        


