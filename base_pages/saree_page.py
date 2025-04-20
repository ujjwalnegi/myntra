import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Saree_Page():
    more_brand_xpath = "//div[@class='brand-more']"
    all_brand_list = "//ul[@class='FilterDirectory-list']//li"
    anouk_brand_xpath = "//div[@class='FilterDirectory-panel FilterDirectory-expanded']/div[2]/ul/li[6]"
    all_saree_xpath = "//li[contains(@class, 'product-base')]"
    pink_colour_xpath = "//span[@data-colorhex='pink']"
    hover_sort_by_xpath = "//div[@class='sort-sortBy']"
    sort_by_option_xpath = "//div[@class='horizontal-filters-sortContainer']/div/div/div/ul/li[2]"
    popup_xpath = "//div[@class='FilterDirectory-panel FilterDirectory-expanded']"
    popup_close_xpath = "//span[@class='myntraweb-sprite FilterDirectory-close sprites-remove']"
    price_Saree_xpath = "//span[@class='product-discountedPrice']"
    saree_xpath = "//li[@class='product-base'][1]"
    whats_new_xpath = "//main//div//div//div//div//div//div//div//div//div[1]//span[1]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)  # You can reuse this in all methods

    def click_more_brand(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.more_brand_xpath)))
        self.driver.find_element(By.XPATH, self.more_brand_xpath).click()

    def select_anouk_brand(self):
        all_brands = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH,self.all_brand_list)))
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.anouk_brand_xpath)))
        anouk_brand = self.driver.find_element(By.XPATH, self.anouk_brand_xpath)
        for brand in all_brands:
            if brand == anouk_brand:
                anouk_brand.click()
                print(f"Brand selected : {anouk_brand}")
                break
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.popup_close_xpath)))
        self.driver.find_element(By.XPATH, self.popup_close_xpath).click()



    def select_pink_colour(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pink_colour_xpath)))
        self.driver.find_element(By.XPATH, self.pink_colour_xpath).click()

    def hover_sort(self):
        # Wait until the sort container is present in DOM
        dropdown_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.hover_sort_by_xpath)))

        # Scroll the element into view (required for Myntra's sticky layout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_element)

        # Wait until the element is actually visible and interactable
        self.wait.until(EC.visibility_of(dropdown_element))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.hover_sort_by_xpath)))

        # Perform hover action
        ActionChains(self.driver).move_to_element(dropdown_element).pause(1).perform()

    def click_option_sort(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sort_by_option_xpath)))
        self.driver.find_element(By.XPATH, self.sort_by_option_xpath).click()
        expected_text = "What'S New"
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH,self.whats_new_xpath),expected_text))
        whats_new_text = self.driver.find_element(By.XPATH,self.whats_new_xpath).text
        print(f"expected : {expected_text}")
        print(f"actual : {whats_new_text}")
        assert expected_text in whats_new_text

    def click_saree(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.saree_xpath)))
        self.driver.find_element(By.XPATH, self.saree_xpath).click()
