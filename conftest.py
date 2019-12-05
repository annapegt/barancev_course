import pytest
from fixture.application import Application
# conftest contains a common method for all tests due to containing fixture


@pytest.fixture(scope="session")  # one browser will be used for all tests
# fixture initialization
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)  # needed for fixture destroying
    return fixture
