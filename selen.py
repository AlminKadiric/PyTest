from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from credentials import passwordCredentials, usernameCredentials
# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the specified URL
driver.get('https://www.it-akademija.com/')

# Wait for 3 seconds to allow the page to load
time.sleep(3)

# Find the element with the ID 'topRight'
topRight = driver.find_element(By.ID, "topRight")

# Find all anchor tags within the 'topRight' element
sviAElementi = topRight.find_elements(By.TAG_NAME, "a")

# Print the title of the page
print(driver.title)

# Wait for 10 seconds before closing the browser
time.sleep(10)

# Close the browser
driver.quit()

for aElement in sviAElementi:
    tekstAElement = aElement.text.lower().replace(" ","")
    if tekstAElement == 'dlplatforma':
        aElement.click()
        break
time.sleep()

username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")
submit = driver.find_element(By.ID,"submit")
username.send_keys(usernameCredentials())
password.send_keys(passwordCredentials())
submit.click()


time.sleep(4)

naviLinkovi = driver.find_elements(By.CLASS_NAME,"nav-link")


for link in naviLinkovi:
    tekstPojedinacnogLinka = naviLinkovi.text
    tekstPojedinacnogLinka = tekstPojedinacnogLinka.lower()
    if "podrska ucenju" in tekstPojedinacnogLinka:
        link.click()
        break
    
time.sleep(50)
startVideo = driver.find_elements(By.CLASS_NAME,"mejs_overlay-button")
startVideo.click()
time.sleep(10)

br = 0
while True:
    time.sleep()
    driver.get_screenshot_as_file(f"screenshot{br}.png")
    br+=1
    
    
time.sleep(100)