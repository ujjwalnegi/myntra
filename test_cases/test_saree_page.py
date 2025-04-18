import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Home_Page import Home_Page
from base_pages.saree_page import Saree_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test02_Myntra_Saree_Page:
    def test_filters_saree_page(self,driver_navigated_to_saree_page):
        self.logger = Log_Maker.log_generator()
        driver = driver_navigated_to_saree_page
        self.logger.info("************* Navigated to saree with all the filters page ****************")
        saree_page = Saree_Page(driver)
        time.sleep(5)
        saree_page.click_more_brand()
        saree_page.select_anouk_brand()
        time.sleep(7)
        saree_page.select_pink_colour()
        saree_page.hover_sort()
        time.sleep(5)
        saree_page.click_option_sort()
        time.sleep(10)
        saree_page.click_saree()
        time.sleep(10)

