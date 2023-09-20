import time

from behave import *
from selenium.webdriver.common.by import By

# @when('login to the dash board')
# def dashboard(context):
#         context.driver.find_element(By.XPATH, "//*[@class='oxd-main-menu']//span[text()='Dashboard']")
#         context.time.sleep(3)

@when('scroll the till find element')
def scroll(context):
        hgt=context.driver.execute_script("return document.body.scrollHeight")
        print(hgt)
        time.sleep(3)
        context.driver.execute_script ("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)

@when('take a screen shot')
def screenshot(context):
        context.driver.get_screenshot_as_file("piechart.png")
        time.sleep(5)
@then('login to the PIM')
def pim(context):
        context.driver.find_element(By.XPATH, "//*[@class='oxd-main-menu']//span[text()='PIM']").click()
        time.sleep(3)
@then('click the add button')
def add_btn(context):
        context.driver.find_element(By.XPATH,"//button[text()=' Add ']").click()
        time.sleep(2)
# @then('take the screen shot')
# def pim_screenshot(context):
#         context.driver.get_screenshot_as_file("add_emp.png")
#         time.sleep(3)

@then('take the screen shot')
def pim_screenshot(context):
        pim_ss=context.driver.find_element(By.XPATH,"//div[@class='oxd-form-row']")
        pim_ss.screenshot("pims.png")
        time.sleep(3)

