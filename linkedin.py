from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r'chromedriver.exe')


login_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
driver.get(login_url)
sleep(1)
email = driver.find_element_by_id('username')
passsword = driver.find_element_by_id('password')

email.send_keys("email")
passsword.send_keys("password")
driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mercado-button--primary", " " ))]').click()
sleep(1)

network_url = "https://www.linkedin.com/mynetwork/"
driver.get(network_url)
sleep(5)


button_elements = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "artdeco-button__text", " " ))]')

count = 1

print(len(button_elements))
while True:
    button_elements = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "artdeco-button__text", " " ))]')
    for i in button_elements:
        print(count)
        if i.text == 'Connect':
            try:
                i.click()
                print("Connection Request send to : ")
            except:
                print("Skipped")
            sleep(2)
        count += 1
    driver.execute_script("window.scrollTo(0, 1080)")
    sleep(5)

driver.close()
