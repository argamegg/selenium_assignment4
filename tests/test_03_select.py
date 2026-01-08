from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from src.helpers import open_search
from src.waits import explicit_wait


def test_select_on_amazon(driver):
    open_search(driver)

    wait = explicit_wait(driver, 15)

    sort_select_el = wait.until(
        EC.presence_of_element_located((By.ID, "s-result-sort-select"))
    )

    sort_select = Select(sort_select_el)

    # ✅ Select class: выбираем сортировку
    sort_select.select_by_visible_text("Price: Low to High")

    selected = sort_select.first_selected_option.text
    assert "Low to High" in selected
