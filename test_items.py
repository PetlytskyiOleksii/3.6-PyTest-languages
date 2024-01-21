from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import *

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

add_product_button = By.ID, 'add_to_basket_form'


def test_to_check_if_add_to_basket_button_present(browser):
    browser.get(link)
    expected_result = WebDriverWait(browser, 10).until(ec.presence_of_element_located(add_product_button)).text
    print(expected_result)
    assert expected_result == 'Añadir al carrito'



