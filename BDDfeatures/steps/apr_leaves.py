import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from behave import then
import string

# @then('click on the Leave')
# def cl_lvs(context):
#     context.driver.find_element(By.XPATH, "//*[@class='oxd-main-menu']//span[text()='Leave']").click()

@then('give the {action}')
def apr_lvs(context,action):
    time.sleep(5)
    if action == 'Approve':
        list_ = [i for i in range(1, 10) if i % 2 == 0]
    else:
        list_ = [i for i in range(1, 10) if i % 2 != 0]
    for i in list_:
        context.driver.find_element(By.XPATH, "(//button[text()=' {action} '])[{i}]".format(action=action, i=i)).click()

        context.driver.find_element(By.XPATH,"//button[text()=' {action} ']".format(action=action)).click()

