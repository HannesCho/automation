from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui

# Auto update Chrome Driver
from webdriver_manager.chrome import ChromeDriverManager

# prevent Browser closing
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# remove unnecessary error msgs
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())

url = "https://www.bizhankook.com/bk/article/25851"

bizkor_browser = webdriver.Chrome(service=service, options=chrome_options)
bizkor_browser.get(url)
bizkor_action = ActionChains(bizkor_browser)
bizkor_browser.implicitly_wait(1)

bizkor_action.key_down(Keys.COMMAND).send_keys("f").key_up(Keys.COMMAND).pause(3).send_keys("[비즈한국] ").pause(1).send_keys(Keys.ENTER).perform()
# ad_btn = bizkor_browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]")
# ad_btn.click()
# time.sleep(1)
# start_article = bizkor_browser.find_element(By.CSS_SELECTOR,".viewContWrap > p:nth-child(2)")
# end_article = bizkor_browser.find_element(By.CSS_SELECTOR,".viewContWrap > p:nth-last-child(13)")
# # bizkor_action.drag_and_drop(start_article, end_article).key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()
# bizkor_action.click(start_article).key_down(Keys.SHIFT).click(end_article).key_up(Keys.SHIFT).key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()
time.sleep(5)
bizkor_browser.close()