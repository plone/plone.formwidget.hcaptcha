from AccessControl import Unauthorized
from AccessControl.users import nobody
from plone import api

import pytest


class TestControlPanel:
    @pytest.fixture(autouse=True)
    def _setup(self, http_request, portal):
        self.portal = portal
        self.request = http_request

    def test_controlpanel_view(self):
        view = api.content.get_view(
            name="hcaptcha-settings", context=self.portal, request=self.request
        )
        assert view()

    def test_controlpanel_view_protected(self):

        with api.env.adopt_user(user=nobody), pytest.raises(Unauthorized) as exc:
            self.portal.restrictedTraverse("@@hcaptcha-settings")
        assert "Unauthorized('@@hcaptcha-settings'" in str(exc)

    def test_in_controlpanel(self):
        portal_controlpanel = api.portal.get_tool("portal_controlpanel")
        cp_ids = [a.getAction(self)["id"] for a in portal_controlpanel.listActions()]
        assert "hcaptcha" in cp_ids


class TestControlPanelAPI:
    configlet_id: str = "hcaptcha"

    @pytest.fixture(autouse=True)
    def _setup(self, functional_portal, manager_request):
        self.portal = functional_portal
        self.api_session = manager_request
        self.configlet_url = (
            f"{self.portal.absolute_url()}/@controlpanels/{self.configlet_id}"
        )

    def test_controlpanels_endpoint(self):
        response = self.api_session.get("/@controlpanels")
        data = response.json()
        configlets = {cp["@id"]: cp for cp in data}
        assert self.configlet_url in configlets
        configlet = configlets[self.configlet_url]
        assert isinstance(configlet, dict)
        assert configlet["title"] == "HCaptcha"

    @pytest.mark.parametrize(
        "key,type_",
        (
            ("@id", str),
            ("data", dict),
            ("group", str),
            ("schema", dict),
            ("title", str),
        ),
    )
    def test_serialization(self, key, type_):
        response = self.api_session.get(f"/@controlpanels/{self.configlet_id}")
        data = response.json()
        assert key in data
        assert isinstance(data[key], type_)
