import time

from selenium.webdriver.common.by import By


def test_can_add_item_into_cart(browser):
    browser.get(
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    )
    time.sleep(5)
    assert browser.find_element(
        By.CLASS_NAME,
        ('btn-add-to-basket')
    ), 'Невозможно добавить товар в корзину'
