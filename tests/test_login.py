import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class TestLogin:
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_search_without_providing_any_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH,
                                        "//p[contains(text(),'There is no product that matches the search criter')]").text.__eq__(
            expected_text)


"""
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("umarfaru01@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("syn12345")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT, "Account").is_displayed()

    def test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(5)
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']").text.__contains__(expected_warning_message)

"""