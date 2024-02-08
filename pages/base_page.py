from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
    Base class for PageObject
    """
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def button_click(self, locator):
        button = self.find_element(locator)
        button.click()
