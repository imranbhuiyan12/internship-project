from page.base_page import BasePage
from page.main_page import MainPage
from page.off_plan import OffPlanPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.off_plan = OffPlanPage(driver)