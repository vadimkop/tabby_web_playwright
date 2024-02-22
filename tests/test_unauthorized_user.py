import pytest
from qaseio.pytest import qase


@pytest.mark.prod
@qase.layer("e2e")
class TestUnauthorizedUser:

    @qase.id(0)
    @qase.title("Open Deal card from slider")
    @qase.description("Open Shared charter or Empty leg from Featured Private Jet Flights slider")
    @qase.severity("normal")
    def test_unauthorized_user(self, page_logged_out, base_url):
        page_logged_out.goto(base_url)
