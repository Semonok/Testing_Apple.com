import pytest
from Application.application import Application

@pytest.fixture(scope="session")# params=["Chrome", "Firefox", "IE"])
def driver(request):
    driver = Application("Chrome")
    driver.home_page()
    request.addfinalizer(driver.quit)
    return driver