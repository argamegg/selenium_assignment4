import os
import pytest
from src.driver_factory import create_driver


@pytest.fixture
def driver():
    headless = os.getenv("HEADLESS", "0") == "1"
    d = create_driver(headless=headless, implicit_wait_seconds=7)
    yield d
    d.quit()
