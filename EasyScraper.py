from selenium.webdriver.common.by  import By
import chromedriver_autoinstaller
import time
import yagmail 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def yagemail(subject, to, content):
    subject = subject
    content = [content]
    user, app_password = getLoginCredentials()
    to = to
    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject, content)



def getLoginCredentials(creds_file):
    """ Reads a text file and captures login details.
    The file should be structured as:

    user@email.com
    password123

    This is in no way a secure way of doing things, but better than hardcoding.
    """
    with open(creds_file, "r") as f:
        email_addr = f.readline().strip("\n")
        app_pword = f.readline().strip("\n")
    return email_addr, app_pword



chromedriver_autoinstaller.install()

# options = Options()
options = webdriver.ChromeOptions() 
options.add_argument('--disable-blink-features=AutomationControlled')
options.headless = True
driver = webdriver.Chrome(options=options)


easy_jet = r"https://www.easyjet.com/en"


#driver.set_page_load_timeout(15)

driver.get(easy_jet)
time.sleep(10)


cookie_button = r"/html/body/section[2]/div/div/div[2]/button[2]"
try:
    driver.find_element(By.XPATH, cookie_button).click()
    print("Cookies accepted")
    time.sleep(2)
except:
    print("No cookies.")


body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.CONTROL + 't')

outbound = "/html/body/div[3]/div[1]/main/div/div[1]/section/div[1]/div/div/ul/li[1]/div/div/form/div[2]/div/div[2]/div[1]/input"
driver.find_element(By.XPATH,outbound).clear()
driver.find_element(By.XPATH,outbound).send_keys("London Luton (LTN)")
driver.find_element(By.XPATH,outbound).send_keys(Keys.RETURN)
time.sleep(1)

destination = "/html/body/div[3]/div[1]/main/div/div[1]/section/div[1]/div/div/ul/li[1]/div/div/form/div[2]/div/div[4]/div/input"
driver.find_element(By.XPATH,destination).send_keys("Santorini (JTR)")
driver.find_element(By.XPATH,destination).send_keys(Keys.RETURN)
time.sleep(1)

outbound_date = "/html/body/div[3]/div[1]/main/div/div[1]/section/div[1]/div/div/ul/li[1]/div/div/form/div[3]/div/div[1]/div/button"
driver.find_element(By.XPATH, outbound_date).click()
time.sleep(10)

elements = driver.find_elements(By.TAG_NAME, 'h3')

dates_available = []
for element in elements:
    dates_available.append(element.text)

if "July 2023" in dates_available:
    yagemail(subject="Easy Jet Dates",
             to="James.hinkley95@gmail.com", 
             content="Dates are available for the honeymoon, go book now!!")
    
else:
    print("Dates dates unavailable")
