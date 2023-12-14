from datetime import datetime

from selenium.webdriver import Keys
from behave import *
from selenium.webdriver.common.by import By
import time


@given('mammu login into the my medgas home page')
def login_mmg(context):
    context.driver.get("https://mmg-staging-web.azurewebsites.net/")
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(5)


@when('she have to enter email "{mail}" and password "{pwd}"')
def email_pwd(context, mail, pwd):
    context.driver.switch_to.window(context.driver.window_handles[1])
    context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(mail)
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(pwd)
    time.sleep(2)


@when('she clicks on sign in button')
def signin(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    context.driver.switch_to.window(context.driver.window_handles[0])
    context.driver.find_element(By.XPATH, "//div[@class='list-group']//a[@title='Home']").is_displayed()
    screenshots = context.driver.find_element(By.XPATH, "//div[@class='list-group']//a[@title='Home']")
    screenshots.screenshot("pims.png")
    time.sleep(3)


@when('she click on the "{section}"')
def home_sec(context, section):
    context.driver.find_element(By.XPATH, f"//div[@class='list-group']//a[@title='{section}']").click()
    time.sleep(3)


@when('she click on the add facility')
def add_facility(context):
    context.driver.find_element(By.XPATH, "//button[text()='Add Facility']").click()
    time.sleep(3)


@when('she fill the the some needed details')
def fill_details(context):
    now = datetime.now()
    name = "iris_4" + now.strftime("_%d_%m_%Y_%H_%M_%S")
    name_input = context.driver.find_element(By.XPATH,"//input[@name='fac-name']")
    name_input.send_keys(name)
    # context.driver.find_element(By.XPATH, "//input[@name='fac-name']").send_keys("iris_4")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//h4[text()='Add Facility']/ancestor::div[@class='modal-content']//label["
                                          "text()='standard']/parent::div//*[contains(@class, "
                                          "'react-select__control')]//input").click()
    context.driver.find_element(By.XPATH,
                                "//h4[text()='Add Facility']/ancestor::div[@class='modal-content']//label["
                                "text()='standard']/parent::div//*[contains(@class, "
                                "'react-select__control')]//input").send_keys("HTM_MY")
    context.driver.find_element(By.XPATH,
                                "//h4[text()='Add Facility']/ancestor::div[@class='modal-content']//label["
                                "text()='standard']/parent::div//*[contains(@class, "
                                "'react-select__control')]//input").send_keys(Keys.ENTER)

    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@name='address']").send_keys("address_4")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@name='city']").send_keys("city_4")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@name='postal-code']").send_keys("1234")
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//textarea[@name='comments']").send_keys("add facility in my med gas")
    time.sleep(5)


@when('she click on the save button')
def save_btn(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)


@then(u'she search "{facility_name}" in facility searchbar')
def search(context, facility_name):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search for facility...']").send_keys(facility_name)
    time.sleep(5)


@when(u'she have to click on the assets')
def click_assets(context):
    context.driver.find_element(By.XPATH, f"//div[@class='list-group']//a[@title='Assets']").click()
    time.sleep(3)


@when(u'In the assets page in facility search bar search for "iris_3')
def search_facility(context):
    context.driver.find_element(By.XPATH,"(//div[@class='banner purple soso']//input[@class='react-select__input'])[2]").click()
    time.sleep(5)
    context.driver.find_element(By.XPATH,"(//div[@class='banner purple soso']//input[@class='react-select__input'])[2]").send_keys(Keys.ENTER)
    time.sleep(2)
    # // div[contains( @class ,'beacon-select has-success')] // div[contains( @ class, 'react-select__value')]


@when(u'she have to click on the new asset')
def new_asset(context):
    context.driver.find_element(By.XPATH, "//button[text()='new Asset']").click()
    time.sleep(2)


@when(u'In that pagesearch section search the "Gem10"')
def search_brand(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search By Name, Part #, etc.']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search By Name, Part #, etc.']").send_keys("gem10")
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search By Name, Part #, etc.']").send_keys(Keys.ENTER)
    time.sleep(2)
    context.driver.find_element(By.XPATH,
                                "(//div[contains(@class,'beacon-list')]//li[contains(@class,'list-group')])[8]").click()
    time.sleep(2)


@when(u'add new asset section')
def add_asset(context):
    # ********* Enter nickname
    context.driver.find_element(By.XPATH, "//input[@name='nickname']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@name='nickname']").send_keys("1st item added new asset")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@name='nickname']").send_keys(Keys.ENTER)
    time.sleep(2)
    # context.driver.find_element(By.XPATH, "//input[@name='quantity']").click()
    # time.sleep(2)
    # context.driver.find_element(By.XPATH, "//input[@name='quantity']").send_keys("8")
    # time.sleep(2)
    # context.driver.find_element(By.XPATH, "//input[@name='quantity']").send_keys(Keys.ENTER)
    time.sleep(2)


@Then('she have to click Save button')
def save(context):
    context.driver.find_element(By.XPATH, "//button[text()='Save']").click()
    time.sleep(5)



