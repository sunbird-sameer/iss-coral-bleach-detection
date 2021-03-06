from selenium import webdriver
from time import sleep
import iss_location

def main():

    driver = webdriver.Firefox()
    driver.get("https://iss-live.github.io")

    sleep(30)

    driver.get_screenshot_as_file(str(iss_location.lat() + '_' + iss_location.long() + '.png'))
    driver.quit()

if __name__ == "main":
    main()
