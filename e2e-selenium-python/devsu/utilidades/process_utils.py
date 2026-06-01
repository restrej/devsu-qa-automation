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
    options.add_argument("--disable-popup-blocking")

    # Evita popups de Chrome relacionados con contraseñas guardadas o comprometidas
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2
    }

    options.add_experimental_option("prefs", prefs)

    # Oculta mensajes de automatización innecesarios
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    service = Service(ChromeDriverManager().install())

    wd = webdriver.Chrome(service=service, options=options)
    wd.implicitly_wait(5)

    return wd