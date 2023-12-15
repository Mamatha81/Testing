import pdb

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

@given('login into the mymedgas home page')
def log(context):
    context.driver.get("https://mmg-staging-web.azurewebsites.net/")
    time.sleep(3)


@when('Click a signup Button')
def sign_up(context):
    context.driver.find_element(By.XPATH, "//a[text()='Sign Up']").click()
    time.sleep(2)


@when('fill the signup details')
def sign_dtls(context):
    # // input[ @ name = 'first']
    # // input[ @ name = 'last']
    # // input[ @ name = 'email']........ x paths are same, so we can use below method
    for row in context.table:
        if row["Field name"] == "Email":
            timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
            x = f"robot.mymedgas.uk_{timestamp}@gmail.com"
            context.driver.find_element(By.XPATH,f"//label[text()='{row['Field name']}']/following-sibling::input").send_keys(x)
        elif not row["Field name"] in ("Country Code","Country"):
            context.driver.find_element(By.XPATH,f"//label[text()='{row['Field name']}']/following-sibling::input").send_keys(row['input text'])
        else:
            context.driver.find_element(By.XPATH,f"//label[text()='{row['Field name']}']/parent::div//input[@class='react-select__input']").click()
            time.sleep(3)
            context.driver.find_element(By.XPATH,f"//label[text()='{row['Field name']}']/parent::div//input[@class='react-select__input']").send_keys(row['input text'])
            time.sleep(3)
            context.driver.find_element(By.XPATH,f"//label[text()='{row['Field name']}']/parent::div//input[@class='react-select__input']").send_keys(Keys.ENTER)
            # context.driver.find_element(By.XPATH,f"//label[text()='{row['Field name']}']/parent::div//input[@class='react-select__input']").send_keys(Keys.ENTER)
            time.sleep(3)

    screenshots = context.driver.find_element(By.XPATH, "//div[@class='front']")
    screenshots.screenshot("medgas_signup.png")
    time.sleep(3)

@when('again click the signup button')
def click_signup(context):
    context.driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
    time.sleep(2)

@Then('click ok button')
def ok_btn(context):
    WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Account Pending']")))

    context.driver.find_element(By.XPATH, "//button[text()='Ok']").click()
    time.sleep(3)



# ******************************
@when('click on "{sec_name}"')
def sec(context,sec_name):
    context.driver.find_element(By.XPATH,f"//div[@title='{sec_name}']").click()
    time.sleep(2)

@when('click "{admin_sec}"')
def admin_sec(context,admin_sec):
    context.driver.find_element(By.XPATH,f"//a[@title='{admin_sec}']").click()
    time.sleep(2)

@when(u'In search page search "{fn_ln_email}"')
def searc(context,fn_ln_email):
    context.driver.find_element(By.XPATH,"//label[text()='search']//parent::div//input[@placeholder='Search by First, Last, or Email']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//label[text()='search']//parent::div//input[@placeholder='Search by First, Last, or Email']").send_keys(fn_ln_email)
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//label[text()='search']//parent::div//input[@placeholder='Search by First, Last, or Email']").send_keys(Keys.ENTER)
    time.sleep(2)

@when('click on first element')
def click_elm(context):
    context.driver.find_element(By.XPATH,"(//div[@class='rt-tbody']//div[@class='rt-tr-group'])[1]").click()
    time.sleep(2)

@then('in the new user page fill some details')
def newuser_details(context):
    # ********* facility
    context.driver.find_element(By.XPATH, "//label[text()='Facility']//parent::div//input").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//label[text()='Facility']//parent::div//input").send_keys("demo")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//label[text()='Facility']//parent::div//input").send_keys(Keys.ENTER)
    time.sleep(2)

    # ********** usertype
    context.driver.find_element(By.XPATH, "//label[text()='User Type']//parent::div//input").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//label[text()='User Type']//parent::div//input").send_keys("Contractor")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//label[text()='User Type']//parent::div//input").send_keys(Keys.ENTER)
    time.sleep(2)


@then(u'click "Save & Approve"')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[text()='Save & Approve']").click()
    time.sleep(2)
