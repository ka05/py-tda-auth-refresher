import atexit
import os
import sys
from shutil import which

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriverProvider:

    @staticmethod
    def get_docker_web_driver():

        # Running in docker container on linux
        # chrome driver install location
        # https://stackoverflow.com/questions/57243622/docker-google-cloud-chromedriver-executable-needs-to-be-in-path
        chrome_driver_path = '/usr/bin/chromedriver'

        # Fix for running in Docker container
        # https://github.com/wechaty/wechaty/issues/26
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920, 1200")

        driver = webdriver.Chrome(
            executable_path=chrome_driver_path,
            chrome_options=chrome_options)

        atexit.register(lambda: driver.quit())

        return driver

    @staticmethod
    def get_web_driver(use_headless_web_driver=False):

        options = webdriver.ChromeOptions()

        if sys.platform == 'darwin':
            # MacOS
            if os.path.exists("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
                options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
            elif os.path.exists("/Applications/Chrome.app/Contents/MacOS/Google Chrome"):
                options.binary_location = "/Applications/Chrome.app/Contents/MacOS/Google Chrome"
        elif 'linux' in sys.platform:
            # Linux
            options.binary_location = which('google-chrome') or \
                                      which('chrome') or \
                                      which('chromium')
        else:
            # Windows
            if os.path.exists('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'):
                options.binary_location = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
            elif os.path.exists('C:/Program Files/Google/Chrome/Application/chrome.exe'):
                options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

        chrome_driver_binary = which('chromedriver') or "/usr/local/bin/chromedriver"

        if use_headless_web_driver:
            options.add_argument('--headless')
            options.add_argument("--no-sandbox")
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--window-size=1920, 1200")

        return webdriver.Chrome(chrome_driver_binary, chrome_options=options)
