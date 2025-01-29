from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import Select

from page.base_page import BasePage


class OffPlanPage(BasePage):


    OFF_PLAN = (By.CSS_SELECTOR, "[wized = 'mobileTabProperties']")
    OFF_PLAN_TITLE = (By.XPATH, "//a[text()='Off-plan']")
    DD_FILTER = (By.CSS_SELECTOR, "[id = 'Location-2']")
    ALL_PRODUCT = (By.CSS_SELECTOR, "[wized='cardOfProperty']")
    OOS = (By.CSS_SELECTOR,"[wized='projectStatus']")





    def click_off_plan_button(self):
        self.click(*self.OFF_PLAN)
        sleep(5)



    def verify_right_page(self):
        expected = 'Off-plan'
        self.verify_text(expected, *self.OFF_PLAN_TITLE)
        print("The page is verified")




    def select_filter(self):
        dd = self.find_element(*self.DD_FILTER)
        select = Select(dd)
        select.select_by_value('Out of stock')
        sleep(5)



    def verify_each_listing(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        all_product = self.driver.find_elements(By.CSS_SELECTOR, "[wized='cardOfProperty']")
        print(all_product)
        for OutOfStock in all_product:
            tag_oos = OutOfStock.find_elements(By.CSS_SELECTOR, "[wized='projectStatus']")
            assert tag_oos != '', f"product not shown"























