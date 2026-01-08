from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from src.helpers import open_search
from src.waits import explicit_wait


def test_actions_on_amazon(driver):
    # Открываем страницу (у тебя open_search уже ведёт на /s?k=laptop)
    open_search(driver)

    wait = explicit_wait(driver, 20)

    # Ждём поисковую строку (она стабильнее, чем карточки товаров)
    search_box = wait.until(
        EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
    )

    # ActionChains: клик -> выделить всё -> стереть -> ввести запрос -> Enter
    actions = ActionChains(driver)
    actions.move_to_element(search_box).click().pause(0.2)
    actions.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND)  # mac: Cmd+A
    actions.send_keys(Keys.BACKSPACE)
    actions.send_keys("headphones")
    actions.send_keys(Keys.ENTER)
    actions.perform()

    # Ждём, что открылись результаты нового поиска
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot")))

    # Проверка, что запрос изменился в URL
    assert "k=headphones" in driver.current_url
