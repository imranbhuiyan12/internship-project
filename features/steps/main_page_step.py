from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given ('Open the main page')
def open_main(context):
    context.app.main_page.open_main()


# @then ('Log in to the page')
# def log_in(context ):
#     context.find_element(By.ID, 'email-2').send_keys()
#     sleep(6)

@given ('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@then('Log in to the page email and password')
def log_in(context):
    # email = context.driver.find_element(By.ID, 'email-2').send_keys('ibhuiyan15@gmail.com')
    # password = context.driver.find_element(By.ID, 'field').send_keys('123456')
    #
    # sleep(10)
    # context.driver.find_element(By.CSS_SELECTOR, "[class *= 'login-button']").click()
    # sleep(5)
    context.app.main_page.log_in()




