from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
    for row in context.table:
        if not row["Field name"] in ("Country Code","Country"):
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
