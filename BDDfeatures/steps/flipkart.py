from selenium.webdriver.support import expected_conditions as EC

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@given('Mamatha opens flipkart home')
def flipkart_hp(context):
    context.driver.get("https://www.flipkart.com/")
    time.sleep(3)
    context.driver.find_element(By.XPATH,"//div[@class='JFPqaw']//span[@role='button']").click()
    time.sleep(5)
    search=context.driver.find_element(By.XPATH, "//div[@class='_2SmNnR']")
    ActionChains(context.driver).move_to_element(search).click().perform()
    time.sleep(3)
    # context.driver.find_element(By.XPATH, "//div[@class='_2SmNnR']").send_keys("dell laptop")
    # time.sleep(3)
    # context.driver.find_element(By.XPATH, "//div[@class='_2SmNnR']").send_keys(Keys.ENTER)


@when('she search "{brand}"')
def brand_name(context, brand):
    context.driver.find_element(By.XPATH, "//input[@class='Pke_EE']").send_keys(brand)
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@class='Pke_EE']").send_keys(Keys.ENTER)
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//a[@title='Laptops']").click()
    time.sleep(2)
    mini = context.driver.find_element(By.XPATH,
                                       "//div[@class='_1YAKP4']//select[@class='_2YxCDZ']//option[@value='20000']")
    mini.click()
    core = context.driver.find_element(By.XPATH, "//section[@class='_167Mu3 _2hbLCH']//div[@title='Core i5']")
    core.click()


@when('she filters by stars "{star}"')
def rating(context,star):
    sel_rat = context.driver.find_element(By.XPATH,
                                          f"//div[@class='_1YokD2 _3Mn1Gg col-2-12']//section[@class='_167Mu3 _2hbLCH']//div[@title='{star}★ & above']")
    context.driver.execute_script("arguments[0].scrollIntoView();", sel_rat)
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                  "//div[@class='_1YokD2 _3Mn1Gg col-2-12']//section[@class='_167Mu3 _2hbLCH']//div[@title='4★ & above']")
                                                                                 ))
    time.sleep(3)


@when('she add top "{n}" products')
def add_items(context, n):
    context.driver.find_element(By.XPATH, "//div[contains(text(),'DELL ')]")
    time.sleep(3)
    flp_links = []
    for i in range(1, int(n) + 1):
        link = context.driver.find_element(By.XPATH, f"(//div[@class='_1YokD2 _3Mn1Gg']//div[contains(text(),'DELL ')]/ancestor::a)[{i}]").get_attribute("href")
        flp_links.append(link)
        print(link)
        time.sleep(3)


    prices = []

    for link in flp_links:
        context.driver.get(link)
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='_30jeq3 _16Jk6d']")
                                             ))
        cost = context.driver.find_element(By.XPATH, "//div[@class='_30jeq3 _16Jk6d']").text
        prices.append(cost)
        time.sleep(3)
        context.driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
        time.sleep(3)

    prices = [int(x.replace(",", "").replace("₹", "")) for x in prices]

    context.final_price = sum(prices)


@when('she click on cart')
def nav(context):
    context.driver.refresh()

    cart = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='_3SkBxJ']")))

    cart.click()

@then('she calculate the cart value')
def subtotal(context):
    cart_amount = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='_35mLK5']//div[@class='_1dqRvU']")))
    cart_count = cart_amount.text

    cart = cart_count.replace(",", "").replace("₹", "")
    cart = float(cart)
    cart_value = int(cart)

    assert cart_value == context.final_price, "Cart values is different"
    print(cart_value)

