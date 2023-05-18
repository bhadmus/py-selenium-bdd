from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from data_elements.element_mapper import *


class HomePageObject:
    """
        This helps to resolve all actions carried out on the home page
    """

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)

    def launch_page(self):
        """
        This method launches the page
        :return: a launched web page
        """
        self.driver.get(LoginPage.url)
        self.driver.maximize_window()

    def click_element(self, element):
        """
        This method clicks any element that is parsed
        :return:
        """
        self.wait_for_presence(element)
        self.driver.find_element(By.CSS_SELECTOR, element).click()

    def wait_for_presence(self, element):
        """
        This method waits for the presence of the elements parsed
        :return:
        """
        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def wait_for_absence(self, element):
        """
        This method waits for the presence of the elements parsed
        :return:
        """
        self.wait.until(ec.invisibility_of_element_located((By.CSS_SELECTOR, element)))

    def wait_for_selection(self, element):
        """
        This method waits for the elements parsed to be selected
        :return:
        """
        self.wait.until(ec.element_located_to_be_selected((By.CSS_SELECTOR, element)))

    def wait_for_text_presence(self, element, text):
        """
        This method waits for the presence of the elements parsed to have a specified text
        :return:
        """
        self.wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, element), text))

    def verify_text(self, element, message):
        """
        This method verifies that the text on the element parsed matches the expected text
        :return:
        """
        self.wait_for_presence(element)
        expect_text = self.driver.find_element(By.CSS_SELECTOR, element).text
        assert expect_text == message

    def fill_details(self, field, text):
        """
        This method fills in a text into any field parsed
        :return:
        """
        self.wait_for_presence(field)
        self.driver.find_element(By.CSS_SELECTOR, field).send_keys(text)

    def execute_click_action(self, element):
        """
        This method uses the jQuery function to click an element
        :return:
        """
        self.wait_for_presence(element)
        ele = self.driver.find_element(By.CSS_SELECTOR, element)
        self.driver.execute_script("arguments[0].click();", ele)
