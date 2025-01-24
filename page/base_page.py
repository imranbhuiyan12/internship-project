from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from support.logger import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def open_url(self, url):
        self.driver.get(url)
        logger.info(f"Opening url: {url}")



    def find_element(self, *locator):
        logger.info(f"Finding elements: {locator}")
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f"Finding elements: {locator}")
        return self.driver.find_element(*locator)

    def click(self, *locator):
        logger.info(f"Clicking element: {locator}")
        self.driver.find_element(*locator).click()

    def input_text(self,text, *locator):
        logger.info(f"Input text: {text}")
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f"expected {expected_text} not in {actual_text}"














    def verify_partial_url(self, expected_url, *locator):
        url = self.driver.current_url
        assert expected_url in url, f"expected {expected_url} not in {url}" 