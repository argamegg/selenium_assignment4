from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.helpers import open_search
from src.waits import explicit_wait, fluent_wait


def test_waits_on_amazon(driver):
    open_search(driver)

    # ✅ Explicit wait: ждём контейнер результатов
    explicit_wait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
    )

    # ✅ Fluent wait: ждём пока появится хотя бы 1 карточка товара
    fw = fluent_wait(driver, timeout=20, poll_frequency=0.5)
    fw.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")) > 0)

    assert "amazon.com" in driver.current_url.lower()
