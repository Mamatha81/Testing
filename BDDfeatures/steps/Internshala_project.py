from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

@given('I have to Launch chrome browser')
def launch_chrome(context):
    # option = webdriver.ChromeOptions()
    # option.add_argument("start-maximized")

    # context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
    # context.driver.maximize_window()
    # context.driver = webdriver.Chrome('D:/Basics/venv/WebDriverManager')
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    time.sleep(5)

@when('I have to open facegenie home page')
def facegenie_home(context):
    context.driver.get("https://facegenie-ams-school.web.app/")
    time.sleep(2)

@when('I have to enter mail "{username}" and pass word "{pwd}"')
def mail_pwd(context,username,pwd):
    context.driver.find_element(By.ID,"email").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(pwd)
    time.sleep(3)

@when('I have to click a login button')
def login(context):
    context.driver.find_element(By.XPATH,"//button[text()='Log In']").click()
    time.sleep(15)
    if not context.driver.find_element(By.XPATH,"//nav[@class='MuiList-root MuiList-padding css-1ontqvh']//span[text()='Log Out']").is_displayed():
        raise Exception("Log In has failed")


@then('I have to click a logout button')
def logout(context):
    context.driver.find_element(By.XPATH,"//span[text()='Log Out']").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//button[text()='Ok']").click()
    if not context.driver.find_element(By.XPATH,"//button[text()='Log In']").is_displayed():
        raise Exception("Log out has failed")

