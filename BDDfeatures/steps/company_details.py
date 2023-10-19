import time
import re
from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
final_details=[]

@given('User is On Google Page')
def google_page(context):
    context.driver.get("https://www.google.com/")
    time.sleep(2)

@when('she Searched For Company "{company_name}"')
def search(context, company_name):
    context.driver.find_element(By.ID, "APjFqb").send_keys(company_name)
    time.sleep(3)
    context.driver.find_element(By.ID, "APjFqb").send_keys(Keys.ENTER)
    time.sleep(3)

@when('she Extract Information')
def extract(context):
    # context.driver.find_element(By.XPATH,"//*[@id='lu_map']").click()
    # names=context.driver.find_element(By.XPATH,"//div[@class='fYOrjf iB08Xb kp-hc']//*[contains(text(),'Actualize')]").text
    company_data=[]

    try:
        names = context.driver.find_element(By.XPATH,"//div[@class='fYOrjf iB08Xb kp-hc']//h2[contains(@class,'qrShPb')]").text
    except:
        names=''
    try:
        rating = context.driver.find_element(By.XPATH,"//div[@class='fYOrjf iB08Xb kp-hc']//span[@class='Aq14fc']").text
    except:
        rating=''
    try:
        Reviews = context.driver.find_element(By.XPATH, "//div[@class='fYOrjf iB08Xb kp-hc']//span[@class='hqzQac']").text
    except:
        Reviews=''
    try:
        address = context.driver.find_element(By.XPATH, "//span[@class='LrzXr']").text
    except:
        address=''
    try:
        phone = context.driver.find_element(By.XPATH, "//span[@class='LrzXr zdqRlf kno-fv']").text
    except:
        phone=''
    try:
        context.driver.find_element(By.XPATH, "//*[@id='lu_map']").click()
        time.sleep(3)
        geo_loc = context.driver.current_url
        # s = "https://www.google.com/maps/place/Actualize+Consulting+Engineers+India+Pvt+Ltd.,+Bengaluru/@12.993411,77.6992034,15z/data=!4m6!3m5!1s0x3bae3d208a298d63:0x999e4c2874ab22ce!8m2!3d12.993411!4d77.6992034!16s%2Fg%2F1ptyqhw9m?entry=ttu"
        s = geo_loc
        lattitude, longitude = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', s).groups()


    except:
        lattitude = longitude= ''

    company_data.extend([names,address,phone,rating,Reviews,lattitude,longitude])
    final_details.append(company_data)
    # print(company_data)

@then('Successfully Make Csv file of all data')
def csv_data(context):
    import csv
    with open('out.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([['names','address','phone','rating','Reviews','lattitude','longitude']])
        writer.writerows(final_details)




