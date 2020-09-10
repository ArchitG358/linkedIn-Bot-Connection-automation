from selenium import webdriver
from time import sleep


def login():
    driver.get(login_url)
    sleep(2)

    # Setting up login details
    email_element = driver.find_element_by_id('username')
    password_element = driver.find_element_by_id('password')
    # Sending Input in the field
    email_element.send_keys(email)
    password_element.send_keys(password)

    # Submitting the login request
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "mercado-button--primary", " " ))]').click()


def open_networks():
    driver.get(network_url)
    driver.maximize_window()


def send_requests():
    flag = 1
    while flag:
        # Getting all button elements
        button_elements = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "artdeco-button__text", " " ))]')
        for i in button_elements:
            if i.text == 'Connect':
                try:
                    i.click()
                    print("Connection Request send")
                except:
                    print("Skipped")
                sleep(1)

        # Scroll down the page and refresh the button list
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2.5)
        # stopping condition to be added
        # flag = 0


if __name__ == '__main__':
    login_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    network_url = "https://www.linkedin.com/mynetwork/"

    # Taking user input to set credentials
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Invalid credential conditions to be added.

    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    login()
    sleep(5)

    open_networks()
    sleep(5)

    send_requests()
    print("Done for today")
