from selenium.webdriver.common.by import By


class AttendantPage:

    def __init__(self, driver):
        self.driver = driver

    attendant_link = (By.XPATH, "//*[@class='list']/li[4]/ul/li[5]/a")
    add_attendant = (By.XPATH, "//*[@class='btn btn-primary waves-effect']")
    attendant_name = (By.ID, "name")
    attendant_description = (By.ID, "description")
    attendant_record = (By.ID, "recording_chosen")
    select_record = (By.XPATH, "//div[@id='recording_chosen']//input[@type='text']")
    selected_recording = (By.XPATH, "//em[normalize-space()='Avi']")
    save_recording = (By.ID, "submitbutton")

    def attendantLink(self):
        return self.driver.find_element(*AttendantPage.attendant_link)

    def addAttendant(self):
        return self.driver.find_element(*AttendantPage.add_attendant)

    def attendantName(self):
        return self.driver.find_element(*AttendantPage.attendant_name)

    def attendantDescription(self):
        return self.driver.find_element(*AttendantPage.attendant_description)

    def attendantRecord(self):
        return self.driver.find_element(*AttendantPage.attendant_record)

    def selectRecord(self):
        return self.driver.find_element(*AttendantPage.select_record)

    def selectedRecording(self):
        return self.driver.find_element(*AttendantPage.selected_recording)

    def saveRecording(self):
        return self.driver.find_element(*AttendantPage.save_recording)
