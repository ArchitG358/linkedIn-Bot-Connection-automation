from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException


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


def check_password():
    try:
        error = driver.find_element_by_id("error-for-password")
        if "Hmm, that's not the right password" in error.text:
            print("Wrong Password")
            return 0
        elif "Password must be 6 characters or more" in error.text:
            print("Short Password")
            return 0
    except NoSuchElementException:
        return 1
    else:
        return 0


def check_email():
    # To be completed.
    return 1


def check_credentials():
    if check_password and check_email:
        return 1
    else:
        return 0


def open_networks():
    driver.get(network_url)
    driver.maximize_window()


def send_requests():
    flag = 1
    count_skipped = 0
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
                    count_skipped += 1
                    if count_skipped == 4:
                        flag = 0
                sleep(1)

        # Scroll down the page and refresh the button list
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2.5)


if __name__ == '__main__':
    login_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    network_url = "https://www.linkedin.com/mynetwork/"

    # Taking user input to set credentials
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Driver running
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    # Calling the login function
    login()

    # wrong email check condition is left.

    # Check for correct password
    if check_credentials():
        sleep(5)
        open_networks()
        sleep(5)
        send_requests()
        driver.quit()
        print("Done for today")
    else:
        driver.quit()
        print("Retry with correct password")
