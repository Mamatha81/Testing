import pdb
from selenium.webdriver.support import expected_conditions as EC

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait


@given('mamatha Launched chrome browser')
def chrome(context):
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    time.sleep(5)


@when('she opens amazon homes page')
def amazon_hp(context):
    context.driver.get("https://www.amazon.in/")
    time.sleep(5)
    context.driver.find_element(By.XPATH, "//a[text()='Mobiles']").click()
    time.sleep(3)


@when('she search for "{brand}" mobile')
def mobile(context, brand):
    context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys(brand)
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys(Keys.ENTER)
    time.sleep(10)


@when('she filters by rating "{star}"')
def rating_fltr(context, star):
    context.driver.find_element(By.XPATH, f"//section[@aria-label='{star} Stars & Up']").click()
    time.sleep(5)


@when('she add top "{n}" products to the cart')
def cart(context, n):
    context.driver.find_elements(By.XPATH,"//div[contains(@class,'s-title-instructions-style')]//a[contains(@class,'a-text-normal')]")
    links = []
    for i in range(1, int(n) + 1):
        link = context.driver.find_element(By.XPATH,f"(//div[contains(@class,'s-title-instructions-style')]//a[contains(@class,'a-text-normal')])[{i}]").get_attribute("href")
        links.append(link)
        time.sleep(3)
        print(links)

    prices = []

    for link in links:
        context.driver.get(link)
        cost = context.driver.find_element(By.XPATH, "//div[@id='apex_desktop']//span[@class='a-price-whole']").text
        prices.append(cost)
        time.sleep(3)
        context.driver.find_element(By.ID, "add-to-cart-button").click()
        time.sleep(15)
        # element = WebDriverWait(context.driver, 20)
        # element.until(EC.element_to_be_clickable((By.XPATH,"add-to-cart-button"))).click()
    print(prices)
    for i in prices:
        print(i)
    count = [int(x.replace(",", "")) for x in prices]
    print(count)
    context.final_price = sum(count)
    time.sleep(3)


@then('she verifies the cart value is same')
def same_value(context):
    context.driver.find_element(By.ID, "attach-close_sideSheet-link").click()
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//div[@id='nav-belt']//a[@id='nav-cart']").click()
    time.sleep(10)
    cart_count = context.driver.find_element(By.ID, "sc-subtotal-amount-buybox").text
    print(cart_count)

    cart = cart_count.replace(",", "")
    bal = float(cart)
    total = int(bal)
    print(total)

    time.sleep(5)
    if total == context.final_price:
        print("yes")
    else:
        print("no")
