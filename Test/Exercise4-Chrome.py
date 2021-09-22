from selenium import webdriver

ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument("--start-maximized")
ChromeOptions.add_argument("--disable-infobars")
ChromeOptions.add_argument("--disable-gpu")
ChromeOptions.add_argument("--disable-dev-shm-usage")
ChromeOptions.add_argument("--no-sandbox")

try:
    Chrome_driver = webdriver.Chrome(executable_path="/home/ubuntu/PycharmProjects/DevOpsLinux/Test/chromedriver", options=ChromeOptions)
    websiteName = "https://translate.google.com/"
    Chrome_driver.get(websiteName)
    TranslateTextArea = Chrome_driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea")
    TranslateTextArea.send_keys("שלח את זה")
    Chrome_driver.close()

except BaseException as BE:
    print(repr(BE))
