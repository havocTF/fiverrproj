from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--mute-audio")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
count = 1
othercount = 1


def changeServerAndJoin():
    try:
        element = browser.find_element_by_id("server-dropdown-container")  # looks for the dropdown for the servers
        element.click()
        element = browser.find_element_by_id(
            "server-option-2")  # looks for the eu- 2 option (will only choose the 4th option) CHANGE THIS IF YOU
        # WANT THE BOTS TO BE IN A DIFFERENT SERVER the server options start at 0 brazil would be 0 because eu is 5
        # down, it would be 4 because it starts at 0 right now its at 2 so it spawns on the third server option
        element.click()
        element = browser.find_element_by_id("play-game-button")  # looks for the play button
        element.click()
    except:
        changeServerAndJoin()


def close_response():
    try:
        browser.find_element_by_xpath(
            '//*[@id="refresh-modal"]/div/div/div[2]/button[2]').click()  # sometimes it says the server stopped
        # responding so this just closes that prompt
    except:
        pass


while count < 49:  # until theres 50 bots opens up 49 times
    browser.execute_script("window.open('about:blank', 'tab{}');".format(count))
    browser.switch_to.window("tab{}".format(count))  # these 2 lines just open new tab
    browser.get('https://beta.modd.io/play/two-houses')  # opens up url
    count = count + 1
    print("Bot ", count, " loaded")
print("finished loading starting to play")
while othercount < 49:
    browser.switch_to.window("tab{}".format(othercount))
    close_response()
    changeServerAndJoin()
    othercount = othercount + 1
    print("Bot ", othercount, " playing")
input("Finished botting... Please do not close this window or else it will stop communication with the server hoster "
      "and close all the bot tabs")
# wait like 2 - 3 mins before it acutally starts when it says bot 49 loaded it will start playing
