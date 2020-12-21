from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    user_name = (By.ID, "login_id")
    passwd = (By.ID, "password")
    login_btn = (By.ID, "login_button")

    def username(self):
        return self.driver.find_element(*LoginPage.user_name)

    def password(self):
        return self.driver.find_element(*LoginPage.passwd)

    def login(self):
        return self.driver.find_element(*LoginPage.login_btn)
