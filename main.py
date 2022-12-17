from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver = "/usr/src/chrome/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path=chromedriver,options=chrome_options)
driver.get("https://www.smpa.go.kr/user/nd54882.do")
gotit=driver.find_element(By.XPATH, '//*[@id="subContents"]/div/div[2]/table/tbody/tr[1]/td[2]/a')
gotit.click()
time.sleep(5)
downloadpdf= driver.find_element(By.XPATH, '//*[@id="subContents"]/div/div[2]/table/tbody/tr[3]/td/a[3]')
downloadpdf.click()

driver.quit()