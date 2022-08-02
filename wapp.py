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
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument(r'--user-data-dir=C:/Users/ARMACAEDA/AppData/Local/Google/Chrome/User')
options.add_argument('--profile-directory=Default')
browser = webdriver.Chrome(options = options)

loc = "C:/Users/ARMACAEDA/Desktop/Auto.xlsx"
df = pd.read_excel(loc, engine = 'openpyxl')
for i in range(len(df)):
	name  =df.iloc[i,0]
	number = df.iloc[i,1]
	browser.execute_script("window.open('about:blank', 'tab2');")
	browser.switch_to.window("tab2")
	url = 'https://web.whatsapp.com/send?phone=91' + str(number)
	try:
		browser.get(url)
	except:
		continue
	time.sleep(15)
	try:
		msz_box = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
	except:
		continue
	msz = "Congratulations" + name + ".You have been selected as a test subject for my project on automation"
	msz_box.send_keys(msz)
	send_button = browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]/button/span')
	send_button.click()
	time.sleep(2)

browser.close()
print("JOB DONE!!")



/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[1]/div/div[3]/div/div/span
/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[3]/div/div[3]/div/div/span
/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[3]/ytcp-content-section/ytcp-video-section/ytcp-video-section-content/div/ytcp-video-row[2]/div/div[3]/div/div/span