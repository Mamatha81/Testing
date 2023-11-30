from selenium.webdriver.support import expected_conditions as EC

from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


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
    context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys(brand)
    context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys(Keys.ENTER)


@when('she filters by rating "{star}"')
def rating_fltr(context, star):
    stars = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//section[@aria-label='{star} Stars & Up']")))
    stars.click()
    time.sleep(5)


@when('she add top "{n}" products to the cart')
def cart(context, n):
    context.driver.find_elements(By.XPATH,"//div[contains(@class,'s-title-instructions-style')]//a[contains(@class,'a-text-normal')]")
    links = []
    for i in range(1, int(n) + 1):
        link = context.driver.find_element(By.XPATH,f"(//div[contains(@class,'s-title-instructions-style')]//a[contains(@class,'a-text-normal')])[{i}]").get_attribute("href")
        links.append(link)

    prices = []

    for link in links:
        context.driver.get(link)
        cost = context.driver.find_element(By.XPATH, "//div[@id='apex_desktop']//span[@class='a-price-whole']").text
        prices.append(cost)
        time.sleep(3)
        add_to_cart = context.driver.find_element(By.XPATH, "//div[@id='desktop_qualifiedBuyBox']//span[text()='Add to Cart']")
        context.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart)
        add_to_cart = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='desktop_qualifiedBuyBox']//span[text()='Add to Cart']")
                                                                                         ))
        ActionChains(context.driver).move_to_element(add_to_cart).click().perform()

        time.sleep(3)


    prices = [int(x.replace(",", "")) for x in prices]

    context.final_price = sum(prices)


@when('she naviagtes to cart')
def open_cart(context):
    context.driver.refresh()

    cart = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='nav-belt']//a[@id='nav-cart']")))

    cart.click()


@then('she verifies the cart value is same')
def same_value(context):
    cart_amount = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "sc-subtotal-amount-buybox")))
    cart_count = cart_amount.text

    cart = cart_count.replace(",", "")
    cart = float(cart)
    cart_value = int(cart)

    assert cart_value == context.final_price,"Cart values is different"

