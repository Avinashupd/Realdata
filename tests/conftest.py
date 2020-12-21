import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def launchDriver(request):
    driver = webdriver.Chrome(executable_path="F:\\realtimeds\\chromedriver.exe")
    driver.get("https://customer.servetel.in/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
