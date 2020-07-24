# Open https://the-internet.herokuapp.com/login

# Please automate next test cases:
# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
# 2. Login with invalid creds and check validation error
# 3. Logout from app and assert you successfully logged out

def log_in_valid_data():
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element_by_css_selector('#username').send_keys('tomsmith')
    driver.find_element_by_css_selector('#password').send_keys('SuperSecretPassword!')
    driver.find_element_by_css_selector('.radius').click()
    element = driver.find_element_by_css_selector('.flash.success')
    assert element.text == 'You logged into a secure area!\n×'
    # driver.quit()



def log_in_invalid_data():
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element_by_css_selector('#username').send_keys('Jack_Daniels')
    driver.find_element_by_css_selector('#password').send_keys('!')
    driver.find_element_by_css_selector('.radius').click()
    element = driver.find_element_by_css_selector('[id="flash"]')
    assert element.text == 'Your username is invalid!\n×'
    driver.quit()



def log_in_log_out():
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element_by_css_selector('#username').send_keys('tomsmith')
    driver.find_element_by_css_selector('#password').send_keys('SuperSecretPassword!')
    driver.find_element_by_css_selector('.radius').click()
    driver.find_element_by_css_selector('.button.secondary.radius').click()
    element = driver.find_element_by_css_selector('[id="flash"]')
    assert element.text == 'You logged out of the secure area!\n×'
    driver.quit()

log_in_valid_data()
log_in_invalid_data()
log_in_log_out()
