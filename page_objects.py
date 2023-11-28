from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locators
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.XPATH, '//h3[@data-test="error"]')

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text


class HomePage:

    # Locators
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    SUBTITLE = (By.CLASS_NAME, 'title')
    IMAGES = (By.XPATH, "//div[@class='inventory_item']//img")

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_subtitle(self):
        subtitle_element = self.driver.find_element(*self.SUBTITLE)
        return subtitle_element.text

    def get_item_images(self):
        item_images = self.driver.find_elements(*self.IMAGES)
        return item_images

    def get_all_product_elements(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    def get_location_of_all_elements(self):
        elements_to_check = [
            (By.CLASS_NAME, 'title'),
            (By.CLASS_NAME, 'inventory_item_name'),
            (By.CLASS_NAME, 'inventory_item_price'),
            (By.CLASS_NAME, 'btn_primary'),
            (By.CLASS_NAME, 'shopping_cart_link'),
        ]
        location_dict = {}
        for element_locator in elements_to_check:
            found_elements = self.driver.find_elements(*element_locator)
            element_key = element_locator[1]
            if not found_elements:
                continue
            location_dict[element_key] = [element.location for element in found_elements]
        return location_dict

    def click_logout_button(self):
        logout_button = self.driver.find_element(*self.LOGOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", logout_button)
