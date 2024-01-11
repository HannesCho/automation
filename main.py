from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui
import pyperclip
import requests
from bs4 import BeautifulSoup

# Auto update Chrome Driver
from webdriver_manager.chrome import ChromeDriverManager

# prevent Browser closing
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# remove unnecessary error msgs
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
brunch_browser = webdriver.Chrome(service=service, options=chrome_options)
# bizkor_browser = webdriver.Chrome(service=service, options=chrome_options)


# move to webpage
brunch_browser.get("https://brunch.co.kr/")
# bizkor_browser.get("https://www.bizhankook.com/search/all/bk/1/12?q=%EC%9D%B4%EC%9D%80%EC%84%9C&searchDay=0")
brunch_browser.implicitly_wait(3)

# action chains
brunch_action = ActionChains(brunch_browser)
# bizkor_action = ActionChains(bizkor_browser)

#login to brunch
login_btn = brunch_browser.find_element(By.ID, "topStartBrunchButton")
login_btn.click()
brunch_browser.implicitly_wait(3)
kakao_login_btn = brunch_browser.find_element(By.ID, "kakaoLogin")
kakao_login_btn.click()
time.sleep(3)
id_input = brunch_browser.find_element(By.ID, "loginKey--1")
id_input.click()
pyperclip.copy("id")
pyautogui.keyDown("command")
pyautogui.press("v")
pyautogui.keyUp("command")
time.sleep(1)

pw_input = brunch_browser.find_element(By.ID, "password--2")
pw_input.click()
pyperclip.copy("pw")
pyautogui.hotkey("command", "v")
time.sleep(1)

brunch_browser.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]').click()

# 글쓰기 버튼
time.sleep(2)
brunch_browser.get("https://brunch.co.kr/write")

#최신 글 찾기/ 제목 복사
# brunch_browser.implicitly_wait(2)
# menu_btn = brunch_browser.find_element(By.ID, "btnServiceMenu")
# menu_btn.click()
# time.sleep(1)
# fac_btn = brunch_browser.find_element(By.XPATH, '//*[@id="wrapSideMenu"]/main/div[1]/a[1]')
# fac_btn.click()

# first_title = brunch_browser.find_element(By.CLASS_NAME, "tit_subject").get_attribute("innerHTML").strip()


# 비즈한국에서 글 가져오기
# 기사 url
#25851
def get_article(number) : 

    url = f"https://www.bizhankook.com/bk/article/{number}"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    title = soup.select('body > div.wrap > div.bodyWrapper > div.subContens01.view > div.sub01 > div.viewTitWrap > h2')[0].text.replace("[유럽스타트업열전]", "").strip()
    subtitle = soup.select('body > div.wrap > div.bodyWrapper > div.subContens01.view > div.sub01 > div.viewTitWrap > p')[0].text

    # 내용 붙여넣기
    brunch_browser.find_element(By.CLASS_NAME,"cover_title").click()
    pyperclip.copy(title)
    pyautogui.hotkey("command", "v")

    brunch_browser.find_element(By.CLASS_NAME,"cover_sub_title").click()
    pyperclip.copy(subtitle)
    pyautogui.hotkey("command", "v")


    # 비즈한국에서 글 가져오기
    brunch_browser.execute_script('window.open("about:blank", "_blank");')
    tabs = brunch_browser.window_handles
    brunch_browser.switch_to.window(tabs[1])
    brunch_browser.get(url)
    brunch_browser.implicitly_wait(1)

    ad_btn = brunch_browser.find_element(By.CLASS_NAME, "__staxadclose")
    ad_btn.click()
    time.sleep(1)
    start_article = brunch_browser.find_element(By.CSS_SELECTOR,".viewContWrap > p:nth-child(1)")
    end_article = brunch_browser.find_element(By.CSS_SELECTOR,".viewContWrap > p:nth-last-child(13)")
    # bizkor_action.drag_and_drop(start_article, end_article).key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()
    brunch_action.click(start_article).key_down(Keys.SHIFT).click(end_article).key_up(Keys.SHIFT).key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).perform()
    time.sleep(1)
    brunch_browser.close()

    #복사된 글 붙여넣기
    brunch_browser.switch_to.window(tabs[0])
    time.sleep(1)
    article_box = brunch_browser.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]/p/br')
    brunch_action.click(article_box).send_keys(Keys.TAB).pause(1).send_keys(Keys.TAB).key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()
    time.sleep(5)
    pyperclip.copy("[비즈한국] ")
    pyautogui.hotkey("command", "f")
    pyautogui.hotkey("command", "v")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("esc")
    time.sleep(1)
    pyautogui.keyDown("shift")
    pyautogui.press("home")
    pyautogui.keyUp("shift")
    pyautogui.press("delete")
    pyautogui.press("delete")

    pyautogui.hotkey("command", "down")
    pyautogui.press("enter")
    pyperclip.copy('*이 글은 <비즈한국>의 [유럽스타트업열전]에 기고하였습니다.')
    pyautogui.hotkey("command", "v")

    brunch_browser.find_element(By.XPATH, '//*[@id="side--bttn--wrapper-1"]/div[2]/button[3]').click()
    brunch_browser.find_element(By.XPATH, '//*[@id="side--bttn--wrapper-1"]/div[3]/ul/li[1]/button').click()

    pyperclip.copy('이은서')
    pyautogui.hotkey("command", "v")

    pyautogui.press("enter")
    pyperclip.copy('eunseo.yi@123factory.de')
    pyautogui.hotkey("command", "v")

    # 글 저장
    brunch_browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/span/button[1]').click()

    # 다시 글쓰기로 돌아가기
    brunch_browser.implicitly_wait(5)
    time.sleep(5)
    brunch_browser.get("https://brunch.co.kr/write")
    brunch_browser.implicitly_wait(5)
    # time.sleep(5)

articles = ['25698', '25641', '25612', '25558', '25539', '25507', '25479', '25444', '25399', '25363', '25330', '25301', '25267', '25237', '25198', '25164', '25129', '25092', '25062', '25020', '24985', '24952', '24914', '24878', '24840', '24815', '24768', '24734', '24689', '24661', '24612', '24566', '24535', '24498', '24453', '24417', '24389', '24359', '24319', '24284', '24253', '24220', '24183', '24126', '24076', '24038', '24002', '23956', '23917', '23881', '23843', '23811', '23762', '23728', '23695', '23662', '23630', '23593', '23560', '23530', '23491', '23457', '23423', '23389', '23361', '23316', '23289', '23256', '23239', '23202', '23177', '23143', '23110', '23088', '23039', '23000', '22966', '22931', '22886', '22858', '22824', '22787']

for article in articles : 
    get_article(article)


# brunch_action.click(body).key_down(Keys.COMMAND).send_keys("f").key_up(Keys.COMMAND).pause(1).send_keys("[비즈한국] ").pause(1).send_keys(Keys.ENTER).perform()

#로그아웃
# brunch_browser.implicitly_wait(2)
# menu_btn = brunch_browser.find_element(By.ID, "btnServiceMenu")
# menu_btn.click()
# time.sleep(1)
# logout_btn = brunch_browser.find_element(By.ID, "sideMenuLogoutButton")
# logout_btn.click()
# brunch_browser.implicitly_wait(2)
# kakao_logout_btn = brunch_browser.find_element(By.NAME, "logout_with_kakao")
# kakao_logout_btn.click()

time.sleep(4)
brunch_browser.close()
