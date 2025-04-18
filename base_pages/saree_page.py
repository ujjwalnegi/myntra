from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Saree_Page():
    more_brand_xpath = "//div[normalize-space()='+ 873 more']"
    anouk_brand_xpath = "//div[@class='FilterDirectory-panel FilterDirectory-expanded']/div[2]/ul/li[6]"
    all_saree_xpath = "(//li[contains(@class, 'product-base')])"
    # slider_xpath = "//div[@class='slider-root']/div[1]/div[4]"
    # slider_amount_xpath = "//div[@class='slider-root']/div[2]"
    pink_colour_xpath = "//span[@data-colorhex='pink']"
    hover_sort_by_xpath = "//div[@class='sort-sortBy']"
    sort_by_option_xpath = "//div[@class='horizontal-filters-sortContainer']/div/div/div/ul/li[2]"
    popup_xpath = "//div[@class='FilterDirectory-panel FilterDirectory-expanded']"
    popup_close_xpath = "//span[@class='myntraweb-sprite FilterDirectory-close sprites-remove']"
    price_Saree_xpath = "//span[@class='product-discountedPrice']"

    def __init__(self, driver):
        self.driver = driver

    def click_more_brand(self):
        self.driver.find_element(By.XPATH, self.more_brand_xpath).click()

    def select_anouk_brand(self):
        self.driver.find_element(By.XPATH, self.anouk_brand_xpath).click()
        self.driver.find_element(By.XPATH, self.popup_close_xpath).click()

    def select_pink_colour(self):
        self.driver.find_element(By.XPATH, self.pink_colour_xpath).click()

    def hover_sort(self):
            wait = WebDriverWait(self.driver, 15)

            # Wait until the sort container is present in DOM
            dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, self.hover_sort_by_xpath)))

            # Scroll the element into view (required for Myntra's sticky layout)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown_element)

            # Wait until the element is actually visible and interactable
            wait.until(EC.visibility_of(dropdown_element))
            wait.until(EC.element_to_be_clickable((By.XPATH, self.hover_sort_by_xpath)))

            # Perform hover action
            ActionChains(self.driver).move_to_element(dropdown_element).pause(1).perform()

    def click_option_sort(self):
        self.driver.find_element(By.XPATH, self.sort_by_option_xpath).click()

    def click_saree(self):
        # self.driver.find_element(By.XPATH, self.anouk_selected_saree_xpath)
        # Get all price elements
        price_elements = self.driver.find_elements(By.XPATH, self.price_Saree_xpath)

        # Get all product containers (saree tiles)
        products_displayed_on_screen = self.driver.find_elements(By.XPATH, self.all_saree_xpath)

        for index, price_element in enumerate(price_elements):
            try:
                # convert price to int
                price_text = price_element.text.strip().replace("Rs.", "").replace(",", "")
                price = int(price_text)

                if price <= 1000:
                    # Get the corresponding saree tile and click it
                    saree_link = products_displayed_on_screen[index].find_element(By.TAG_NAME, "a")
                    print(saree_link.text)
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", saree_link)
                    saree_link.click()
                    break

            except Exception as e:
                print(f"Skipping element due to error: {e}")
                continue
