import atexit


class WebDriverProvider:

    @staticmethod
    def get_docker_web_driver():
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

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
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager

        chrome_driver_binary_path = ChromeDriverManager().install()

        chrome_options = webdriver.ChromeOptions()

        if use_headless_web_driver:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument("--window-size=1920, 1200")

        driver = webdriver.Chrome(chrome_driver_binary_path, chrome_options=chrome_options)

        atexit.register(lambda: driver.quit())

        return driver
