from plone.formwidget.hcaptcha.browser import view as view_module
from plone.formwidget.hcaptcha.browser.view import HcaptchaInfoAnnotation
from plone.formwidget.hcaptcha.browser.view import HcaptchaView
from plone.formwidget.hcaptcha.browser.view import IHcaptchaInfo
from plone.formwidget.hcaptcha.nohcaptcha import HcaptchaResponse

import pytest


class TestHcaptchaInfoAnnotation:
    def test_defaults(self):
        info = HcaptchaInfoAnnotation()
        assert info.error is None
        assert info.verified is False


class TestHcaptchaView:
    @pytest.fixture(autouse=True)
    def _setup(self, portal, http_request):
        self.portal = portal
        self.request = http_request
        self.view = HcaptchaView(portal, http_request)
        # Start from a known, empty configuration.
        self.view.settings.public_key = ""
        self.view.settings.private_key = ""

    def test_image_tag_without_public_key(self):
        tag = self.view.image_tag()
        assert "No hcaptcha public key" in tag
        assert "@@hcaptcha-settings" in tag

    def test_image_tag_with_public_key(self):
        self.view.settings.public_key = "my-site-key"
        tag = self.view.image_tag()
        assert 'data-sitekey="my-site-key"' in tag
        assert 'data-theme="light"' in tag

    def test_image_tag_uses_request_language(self):
        self.view.settings.public_key = "my-site-key"
        self.request["LANGUAGE"] = "pt-br"
        assert "hl=pt-br&" in self.view.image_tag()

    def test_audio_url_is_none(self):
        assert self.view.audio_url() is None

    def test_external_is_true(self):
        assert self.view.external is True

    def test_verify_without_private_key_raises(self):
        with pytest.raises(ValueError, match="No hcaptcha private key"):
            self.view.verify()

    def test_verify_returns_true_when_already_verified(self, monkeypatch):
        info = IHcaptchaInfo(self.request)
        info.verified = True

        def _fail(*args, **kwargs):  # pragma: no cover - must never run
            raise AssertionError("submit should not be called when cached")

        monkeypatch.setattr(view_module, "submit", _fail)
        assert self.view.verify() is True

    def test_verify_success_marks_request_verified(self, monkeypatch):
        self.view.settings.private_key = "secret"
        self.request.form["h-captcha-response"] = "token"
        monkeypatch.setattr(
            view_module, "submit", lambda *a, **kw: HcaptchaResponse(is_valid=True)
        )

        assert self.view.verify() is True
        info = IHcaptchaInfo(self.request)
        assert info.verified is True
        assert info.error is None

    def test_verify_failure_records_error(self, monkeypatch):
        self.view.settings.private_key = "secret"
        self.request.form["h-captcha-response"] = "token"
        monkeypatch.setattr(
            view_module,
            "submit",
            lambda *a, **kw: HcaptchaResponse(
                is_valid=False, error_code=["invalid-input-response"]
            ),
        )

        assert self.view.verify() is False
        info = IHcaptchaInfo(self.request)
        assert info.verified is False
        assert info.error == ["invalid-input-response"]
