from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
count = 1


def changeServerAndJoin():
    try:
        element = browser.find_element_by_id("server-dropdown-container")
        element.click()
        time.sleep(1)
        element = browser.find_element_by_id("server-option-3")
        element.click()
        element = browser.find_element_by_id("play-game-button")
        element.click()
    except:
        changeServerAndJoin()


def wait():
    WebDriverWait(browser, 900).until(
        EC.presence_of_element_located((By.ID, "server-dropdown-container"))
    )


browser.get('https://beta.modd.io/play/two-houses')
wait()
changeServerAndJoin()
while True:
    browser.execute_script("window.open('about:blank', 'tab{}');".format(count))
    browser.switch_to.window("tab{}".format(count))
    browser.get('https://beta.modd.io/play/two-houses')
    wait()
    changeServerAndJoin()
    count = count + 1
