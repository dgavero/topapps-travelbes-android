import logging
from telnetlib3 import EC

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from app_utilities.LogUtil import Logger
from app_utilities import configReader

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def click(self, locator):
        xpath_click_locator = configReader.readConfig("locators", locator)
        access_id_click_locator = configReader.readConfig("locators", locator)
        id_click_locator = configReader.readConfig("locators", locator)

        if str(locator).endswith("_XPATH"):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_click_locator)))
            self.driver.find_element(AppiumBy.XPATH, xpath_click_locator).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.wait.until(EC.visibility_of_element_located((By.ACCESSIBILITY_ID, access_id_click_locator)))
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, access_id_click_locator).click()
        elif str(locator).endswith("_ID"):
            self.wait.until(EC.visibility_of_element_located((By.ID, id_click_locator)))
            self.driver.find_element(AppiumBy.ID, id_click_locator).click()
        log.logger.info("Clicking on an Element " + str(locator))

    def type(self, locator, value):
        xpath_type_locator = configReader.readConfig("locators", locator)
        access_id_type_locator = configReader.readConfig("locators", locator)
        id_type_locator = configReader.readConfig("locators", locator)

        if str(locator).endswith("_XPATH"):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_type_locator)))
            self.driver.find_element(AppiumBy.XPATH, xpath_type_locator).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.wait.until(EC.visibility_of_element_located((By.ACCESSIBILITY_ID, access_id_type_locator)))
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, access_id_type_locator).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.wait.until(EC.visibility_of_element_located((By.ID, id_type_locator)))
            self.driver.find_element(AppiumBy.ID, id_type_locator).send_keys(value)
        log.logger.info("Typing in an Element " + str(locator) + " entered the value as : " + str(value))

    def getText(self, locator):
        xpath_text_locator = configReader.readConfig("locators", locator)
        access_id_text_locator = configReader.readConfig("locators", locator)
        id_text_locator = configReader.readConfig("locators", locator)
        text = None

        if str(locator).endswith("_XPATH"):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_text_locator)))
            text = self.driver.find_element(AppiumBy.XPATH, xpath_text_locator).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.wait.until(EC.visibility_of_element_located((By.ACCESSIBILITY_ID, access_id_text_locator)))
            text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, access_id_text_locator).text
        elif str(locator).endswith("_ID"):
            self.wait.until(EC.visibility_of_element_located((By.ID, id_text_locator)))
            text = self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).text
        log.logger.info("Getting text from an element " + str(locator))
        return text

    def clickIndex(self, locator, index):
        xpath_index_locator = configReader.readConfig("locators", locator)
        access_id_index_locator = configReader.readConfig("locators", locator)
        id_index_locator = configReader.readConfig("locators", locator)

        if str(locator).endswith("_XPATH"):
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_index_locator)))
            self.driver.find_element(AppiumBy.XPATH, xpath_index_locator)[index].click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.wait.until(EC.visibility_of_element_located((By.ACCESSIBILITY_ID, access_id_index_locator)))
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, access_id_index_locator)[index].click()
        elif str(locator).endswith("_ID"):
            self.wait.until(EC.visibility_of_element_located((By.ID, id_index_locator)))
            self.driver.find_element(AppiumBy.ID, id_index_locator)[index].click()
        log.logger.info("Clicking on an Element " + str(locator) + "with index : " + str(index))

    # def click(self, locator):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_ACCESSIBILITYID"):
    #         self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).click()
    #     log.logger.info("Clicking on an Element "+ str(locator))
    #
    # def type(self, locator, value):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
    #     elif str(locator).endswith("_ACCESSIBILITYID"):
    #         self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).send_keys(value)
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).send_keys(value)
    #     log.logger.info("Typing in an Element "+ str(locator)+ " entered the value as : "+ str(value))

    # def getText(self, locator):
    #     if str(locator).endswith("_XPATH"):
    #         text = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator)).text
    #     elif str(locator).endswith("_ACCESSIBILITYID"):
    #         text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).text
    #     elif str(locator).endswith("_ID"):
    #         text = self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator)).text
    #     log.logger.info("Getting text from an element "+ str(locator))
    #     return text
    #
    # def clickIndex(self, locator, index):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element(AppiumBy.XPATH, configReader.readConfig("locators", locator))[index].click()
    #     elif str(locator).endswith("_ACCESSIBILITYID"):
    #         self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator))[index].click()
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element(AppiumBy.ID, configReader.readConfig("locators", locator))[index].click()
    #     log.logger.info("Clicking on an Element "+ str(locator) + "with index : " + str(index))
