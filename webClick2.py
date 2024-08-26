from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)

# 웹페이지가 로드될 때까지 2초를 대기
driver.implicitly_wait(time_to_wait=2)

driver.get(url='https://www.privacy.go.kr')
time.sleep(30)

print("시작")

# 팝업으로 이동
driver.switch_to.window(driver.window_handles[-1]) # 최근에 새로 뜬 창
time.sleep(3)

# 강의보기 ( 여기를 바꿔줘야 할듯 싶다)
#driver.find_element(By.XPATH, '/html/body/form/section/div/div[2]/div[2]/a').click()
#time.sleep(10)

while True:
    nextBtn = driver.find_element(By.ID,'nextBtn')
    try:
        #driver.switch_to.window(driver.window_handles[-1]) # 최근에 새로 뜬 창
        #time.sleep(3)
        #driver.find_element(By.XPATH, '/html/body/div/div[1]/div[6]/div[15]').click()
        #driver.find_element_by_id('nextBtn').click()
        nextBtn.click()
    except:
        print("no tags")

    time.sleep(30)
