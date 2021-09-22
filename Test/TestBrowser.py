from selenium import webdriver
from time import sleep


FireFoxOptions = webdriver.FirefoxOptions()
FireFoxOptions.add_argument("--headless")
# FireFoxOptions.add_argument("--profile")
# FireFoxOptions.add_argument("/home/ubuntu/.mozilla/firefox/98ve76xe.default")

try:
    FireFox_driver = webdriver.Firefox(executable_path="/home/ubuntu/PycharmProjects/DevOpsLinux/Test/geckodriver", firefox_options=FireFoxOptions)
    websiteName = "https://www.google.com/"
    FireFox_driver.get(websiteName)
    sleep(5)
    FireFox_driver.close()

except BaseException as BE:
    print(repr(BE))