import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("launchDriver")
class BaseClass:

    def verifyTextPresence(self, locator, text):
        element = WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(locator, text))

    def verifyElementlocated(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
