import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Home_Page import Home_Page
from base_pages.saree_page import Saree_Page
from base_pages.Selected_Saree_Page import Selected_saree_page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test03_myntra_selected_saree_price:
    logger = Log_Maker.log_generator()

    def test_selected_saree_price(self, driver_navigated_to_selected_saree_page):
        self.logger = Log_Maker.log_generator()
        driver = driver_navigated_to_selected_saree_page
        self.logger.info("***************** navigated to selected saree page ******************")
        selected_saree_page = Selected_saree_page(driver)
        selected_saree_page.find_saree_price()
        self.logger.info("******************* Saree price is found *************")

    def test_correct_pincode(self, driver_navigated_to_selected_saree_page):
        self.logger = Log_Maker.log_generator()
        driver = driver_navigated_to_selected_saree_page
        self.logger.info("***************** navigated to selected saree page ******************")
        selected_saree_page = Selected_saree_page(driver)
        selected_saree_page.enter_correct_pincode("125001")
        self.logger.info("******************* Correct Pincode is entered *************")
        driver.save_screenshot(".\\screenshots\\correct_pincode.png")

    def test_incorrect_pincode(self, driver_navigated_to_selected_saree_page):
        self.logger = Log_Maker.log_generator()
        driver = driver_navigated_to_selected_saree_page
        self.logger.info("***************** navigated to selected saree page ******************")
        selected_saree_page = Selected_saree_page(driver)
        selected_saree_page.enter_incorrect_pincode("111111")
        self.logger.info("******************* Inorrect Pincode is entered *************")
        driver.save_screenshot(".\\screenshots\\incorrect_pincode.png")

    def test_add_to_bag(self,driver_navigated_to_selected_saree_page):
        self.logger = Log_Maker.log_generator()
        driver = driver_navigated_to_selected_saree_page
        self.logger.info("***************** navigated to selected saree page ******************")
        selected_saree_page = Selected_saree_page(driver)
        selected_saree_page.add_to_bag()