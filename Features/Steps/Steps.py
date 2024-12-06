from behave import given, when, then
import time
import allure


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()  # Make sure you have chromedriver installed and in PATH


@given(u'launch chrome browser')
def step_impl(context):
    driver.get("https://www.saucedemo.com/v1/")


@when(u'login')

def step_impl(context):
    username_box = driver.find_element(By.ID, "user-name")
    username_box.send_keys("standard_user")
    password_box = driver.find_element(By.ID, "password")
    password_box.send_keys("secret_sauce")
    login_btn = driver.find_element(By.ID, 'login-button')
    login_btn.click()
    time.sleep(5)

@then(u'filter the product')
def step_impl(context):
    filter_box = driver.find_element(By.CLASS_NAME, 'product_sort_container')
    filter_box.send_keys("lohi")
    filter_box.send_keys(Keys.RETURN)
    filter_box.click()
    time.sleep(10)

@then(u'navigate to left side')
def step_impl(context):
    side_menu_btn = driver.find_element(By.CLASS_NAME, 'bm-burger-button')
    side_menu_btn.click()
    time.sleep(5)
    # about_btn = driver.find_element(By.ID, 'about_sidebar_link')
    # about_btn.click()
    logout_link = driver.find_element(By.ID, 'logout_sidebar_link')
    logout_link.click()
    time.sleep(5)
@then(u'select one product')
def step_impl(context):
    search_box = driver.find_element(By.ID, "item_0_title_link")  # Adjust selector as needed
    # search_box.find_element(By.ID,'item_0_title_link')
    search_box.click()
    time.sleep(3)

@then(u'add to cart')
def step_impl(context):
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn_primary.btn_inventory"))  # Adjust ID
    )
    add_to_cart_button.click()
    time.sleep(3)
@then(u'go to cart iteam')
def step_impl(context):
    cart_btn = driver.find_element(By.ID, 'shopping_cart_container')
    cart_btn.click()
    time.sleep(3)

@then(u'close')
def step_impl(context):
    driver.close()
    time.sleep(5)



