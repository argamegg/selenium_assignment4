from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


def explicit_wait(driver, timeout: int = 12) -> WebDriverWait:
    return WebDriverWait(driver, timeout)


def fluent_wait(driver, timeout: int = 20, poll_frequency: float = 0.5) -> WebDriverWait:
    return WebDriverWait(
        driver,
        timeout,
        poll_frequency=poll_frequency,
        ignored_exceptions=(NoSuchElementException, StaleElementReferenceException),
    )


def wait_visible(driver, locator, timeout: int = 12):
    return explicit_wait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_clickable(driver, locator, timeout: int = 12):
    return explicit_wait(driver, timeout).until(EC.element_to_be_clickable(locator))
