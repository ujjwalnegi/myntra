import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Home_Page import HomePage
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test01_Myntra_Home_Page:
    myntra_home_page_url = Read_Config.get_myntra_home_page_url()
    logger = Log_Maker.log_generator()

    def test_title_verification(self, setup):
        self.logger.info("*********Test Case 1 has started - Verifying title****************")
        driver = setup
        # self.driver = webdriver.Chrome() # we have created instance of our driver by using webdriver.chrome , i have commented this because now i have added setup from conftest file to invoke browser
        # self.driver means we can use this driver then we can use class variable like myntra page url , now i have removed self from every method because now we are using fixture
        driver.maximize_window()

        driver.get(self.myntra_home_page_url)
        actual_title = driver.title
        time.sleep(5)
        expected_title = "Online Shopping for Women, Men, Kids Fashion & Lifestyle - Myntra"
        if actual_title == expected_title:
            assert True
            # self.driver.close() #commenting out close method because we have mentioned teardown in our conftest
        else:
            assert False
            # self.driver.close()
        self.logger.info("*************** Title Verified *****************")
        driver.save_screenshot(".\\screenshots\\title_verified.png")

    def test_hover_women_link(self, setup):
        driver = setup
        driver.get(
            self.myntra_home_page_url)  # we are using self here because myntra_home_page_url is a class-level variable, and we're accessing it inside a method of the same class.
        home_page = HomePage(driver)
        home_page.hover_women_link()
        self.logger.info("**************** Hovered on women link *********************")
        home_page.click_saree_link()
        self.logger.info("************** Clicked on Saree Link ***************")


class Test_02_Searchbar_Homepage:
    myntra_home_page_url = Read_Config.get_myntra_home_page_url()
    logger = Log_Maker.log_generator()

    def test_search_correct_data(self, setup):
        driver = setup
        driver.get(self.myntra_home_page_url)
        home_page = HomePage(driver)
        home_page.enter_correct_data_in_searchbar("Shirt")

    def test_search_incorrect_data(self, setup):
        driver = setup
        driver.get(self.myntra_home_page_url)
        home_page = HomePage(driver)
        home_page.enter_incorrect_data_in_searchbar("@@@@@@@@@@@@")
        driver.save_screenshot(".\\screenshots\\no_data.png")

