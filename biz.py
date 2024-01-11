from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
import pyperclip
from bs4 import BeautifulSoup


# Auto update Chrome Driver
from webdriver_manager.chrome import ChromeDriverManager

# prevent Browser closing
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# remove unnecessary error msgs
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())

# 비즈한국에서 글 가져오기
bizkor_browser = webdriver.Chrome(service=service, options=chrome_options)
bizkor_browser.get("https://www.bizhankook.com/search/all/bk/1/12?q=%EC%9D%B4%EC%9D%80%EC%84%9C&searchDay=0")
bizkor_action = ActionChains(bizkor_browser)
bizkor_browser.implicitly_wait(5)

for x in range(0,7) :
    bizkor_browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    more_article_btn = bizkor_browser.find_element(By.ID, "listMore")
    more_article_btn.click()
    time.sleep(2)

# html 가져오기
html = bizkor_browser.page_source
soup = BeautifulSoup(html, "html.parser")
links = soup.select('body > div.wrap > div.bodyWrapper > div.subContens01.event > section.sub01 > div.list01 > article > a')
linkList = []

for link in links :
    article_number = link.attrs["href"].replace("/bk/article/", "") 
    linkList.append(article_number)

print(linkList)

# close window
# time.sleep(5)
# bizkor_browser.close()



