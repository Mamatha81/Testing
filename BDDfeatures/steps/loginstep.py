import pdb
import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def after_step(context,step):
    print()

def before_scenario(context):
    print("inside - before scenario")

def after_scenario(context):
    print("Inside - after scenario ")

@given('i Launch the chrome browser')
def opn_brw(context):
    # context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(executable_path=r'C:\Users\91889\.wdm\drivers\chromedriver\win32\114.0.5735.90')
    context.driver.maximize_window()

@when('i open hrm home page')
def hrm_hp(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def wait_untill_visible(context,locator):
    wait = WebDriverWait(context.driver, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator)))

@when('enter username "{username}" and password "{pwd}"')
def un_pw(context,username,pwd):
    wait_untill_visible(context,"//label[text()='Username']")
    context.driver.find_element(By.NAME,"username").send_keys(username)
    context.driver.find_element(By.NAME,"password").send_keys(pwd)

@then('click on login button')
def login(context):
    context.driver.find_element(By.TAG_NAME,"button").click()
    wait_untill_visible(context, "//div[@class='oxd-sidepanel-header']")
    time.sleep(5)

# @then('login to the dash board')
# # @when('login to the dash board')cl
# def dash_brd(context):
#     text=context.driver.find_element(By.XPATH,"//p[text()='Time at Work']").text()
#     assert text=="Time at Work"
#
# @then('close browser')
# def cls_brw(context):
#     context.driver.close()


