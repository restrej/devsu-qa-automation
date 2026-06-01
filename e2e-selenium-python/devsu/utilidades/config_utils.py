import configparser
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def read_config_file(key: str, param: str, env: str = "local") -> str:
    config = configparser.ConfigParser()
    config_path = os.path.join(BASE_DIR, "config", f"config_{env}.ini")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"No existe el archivo de configuración: {config_path}")

    config.read(config_path)

    if not config.has_section(key):
        raise ValueError(f"No existe la sección [{key}] en {config_path}")

    if not config.has_option(key, param):
        raise ValueError(f"No existe el parámetro '{param}' en la sección [{key}]")

    return config.get(key, param)


def read_locator_web(key: str, param: str) -> str:
    config = configparser.ConfigParser()
    locator_path = os.path.join(BASE_DIR, "config", "web_locators.ini")

    if not os.path.exists(locator_path):
        raise FileNotFoundError(f"No existe el archivo de locators: {locator_path}")

    config.read(locator_path)

    if not config.has_section(key):
        raise ValueError(f"No existe la sección [{key}] en {locator_path}")

    if not config.has_option(key, param):
        raise ValueError(f"No existe el locator '{param}' en la sección [{key}]")

    return config.get(key, param)