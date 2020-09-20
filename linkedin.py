from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, WebDriverException


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
    driver.find_element_by_xpath(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "mercado-button--primary", " " ))]').click()


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
    requests = 0
    while flag:
        # Getting all button elements
        button_elements = driver.find_elements_by_xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "artdeco-button__text", " " ))]')
        for i in button_elements:
            if i.text == 'Connect':
                try:
                    i.click()
                    print("Connection Request send")
                    requests += 1
                except:
                    print("Skipped", count_skipped)
                    try:
                        driver.find_element_by_class_name(
                            "artdeco-button ip-fuse-limit-alert__primary-action artdeco-button--2 artdeco-button--primary ember-view").click()
                    except NoSuchElementException:
                        pass
                    count_skipped += 1
                    if count_skipped == 4:
                        flag = 0
                sleep(1)
            if requests <= 50:
                break

        # Scroll down the page and refresh the button list
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2.5)


def visibilty(company_name):
    driver.get("https://www.linkedin.com/company/" + company_name + "/people/")
    list = []
    sleep(2)

    number = driver.find_element_by_xpath("//*[@class='t-20 t-black']")
    print(number.text)
    c = number.text
    print("Total", c)
    number = int(input("Enter Number Of profiles you want to visit:"))
    while True:
        number -= 10
        try:
            
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(2.5)
        except WebDriverException:
            break
        if number < 0:
            break

    links_list = driver.find_elements_by_xpath("//*[@class='ember-view link-without-visited-state']")
    for i in links_list:
        list.append(i.get_attribute('href'))

    for i in list:
        print(i)
        sleep(2)
        try:
            driver.get(i)
            print("visited", i)
        except WebDriverException:
            break


def get_visibility():
    list_links = driver.find_elements_by_xpath("//div[@class='discover-entity-type-card__info-container']//a")
    for j in list_links[0:50]:
        driver.get(j.get_attribute('href'))
        print("Profile visited ")
        sleep(2)


if __name__ == '__main__':
    login_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    network_url = "https://www.linkedin.com/mynetwork/"

    # Taking user input to set credentials
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Driver running
    driver = webdriver.Chrome(
        executable_path=r'C:\Users\aishk\Downloads\Compressed\payroll-scrapers-master\payroll-scrapers-master\era_nlp\verifiers\swiggy_selenium_new\chromedriver_win32_2\chromedriver.exe')

    # Calling the login function
    login()

    # wrong email check condition is left.

    # Check for correct password
    if check_credentials():
        sleep(5)
        print("What do you want to do")
        print("1. Send connection request+ profile visiting")
        print("2. Only Connection Requests")
        print("3. Visit company personel Profiles")
        choice = int(input("Enter Your Choice:"))
        if choice == 1:
            open_networks()
            sleep(5)
            send_requests()
            get_visibility()
        elif choice == 2:
            open_networks()
            sleep(5)
            send_requests()
        elif choice == 3:
            company = input("Enter Company Name")
            visibilty(company)
        else:
            print("Wrong Option Thanks")
        driver.quit()
        print("Done for today")
    else:
        driver.quit()
        print("Retry with correct password")
