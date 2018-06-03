import pytest
from Application.application import Application

@pytest.fixture
def driver(request):
    driver = Application()
    driver.home_page()
    request.addfinalizer(driver.quit)
    return driver
