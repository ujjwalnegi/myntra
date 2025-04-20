import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Home_Page import Home_Page
from base_pages.saree_page import Saree_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test02_Myntra_Saree_Page:
    logger = Log_Maker.log_generator()

    def test_filters_saree_page(self, driver_navigated_to_saree_page):
        self.logger = Log_Maker.log_generator()
        driver = driver_navigated_to_saree_page
        self.logger.info("************* Navigated to saree with all the filters page ****************")
        saree_page = Saree_Page(driver)
        saree_page.click_more_brand()
        self.logger.info("******************* More brand is clicked*************")
        saree_page.select_anouk_brand()
        self.logger.info("******************* Anouk brand is selected *************")
        saree_page.select_pink_colour()
        self.logger.info("******************* Pink colour is selected *************")
        saree_page.hover_sort()
        self.logger.info("******************* Hovered on dropdown *************")
        saree_page.click_option_sort()
        self.logger.info("******************* What's new option is selected *************")
        saree_page.click_saree()
        self.logger.info("******************* Saree is selected *************")
