from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# service = Service(executable_path="chromedriver.exe")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://staging-hqzen.cxrole.com")
assert 'HQZen' in driver.title

signin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='action primary']"))
)
signin.click()


username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'username'))
)
username.send_keys('amanda@bposeats.com')


password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'password'))
)
password.send_keys('bposeats')


signinbutton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='semibold block large primary']"))
)
signinbutton.click()

homebutton = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'step1'))
)
homebutton.click()

citbutton = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'step2'))
)
citbutton.click()

bposeatsbtn = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/company/10/workforce/49/overview/8722')]"))
)
bposeatsbtn.click()

recruitment = WebDriverWait(driver, 15).until(
     EC.element_to_be_clickable((By.XPATH, "//i[@class='mdi mdi-briefcase-search-outline']"))
)
recruitment.click()

searchjobs = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '//*[@type="text" and @placeholder="Search job posting"]'))
)
searchjobs.send_keys('AI Engineer')

components = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="posting"]'))
)
first_component = components[0]
first_component.click()

time.sleep(20)

driver.quit()
