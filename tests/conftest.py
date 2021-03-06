from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    # browser.config.hold_browser_open = True  # оставить браузер открытым
    # browser.config.wait_for_no_overlap_found_by_js = True  # ожидание появления всех элементов
    browser.config.timeout = 3
    browser.config.window_width = 1920
    browser.config.window_height = 1050