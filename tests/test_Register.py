import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestRegister:
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_search_without_providing_any_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(expected_text)



















"""

    def test_create_account_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("umar")
        self.driver.find_element(By.ID, "input-lastname").send_keys("jasi")
        self.driver.find_element(By.ID, "input-email").send_keys("umarja22@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys("7865932145")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(3)
        expected_text = "Congratulations! Your new account has been success"
        assert self.driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations! Your new account has been success')]").text.__eq__(expected_text)

    def test_create_account_by_providing_all_fields(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("umar")
        self.driver.find_element(By.ID, "input-lastname").send_keys("jasi")
        self.driver.find_element(By.ID, "input-email").send_keys("umarja23@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys("7865932145")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(3)
        expected_text = "Congratulations! Your new account has been success"
        assert self.driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations! Your new account has been success')]").text.__eq__(expected_text)
"""
