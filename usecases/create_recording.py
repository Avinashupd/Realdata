from selenium.webdriver.common.by import By


class RecordingPage:

    def __init__(self, driver):
        self.driver = driver

    services_link = (By.XPATH, "//*[@class='list']/li[4]")
    sys_record = (By.XPATH, "//*[@class='list']/li[4]/ul/li[8]/a")
    upload_rec_btn = (By.XPATH, "//*[@class='btn btn-primary waves-effect']")
    add_rec_header = (By.XPATH, "//*[@id='modaladdmusic']/div/div/div/h4")
    add_rec_name = (By.ID, "name")
    create_rec_radio = (By.XPATH, "//label[@for='create_recording']")
    add_rec_text = (By.ID, "speechinput")
    generate_rec_btn = (By.ID, "generate_recording")
    generated_audio = (By.ID, "audiotag")
    save_audio = (By.ID, "saveandsubmitbtn")
    added_rec = (By.XPATH, "//tbody/tr[1]/td[2]")
    new_agent = (By.XPATH, "//td[normalize-space()='Avinash']")

    def serviceLink(self):
        return self.driver.find_element(*RecordingPage.services_link)

    def newAgent(self):
        return self.driver.find_element(*RecordingPage.new_agent)

    def systemRecord(self):
        return self.driver.find_element(*RecordingPage.sys_record)

    def uploadRecBtn(self):
        return self.driver.find_element(*RecordingPage.upload_rec_btn)

    def addRecHeader(self):
        return self.driver.find_element(*RecordingPage.add_rec_header)

    def addRecName(self):
        return self.driver.find_element(*RecordingPage.add_rec_name)

    def createRecRadio(self):
        return self.driver.find_element(*RecordingPage.create_rec_radio)

    def addRecText(self):
        return self.driver.find_element(*RecordingPage.add_rec_text)

    def generateRecBtn(self):
        return self.driver.find_element(*RecordingPage.generate_rec_btn)

    def generatedAudio(self):
        return self.driver.find_element(*RecordingPage.generated_audio)

    def saveAudio(self):
        return self.driver.find_element(*RecordingPage.save_audio)

    def addedRecording(self):
        return self.driver.find_element(*RecordingPage.added_rec)






