from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://courses.letskodeit.com/practice')

def checkboxfunc(locator):
    ele = driver.find_element(By.ID,locator )
    if ele.is_selected():
        print(f'{locator} is already selected')
    else:
        print(f'{locator} is selected')
        ele.click()
    time.sleep(2)

checkboxfunc(locator='bmwcheck')
checkboxfunc(locator='benzcheck')
checkboxfunc(locator='hondacheck')

textbox=driver.find_element(By.ID,"displayed-text")
if textbox.is_displayed():
    print("entering the keys")
    textbox.send_keys("python")
    # driver.find_element(By.ID,"hide-textbox").click()
else:
    print("textbox is not disaplayed ")
    driver.find_element(By.ID,"show-textbox").click()
    textbox.send_keys("python")
time.sleep(3)


class praveen_task:
     def openbrowser(self,url):
         self.driver=webdriver.Chrome(ChromeDriverManager().install())
         self.driver.get(url)
#         return self.driver
#     def task5(self):
#         driver=self.openbrowser(url="https://online.actitime.com/mkona/login.do")
#         driver.find_element(By.ID, "username").send_keys("konamamathan@gmail.com")
#         driver.find_element(By.NAME, "pwd").send_keys("P@praveenlove6")
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://courses.letskodeit.com/practice')
#



     def checkboxfunc(locator):
            ele = driver.find_element(By.ID,locator )
#     if ele.is_selected():
#         print(f'{locator} is already selected')
#         R1=
#         R1= driver.find_elements(By.TAG_NAME,"a")
# for R1 in x:
#     print(x.get_attribute('arial-label')

      #  driver=self.openbrowser(url="https://www.google.com/search?q=convergytics")
# "//a[@aria-label='tag' and @href='/profile.php?id=1792']")))
