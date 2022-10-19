from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_existing_add_to_basket_button(driver):
    driver.get(link)
    button = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))
    assert button, 'add-to-basket button is missing'
