import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from base_pages.Home_Page import Home_Page
from base_pages.saree_page import Saree_Page
from utilities.read_properties import Read_Config


def pytest_addoption(
        parser):  # This is a special pytest hook function. It lets you add custom command-line options when running pytest.
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(
        browser):  # This is the actual WebDriver setup fixture. It uses the browser fixture to determine which driver to launch
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    yield driver  # Everything before yield runs before the test → this is setup., Everything after yield runs after the test → this is teardown.
    driver.quit()  # we have added teardown


@pytest.fixture()
def driver_navigated_to_saree_page(setup):  # setup fixture will give you the initialized driver
    driver = setup
    driver.maximize_window()
    driver.get(Read_Config.get_myntra_home_page_url())

    home_page = Home_Page(driver)
    home_page.hover_women_link()
    home_page.click_saree_link()

    #Switch to the new tab that opens on clicking Saree
    main_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    yield driver


@pytest.fixture()
def driver_navigated_to_selected_saree_page(driver_navigated_to_saree_page):  # setup fixture will give you the initialized driver
    driver = driver_navigated_to_saree_page
    saree_selected = Saree_Page(driver)
    saree_selected.click_more_brand()
    saree_selected.select_anouk_brand()
    saree_selected.select_pink_colour()
    saree_selected.hover_sort()
    saree_selected.click_option_sort()
    saree_selected.click_saree()

    # Switch to selected saree tab
    driver.main_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != driver.main_window:
            driver.switch_to.window(handle)
            break

    # Optionally, verify that we're on the right page (you can also use a URL check here)
    yield driver
