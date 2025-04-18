from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home_Page:
    # myntra_logo_xpath = "//a[@href='/']"
    women_section_xpath = "//a[@data-group='women']"
    homepage_searchbar_classname = "desktop-searchBar"
    saree_xpath = "//a[normalize-space()='Sarees']"

    def __init__(self, driver):  # we are sending driver as parameter in the constructor of Home_page base class
        self.driver = driver  # we can use it to access all class variables and methods, self keyword means it belongs to the class
        self.driver.maximize_window()
    # def myntra_logo_xpath(self):

    def hover_women_link(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,self.women_section_xpath)))
        women_element = self.driver.find_element(By.XPATH, self.women_section_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(women_element).perform()
        # saree_element = self.driver.find_element(By.XPATH, self.saree_xpath))
        # ActionChains(self.driver).move_to_element(saree_element).perform()
        #
        # try:
        #     saree_visible = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,self.saree_xpath)))
        #     assert saree_visible.is_displayed(), "Saree is not displayed"
        # except Exception as e:
        #     raise AssertionError(f"Hover failed:{str(e)}")

    def click_saree_link(self):
        saree_link = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH,self.saree_xpath)))
        saree_link.click()

    def enter_data_in_searchbar(self, data):
        self.driver.find_element(By.CLASS_NAME, self.homepage_searchbar_classname).send_keys(data)
