from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, 'https://demoqa.com/text-box', timeout)

        self.driver.get(self.url)

        self.full_name = (By.ID, 'userName')
        self.email = (By.ID, 'userEmail')
        self.current_address = (By.CSS_SELECTOR, 'textarea#currentAddress.form-control')
        self.permanent_address = (By.CSS_SELECTOR, 'textarea#permanentAddress.form-control')

        self.submit_button = (By.ID, 'submit')

        self.result_fullname = (By.ID, 'name')
        self.result_email = (By.ID, 'email')
        self.result_current_address = (By.CSS_SELECTOR, 'p#currentAddress.mb-1')
        self.result_permanent_address = (By.CSS_SELECTOR, 'p#permanentAddress.mb-1')
