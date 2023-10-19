import time
from selenium import webdriver
def before_scenario(context,scenario):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    time.sleep(3)
def after_scenario(context,scenario):
    context.driver.close()