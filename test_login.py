import pytest
from selenium import webdriver
from practical_task_1_login.page_objects import LoginPage
from practical_task_1_login.page_objects import HomePage


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_valid_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    usernames = ["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
    for username in usernames:
        login_page.enter_username(username)
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        assert home_page.get_subtitle() == "Products"
        home_page.click_logout_button()


def test_invalid_password_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
hegit     login_page.enter_password("invalid_password")
    login_page.click_login_button()
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"


def test_invalid_username_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("invalid_username")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"


def test_empty_fields_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login_button()
    assert login_page.get_error_message() == "Epic sadface: Username is required"


def test_locked_out_user(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()
    assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out."


def test_all_users_have_same_item_images(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    usernames = ["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
    image_links = {}
    for username in usernames:
        login_page.enter_username(username)
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        assert home_page.get_subtitle() == "Products"
        images = home_page.get_item_images()
        image_links[username] = [image.get_attribute("src") for image in images]
        home_page.click_logout_button()

    assert image_links["standard_user"] == image_links["problem_user"]
    assert image_links["standard_user"] == image_links["performance_glitch_user"]
    assert image_links["standard_user"] == image_links["error_user"]
    assert image_links["standard_user"] == image_links["visual_user"]


def test_all_elements_are_same_for_users(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    usernames = ["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
    elements_text_values = {}
    for username in usernames:
        login_page.enter_username(username)
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        assert home_page.get_subtitle() == "Products"
        product_elements = home_page.get_all_product_elements()
        elements_text_values[username] = [element.text for element in product_elements]
        home_page.click_logout_button()
        assert driver.current_url == "https://www.saucedemo.com/"

    assert elements_text_values["standard_user"] == elements_text_values["problem_user"]
    assert elements_text_values["standard_user"] == elements_text_values["performance_glitch_user"]
    assert elements_text_values["standard_user"] == elements_text_values["error_user"]
    assert elements_text_values["standard_user"] == elements_text_values["visual_user"]


def test_all_users_have_same_element_locations(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    usernames = ["standard_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]
    element_locations = {}
    for username in usernames:
        login_page.enter_username(username)
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        assert home_page.get_subtitle() == "Products"
        element_locations[username] = home_page.get_location_of_all_elements()
        home_page.click_logout_button()

    assert element_locations["standard_user"] == element_locations["problem_user"]
    assert element_locations["standard_user"] == element_locations["performance_glitch_user"]
    assert element_locations["standard_user"] == element_locations["error_user"]
    assert element_locations["standard_user"] == element_locations["visual_user"]
