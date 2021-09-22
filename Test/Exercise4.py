from selenium import webdriver

FireFoxOptions = webdriver.FirefoxOptions()
FireFoxOptions.add_argument("--headless")
# FireFoxOptions.add_argument("--profile")
# FireFoxOptions.add_argument("/home/ubuntu/.mozilla/firefox/98ve76xe.default")

try:
    FireFox_driver = webdriver.Firefox(executable_path="/home/ubuntu/PycharmProjects/DevOpsLinux/Test/geckodriver", firefox_options=FireFoxOptions)
    websiteName = "https://translate.google.com/"
    FireFox_driver.get(websiteName)
    TranslateTextArea = FireFox_driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea")
    TranslateTextArea.send_keys("שלח את זה")
    FireFox_driver.close()
    print("This is update version 2209")

except BaseException as BE:
    print(repr(BE))
