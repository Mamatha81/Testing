from selenium.webdriver.common.by import By
from behave import *

@when('open flags home page')
def flgs_home(context):
    context.driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

@when('scroll element till Bahamas')
def sroll(context):
    flag=context.driver.find_element(By.XPATH,"//td[text()='Bahamas']")
    context.driver.execute_script(0,)


@then('take a screen shot')
def screenshot(context):
    pass