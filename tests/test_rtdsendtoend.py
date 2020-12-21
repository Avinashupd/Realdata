from usecases.create_attendant import AttendantPage
from usecases.create_recording import RecordingPage
from usecases.login import LoginPage
from usecases.assign_attendant import MyNumberPage
from utilities.Base import BaseClass
from tests.apicalls import *


class TestRealTime(BaseClass):

    def test_loginPage(self):
        self.driver.implicitly_wait(5)
        loginpage = LoginPage(self.driver)
        loginpage.username().send_keys("avinashupadhyay99@gmail.com")
        loginpage.password().send_keys("Avirtds@18")
        loginpage.login().click()

    def test_recordingPage(self):
        recordingpage = RecordingPage(self.driver)
        recordingpage.serviceLink().click()
        self.driver.execute_script("arguments[0].scrollIntoView();", recordingpage.systemRecord())
        recordingpage.systemRecord().click()
        recordingpage.uploadRecBtn().click()
        recordingpage.addRecHeader().is_displayed()
        recordingpage.addRecName().send_keys("Avinash")
        recordingpage.createRecRadio().click()
        recordingpage.addRecText().send_keys("Hello, Welcome to real world.")
        recordingpage.generateRecBtn().click()
        recordingpage.generatedAudio().is_displayed()
        recordingpage.saveAudio().click()
        self.verifyElementlocated(recordingpage.new_agent)
        assert recordingpage.addedRecording().text == "Avinash"
        print("second usecase finished")

    def test_createAgent(self):
        post_agent()
        print("agent added successfully")

    def test_attendantPage(self):
        attendantpage = AttendantPage(self.driver)
        attendantpage.attendantLink().click()
        attendantpage.addAttendant().click()
        attendantpage.attendantName().send_keys("Avinash Upadhyay")
        attendantpage.attendantDescription().send_keys("create autoattendent")
        attendantpage.attendantRecord().click()
        attendantpage.selectRecord().send_keys("Avi")
        attendantpage.selectedRecording().click()
        attendantpage.saveRecording().click()

    def test_myNumbertPage(self):
        mynumberpage = MyNumberPage(self.driver)
        mynumberpage.myNumberLink().click()
        mynumberpage.actionBtn().click()
        mynumberpage.editLink().click()
        mynumberpage.name().send_keys("Avinashupd")
        mynumberpage.destinationTxtField().click()
        mynumberpage.selectDestination().send_keys("Avi")
        mynumberpage.selectedDestination().click()
        mynumberpage.savepage().click()
        self.verifyElementlocated(mynumberpage.assigned_agent)
