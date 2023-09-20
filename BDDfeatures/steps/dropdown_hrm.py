import pdb

from behave import *
from selenium.webdriver.common.by import By
import time
@when('click on the section {section}')
@then('click on the section {section}')
def nav_sect(context,section):
    context.driver.find_element(By.XPATH, "//*[@class='oxd-main-menu']//span[text()='{enter}']".format(enter=section)).click()
    time.sleep(3)

@when('scroll till find the element')
def scroll(context):
    name=context.driver.find_element(By.XPATH,"(//div[text()='Charlie  Carter'])[1]")
    # context.driver.find_element(By.XPATH, "(//div[text()='Charlie  Carter'])[1]")
    context.driver.execute_script ("arguments[0].scrollIntoView(true);", name)
    time.sleep(5)

@when('take a view screen shot')
def view_ss(context):
    carter_ss=context.driver.find_element(By.XPATH,"(//div[@class='oxd-table-card'])[6]")
    carter_ss.screenshot("view_sshot.png")
    time.sleep(1)
    context.driver.get_screenshot_as_file("hrm.png")
    time.sleep(3)

@then('click the fourth element on view')
def view(context):
    # pdb.set_trace()
    context.driver.find_element(By.XPATH,"(//button[text()=' View '])[5]").click()
    time.sleep(10)

@then('take the inside view screen shot')
def inview_ss(context):
    # time_sheet=context.driver.find_element(By.XPATH,"//h6[text()='Timesheet for Charlie Carter']")
    # time_sheet.screenshot("charlie_timesheet.png")
    context.driver.get_screenshot_as_file("timesheet.png")
    time.sleep(3)

@then('write the comment')
def comment(context):
    context.driver.find_element(By.XPATH,"//textarea[@placeholder='Type here ...']").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//textarea[@placeholder='Type here ...']").send_keys("I want go my home town, I need 2 days leave")
    time.sleep(5)

@then('dropdown the job title')
def drp_dwn(context):
    context.driver.find_element(By.XPATH,"//label[text()='Job Title']//parent::div//parent::div//div[text()='-- Select --']").click()
    time.sleep(3)
    vals=context.driver.find_element(By.XPATH,"//*[@role='listbox']").get_attribute("innerHTML")
    print(vals)
    time.sleep(3)

@then('search the section names and send the keys')
def search_secname(context):
    context.driver.find_element(By.XPATH,"//input[@placeholder='Search']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("My Info")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//span[text()='My Info']").click()
    time.sleep(2)

