from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
CHROME_DRIVER_PATH = "/home/vishal/Downloads/chromedriver"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

playlist_url = input("enter the link of the youtube playlist\n")
driver.get(playlist_url)

time.sleep(10)
for _ in range(10):
    time.sleep(5)
    label = driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a')
    label.send_keys(Keys.PAGE_DOWN)
time.sleep(15)
mins = []
secs = []
for tag in driver.find_elements_by_css_selector('ytd-thumbnail-overlay-time-status-renderer span'):
    mins.append(float(tag.text.split(':')[0]))
    secs.append(float(tag.text.split(':')[1]))
    
total_hrs = (sum(mins) + (sum(secs)/60))/60
print(f"Total duration of the playlist is round({total_hrs},2) hrs")
