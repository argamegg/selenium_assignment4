AMAZON_SEARCH_URL = "https://www.amazon.com/s?k=laptop"


class AmazonLocators:
    SEARCH_RESULTS_CONTAINER = ("css selector", "div.s-main-slot")
    SORT_SELECT = ("id", "s-result-sort-select")
    FIRST_RESULT = ("css selector", "div.s-main-slot div[data-component-type='s-search-result']")


def open_search(driver):
    driver.get(AMAZON_SEARCH_URL)
