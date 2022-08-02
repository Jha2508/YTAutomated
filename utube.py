import openpyxl
import pandas as pd

import time
import ait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument(r'--user-data-dir=C:/Users/ARMACAEDA/AppData/Local/Google/Chrome/User Data')
options.add_argument('--profile-directory=Default')
browser = webdriver.Chrome(options = options)

loc = "C:/Users/ARMACAEDA/Desktop/Book3.xlsx"
df = pd.read_excel(loc, engine = 'openpyxl')


browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window("tab2")
url = 'https://studio.youtube.com/channel/UCS8936N-dNQBQePjhkMI-IA/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D'

try:
	browser.get(url)
	time.sleep(10)
except:
	pass

try:
	privacy_box = browser.find_element_by_xpath('/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[1]/div/div[3]/div/div/span')
except:
	pass
privacy_box.click()

try:
	share_btn = browser.find_element_by_xpath('/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/div[1]/ytcp-button/div')
except:
	pass
share_btn.click()
list_box = browser.find_element_by_xpath('/html/body/ytcp-private-video-sharing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[2]/div/ytcp-form-input-container/div[1]/div[2]/ytcp-chip-bar/div/input')
for j in range(len(df)):
	email = df.iloc[j,1]
	list_box.send_keys(str(email))
	time.sleep(2)
	list_box.send_keys(Keys.ENTER)
	time.sleep(5)

done_btn = browser.find_element_by_xpath('/html/body/ytcp-private-video-sharing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/div/ytcp-button[2]/div')
done_btn.click()
time.sleep(5)
save_btn = browser.find_element_by_xpath('/html/body/ytcp-video-visibility-edit-popup/tp-yt-paper-dialog/div/ytcp-button[2]/div')
save_btn.click()
time.sleep(10)
browser.close()
print("JOB DONE!!")
