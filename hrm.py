from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import select
import time
class test_1():
    def org_hrm(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.TAG_NAME,"button").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@class='oxd-main-menu']//span[text()='Admin']").click()
        time.sleep(3)
        hgt=driver.execute_script("return document.body.scrollHeight")
        print(hgt)
        driver.execute_script ("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@class='oxd-main-menu']//span[text()='PIM']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[contains(text(),'Job Title')]//ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//i").click()
        time.sleep(5)
        x=driver.find_element(By.XPATH,"//div[@role='listbox']").get_attribute('innerHTML')
        print(x)
        driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("mamatha")
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("praveen")
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)


o=test_1()
o.org_hrm()

