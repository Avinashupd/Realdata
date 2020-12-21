from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="F:\\realtimeds\\chromedriver.exe")
driver.get("https://customer.servetel.in/login")
driver.maximize_window()
driver.implicitly_wait(5)
#driver.get_screenshot_as_file("Home_page.png")
driver.find_element_by_id("login_id").send_keys("avinashupadhyay99@gmail.com")
driver.find_element_by_id("password").send_keys("Avirtds@18")
driver.find_element_by_id("login_button").click()
#2
driver.find_element_by_xpath("//*[@class='list']/li[4]").click()
sys_record = driver.find_element_by_xpath("//*[@class='list']/li[4]/ul/li[8]/a")
driver.execute_script("arguments[0].scrollIntoView();", sys_record)
sys_record.click()
driver.find_element_by_xpath("//*[@class='btn btn-primary waves-effect']").click()
driver.find_element_by_xpath("//*[@id='modaladdmusic']/div/div/div/h4").is_displayed()
driver.find_element_by_id("name").send_keys("Avinash")
driver.find_element_by_xpath("//label[@for='create_recording']").click()
driver.find_element_by_id("speechinput").send_keys("Hello, Welcome to real world.")
driver.find_element_by_id("generate_recording").click()
driver.find_element_by_id("audiotag").is_displayed()
driver.find_element_by_id("saveandsubmitbtn").click()
explicit_wait = WebDriverWait(driver, 20)
explicit_wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//tbody/tr[1]/td[2]"), 'Avinash'))
print("last line")
#3api reference
#4
driver.find_element_by_xpath("//*[@class='list']/li[4]/ul/li[5]/a").click()
driver.find_element_by_xpath("//*[@class='btn btn-primary waves-effect']").click()
driver.find_element_by_id("name").send_keys("Avinash Upadhyay")
driver.find_element_by_id("description").send_keys("create autoattendent")
driver.find_element_by_id("recording_chosen").click()
driver.find_element_by_xpath("//div[@id='recording_chosen']//input[@type='text']").send_keys("Avi")
driver.find_element_by_xpath("//em[normalize-space()='Avi']").click()
#recording = Select(driver.find_element_by_id("recording"))
#recording.select_by_value("Avinash")
driver.find_element_by_id("submitbutton").click()
#5
driver.find_element_by_xpath("//*[@class='list']/li[4]/ul/li[1]/a").click()
driver.find_element_by_xpath("//button[@class='btn btn-default dropdown-toggle1']").click()
driver.find_element_by_xpath("//button[@class='btn btn-default dropdown-toggle1']/following-sibling::ul/li/a").click()
driver.find_element_by_xpath("//form[@id='didNumberForm']//input[@id='name']").send_keys("Avinashupd")
driver.find_element_by_id("did_destination_chosen").click()
driver.find_element_by_xpath("//div[@id='did_destination_chosen']//input[@type='text']").send_keys("Avi")
driver.find_element_by_xpath("//em[normalize-space()='Avi']").click()
driver.find_element_by_xpath("//button[@class='btn btn-link waves-effect btn-active']").click()
explicit_wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[normalize-space()='Avinash ("
                                                                               "Agent)']")))
driver.close()
