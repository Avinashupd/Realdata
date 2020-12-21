from selenium.webdriver.common.by import By


class MyNumberPage:

    def __init__(self, driver):
        self.driver = driver

    my_number_link = (By.XPATH, "//*[@class='list']/li[4]/ul/li[1]/a")
    action_btn = (By.XPATH, "//button[@class='btn btn-default dropdown-toggle1']")
    edit_link = (By.XPATH, "//button[@class='btn btn-default dropdown-toggle1']/following-sibling::ul/li/a")
    name_field = (By.XPATH, "//form[@id='didNumberForm']//input[@id='name']")
    destination_txt_field = (By.ID, "did_destination_chosen")
    select_destination = (By.XPATH, "//div[@id='did_destination_chosen']//input[@type='text']")
    selected_destination = (By.XPATH, "//em[normalize-space()='Avi']")
    save_page = (By.XPATH, "//button[@class='btn btn-link waves-effect btn-active']")
    assigned_agent = (By.XPATH, "//a[normalize-space()='Avinash (Agent)']")


    def myNumberLink(self):
        return self.driver.find_element(*MyNumberPage.my_number_link)

    def actionBtn(self):
        return self.driver.find_element(*MyNumberPage.action_btn)

    def editLink(self):
        return self.driver.find_element(*MyNumberPage.edit_link)

    def name(self):
        return self.driver.find_element(*MyNumberPage.name_field)

    def destinationTxtField(self):
        return self.driver.find_element(*MyNumberPage.destination_txt_field)

    def selectDestination(self):
        return self.driver.find_element(*MyNumberPage.select_destination)

    def selectedDestination(self):
        return self.driver.find_element(*MyNumberPage.selected_destination)

    def savepage(self):
        return self.driver.find_element(*MyNumberPage.save_page)

    def assignedAgent(self):
        return self.driver.find_element(*MyNumberPage.assigned_agent)
