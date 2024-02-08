from pages.textbox_page import TextBoxPage
from faker import Faker
from conftest import *


def test_textbox_page_positive(browser):
    """
    Description:
     - Positive scenario for filling the input fields Full Name, Email, Current Address, Permanent Address,
     pressing the Submit button and checking the text ot result fields.
     - Browser: Chrome.

     Checks:
         - Result Full Name == Input Full Name
         - Result Email == Input Email
         - Result Current Address == Input Current Address
         - Result Permanent Address == Input Permanent Address

    :param browser: fixture object for getting web driver.
    :return:
    """
    page = TextBoxPage(browser)

    # Generating the fake data for input fields filling
    fakedata = Faker("ru_RU")
    fullname = fakedata.name()
    email = fakedata.ascii_free_email()
    current_address = fakedata.address()
    permanent_address = fakedata.address()

    page.enter_text(page.full_name, fullname)
    page.enter_text(page.email, email)
    page.enter_text(page.current_address, current_address)
    page.enter_text(page.permanent_address, permanent_address)

    # Pressing the Submit button
    page.button_click(page.submit_button)

    # Checking the result fields
    assert page.get_text(page.result_fullname) == "Name:" + fullname, "Incorrect Fullname"
    assert page.get_text(page.result_email) == "Email:" + email, "Incorrect Email"
    assert (page.get_text(page.result_current_address) ==
            "Current Address :" + current_address), "Incorrect Current Address"
    assert (page.get_text(page.result_permanent_address) ==
            "Permananet Address :" + permanent_address), "Incorrect Permanent Address"
