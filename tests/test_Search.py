import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestSearch:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="search_for_a_valid_product",attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.MINOR)
    def test_search_for_a_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(expected_text)

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_search_without_providing_any_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(expected_text)

