import pdb
import time
from selenium.webdriver.common.by import By
from behave import then

from BDDfeatures.steps.loginstep import wait_untill_visible


@then('i click on {like_comnt}')
def likes(context,like_comnt):
    wait_untill_visible(context, "//p[text()='Buzz Newsfeed']")

    time.sleep(3)
    context.driver.find_element(By.XPATH,"//button[text()=' {buzzlike} ']".format(buzzlike=like_comnt)).click()
    time.sleep(3)

@then('delete top 5 actions')
def delete(context):
    time.sleep(5)
    for i in range(1, 6):
        pdb.set_trace()
        context.driver.find_element(By.XPATH,f"//i[@class='oxd-icon bi-trash']{i}]").click()


