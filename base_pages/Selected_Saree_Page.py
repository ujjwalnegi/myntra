from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.custom_logger import Log_Maker


class SelectedSareePage:
    saree_price_xpath = "//span[@class='pdp-price']"
    enter_pincode_xpath = "//input[@placeholder='Enter pincode']"
    click_check_xpath = "//input[@value='Check']"
    add_to_bag_xpath = "//div[normalize-space()='ADD TO BAG']"
    change_pincode_xpath = "//button[contains(.,'Change')]"
    pincode_error_xpath = "//p[@class='pincode-error pincode-enterPincode']"
    pincode_service_avl_list_xpath = "//ul[@class='pincode-serviceability-list']"
    enter_pincode_text_xpath = "//p[@class='pincode-enterPincode']"
    one_size_button_xpath = "//p[normalize-space()='Onesize']"
    gotocarttext_xpath = "//a[@class='pdp-goToCart pdp-add-to-bag pdp-button pdp-flex pdp-center ']/span[1]"
    go_to_cart_xpath = "//a[@class='pdp-goToCart pdp-add-to-bag pdp-button pdp-flex pdp-center ']"

    def __init__(self, driver):
        self.driver = driver
        self.logger = Log_Maker.log_generator()
        self.wait = WebDriverWait(self.driver, 30)

    #
    def find_saree_price(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.saree_price_xpath)))
        saree_price = self.driver.find_element(By.XPATH, self.saree_price_xpath).text
        self.logger.info(f"Saree price is : {saree_price}")

    def enter_correct_pincode(self, correct_pincode):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.enter_pincode_xpath)))
        self.driver.find_element(By.XPATH, self.enter_pincode_xpath).send_keys(correct_pincode)
        self.driver.find_element(By.XPATH, self.click_check_xpath).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.pincode_service_avl_list_xpath)))

        assert self.driver.find_element(By.XPATH, self.pincode_service_avl_list_xpath).is_displayed()

        self.driver.find_element(By.XPATH, self.change_pincode_xpath).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.enter_pincode_xpath)))
        pincode_text = self.driver.find_element(By.XPATH, self.enter_pincode_text_xpath).text
        print(pincode_text)
        expected_text = "Please enter PIN code to check delivery time & Pay on Delivery Availability"
        assert expected_text == pincode_text

    def enter_incorrect_pincode(self, incorrect_pincode):
        pincode_field = self.driver.find_element(By.XPATH, self.enter_pincode_xpath)
        pincode_field.clear()
        pincode_field.send_keys(incorrect_pincode)
        self.driver.find_element(By.XPATH, self.click_check_xpath).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.pincode_error_xpath)))
        error_msg_for_wrong_pin = self.driver.find_element(By.XPATH, self.pincode_error_xpath).text
        expected_msg_for_wrong_pin = "Unfortunately we do not ship to your pincode"
        assert error_msg_for_wrong_pin == expected_msg_for_wrong_pin

    def add_to_bag(self):
        self.driver.find_element(By.XPATH, self.one_size_button_xpath).click()
        add_to_bag = self.driver.find_element(By.XPATH, self.add_to_bag_xpath)
        if add_to_bag.is_enabled():
            print(f"Add to bag is enabled")
            add_to_bag.click()
        else:
            print(f"Add to bag is disabled")
            self.driver.close()
            self.driver.switch_to.window(self.driver.main_window)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.gotocarttext_xpath)))
        go_to_cart_text = self.driver.find_element(By.XPATH, self.gotocarttext_xpath).text
        print(f"Actual Text : {go_to_cart_text}")
        expected_text = "GO TO BAG"
        print(f'Expected Text : {expected_text}')
        assert expected_text == go_to_cart_text

    def go_to_cart(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.gotocarttext_xpath)))
        self.driver.find_element(By.XPATH,self.gotocarttext_xpath).click()

