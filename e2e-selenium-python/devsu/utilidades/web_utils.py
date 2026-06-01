import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")

os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def wait_visible(wd, by, locator, timeout: int = 15):
    return WebDriverWait(wd, timeout).until(
        ec.visibility_of_element_located((by, locator))
    )


def wait_clickable(wd, by, locator, timeout: int = 15):
    return WebDriverWait(wd, timeout).until(
        ec.element_to_be_clickable((by, locator))
    )


def send_text(wd, by, locator, text, timeout: int = 15):
    element = wait_visible(wd, by, locator, timeout)
    element.clear()
    element.send_keys(text)
    return element


def click_element(wd, by, locator, timeout: int = 15):
    element = wait_clickable(wd, by, locator, timeout)
    element.click()
    return element


def take_screenshot(wd, file_name: str):
    screenshot_path = os.path.join(SCREENSHOT_DIR, file_name)
    wd.save_screenshot(screenshot_path)
    return screenshot_path