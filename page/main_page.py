from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then

from page.base_page import BasePage




class MainPage(BasePage):
    EMAIL = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    CONTINUE = (By.CSS_SELECTOR, "[class *= 'login-button']")


    def open_main(self):
        self.open_url('https://soft.reelly.io/')
        sleep(5)




    def log_in(self):
        self.input_text('ibhuiyan15@gmail.com', *self.EMAIL)

        self.input_text('123456', *self.PASSWORD)
        sleep(5)
        self.click(*self.CONTINUE)












