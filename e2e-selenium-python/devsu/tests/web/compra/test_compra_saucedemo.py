import pytest

from selenium.webdriver.common.by import By

from devsu.utilidades.config_utils import read_config_file, read_locator_web
from devsu.utilidades.logs_utils import log
from devsu.utilidades.process_utils import only_driver
from devsu.utilidades.web_utils import (click_element, send_text, wait_visible, take_screenshot,
)


class TestData:
    url = read_config_file("WEB", "main_url")
    browser = read_config_file("WEB", "browser")
    headless = read_config_file("WEB", "headless").lower() == "true"

    test_user = read_config_file("USERS", "standard_user")
    test_pass = read_config_file("USERS", "standard_pass")

    first_name = read_config_file("COMPRA", "first_name")
    last_name = read_config_file("COMPRA", "last_name")
    postal_code = read_config_file("COMPRA", "postal_code")

    username_loc = read_locator_web("LOGIN", "username")
    password_loc = read_locator_web("LOGIN", "password")
    btn_login_loc = read_locator_web("LOGIN", "btn_login")

    product_backpack_loc = read_locator_web("PRODUCTOS", "product_backpack")
    product_bike_light_loc = read_locator_web("PRODUCTOS", "product_bike_light")
    shopping_cart_loc = read_locator_web("PRODUCTOS", "shopping_cart")

    btn_checkout_loc = read_locator_web("CARRITO", "btn_checkout")

    first_name_loc = read_locator_web("COMPRA", "first_name")
    last_name_loc = read_locator_web("COMPRA", "last_name")
    postal_code_loc = read_locator_web("COMPRA", "postal_code")
    btn_continue_loc = read_locator_web("COMPRA", "btn_continue")
    btn_finish_loc = read_locator_web("COMPRA", "btn_finish")
    confirmation_message_loc = read_locator_web("COMPRA", "confirmation_message")

    wd = None
    error_flow_desc = None


def setup_class():
    try:
        log.info("Precondición: iniciando navegador")
        TestData.wd = only_driver(driver=TestData.browser, headless=TestData.headless)
        TestData.wd.get(TestData.url)
        return False

    except Exception as err:
        TestData.error_flow_desc = f"Error iniciando navegador: {err}"
        log.error(TestData.error_flow_desc)
        return True


@pytest.mark.e2e
@pytest.mark.compra
@pytest.mark.smoke
def test_compra_saucedemo():
    log.info("El objetivo del test es validar el flujo E2E de compra en SauceDemo")

    if setup_class():
        pytest.skip(reason=TestData.error_flow_desc)

    try:
        log.info("Ingresando usuario estándar")
        send_text(TestData.wd, By.ID, TestData.username_loc, TestData.test_user)

        log.info("Ingresando contraseña")
        send_text(TestData.wd, By.ID, TestData.password_loc, TestData.test_pass)

        log.info("Haciendo click en login")
        click_element(TestData.wd, By.ID, TestData.btn_login_loc)

        log.info("Agregando producto Sauce Labs Backpack al carrito")
        click_element(TestData.wd, By.ID, TestData.product_backpack_loc)

        log.info("Agregando producto Sauce Labs Bike Light al carrito")
        click_element(TestData.wd, By.ID, TestData.product_bike_light_loc)

        log.info("Visualizando carrito")
        click_element(TestData.wd, By.ID, TestData.shopping_cart_loc)

        log.info("Iniciando compra")
        click_element(TestData.wd, By.ID, TestData.btn_checkout_loc)

        log.info("Completando formulario de compra")
        send_text(TestData.wd, By.ID, TestData.first_name_loc, TestData.first_name)
        send_text(TestData.wd, By.ID, TestData.last_name_loc, TestData.last_name)
        send_text(TestData.wd, By.ID, TestData.postal_code_loc, TestData.postal_code)

        log.info("Continuando compra")
        click_element(TestData.wd, By.ID, TestData.btn_continue_loc)

        log.info("Finalizando compra")
        click_element(TestData.wd, By.ID, TestData.btn_finish_loc)

        log.info("Validando mensaje de confirmación")
        confirmation = wait_visible(TestData.wd, By.CLASS_NAME, TestData.confirmation_message_loc
        )

        assert confirmation.is_displayed()
        assert confirmation.text.strip().upper() == "THANK YOU FOR YOUR ORDER!"

        log.info("Flujo E2E de compra finalizado exitosamente")

    except Exception as err:
        take_screenshot(TestData.wd, "error_test_compra_saucedemo.png")
        pytest.fail(f"Falló el flujo E2E de compra: {err}")

def teardown_module():
    try:
        if TestData.wd:
            TestData.wd.quit()
            log.info("Postcondición: navegador cerrado correctamente")

    except Exception as err:
        log.error(f"Error cerrando navegador: {err}")