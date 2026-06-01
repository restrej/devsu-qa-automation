from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def only_driver(driver: str = "chrome", headless: bool = False):
    if driver != "chrome":
        raise ValueError(f"Driver no soportado: {driver}")

    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    service = Service(ChromeDriverManager().install())
    wd = webdriver.Chrome(service=service, options=options)
    wd.implicitly_wait(5)

    return wd