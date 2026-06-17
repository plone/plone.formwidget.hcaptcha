from plone.formwidget.hcaptcha import nohcaptcha
from urllib import parse

import json
import pytest


class FakeResponse:
    """Minimal stand-in for the object returned by ``urlopen``."""

    def __init__(self, payload: dict):
        self._data = json.dumps(payload).encode("utf-8")

    def read(self) -> bytes:
        return self._data

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *exc) -> bool:
        return False


@pytest.fixture
def patch_urlopen(monkeypatch):
    """Patch ``nohcaptcha.urlopen`` and capture the request it receives.

    :returns: A callable that installs a fake ``urlopen`` returning the given
        payload and returns a dict holding the captured ``Request``.
    """

    def factory(payload: dict) -> dict:
        captured = {}

        def _urlopen(request):
            captured["request"] = request
            return FakeResponse(payload)

        monkeypatch.setattr(nohcaptcha, "urlopen", _urlopen)
        return captured

    return factory


class TestHcaptchaResponse:
    def test_defaults(self):
        response = nohcaptcha.HcaptchaResponse(is_valid=True)
        assert response.is_valid is True
        assert response.error_code is None

    def test_error_code_stored(self):
        response = nohcaptcha.HcaptchaResponse(
            is_valid=False, error_code=["bad-request"]
        )
        assert response.is_valid is False
        assert response.error_code == ["bad-request"]

    def test_repr_and_str(self):
        response = nohcaptcha.HcaptchaResponse(is_valid=False, error_code="oops")
        expected = "Hcaptcha response: False oops"
        assert repr(response) == expected
        assert str(response) == expected


class TestDisplayHtml:
    def test_defaults(self):
        html = nohcaptcha.displayhtml("my-site-key")
        assert 'data-sitekey="my-site-key"' in html
        assert 'data-theme="light"' in html
        assert 'data-type="image"' in html
        assert 'data-size="normal"' in html
        assert "hl=&fallback=False&" in html

    def test_custom_values(self):
        html = nohcaptcha.displayhtml(
            "key",
            language="pt-br",
            theme="dark",
            fallback=True,
            d_type="audio",
            size="compact",
        )
        assert 'data-sitekey="key"' in html
        assert 'data-theme="dark"' in html
        assert 'data-type="audio"' in html
        assert 'data-size="compact"' in html
        assert "hl=pt-br&fallback=True&" in html


class TestSubmit:
    def test_empty_response_short_circuits(self, monkeypatch):
        # An empty field must not trigger a network call.
        def _fail(request):  # pragma: no cover - must never run
            raise AssertionError("urlopen should not be called for empty input")

        monkeypatch.setattr(nohcaptcha, "urlopen", _fail)

        response = nohcaptcha.submit("", "secret")
        assert response.is_valid is False
        assert response.error_code == "incorrect-captcha-sol"

    def test_successful_verification(self, patch_urlopen):
        patch_urlopen({"success": True})
        response = nohcaptcha.submit("token", "secret")
        assert response.is_valid is True
        assert response.error_code is None

    def test_failed_verification_returns_error_codes(self, patch_urlopen):
        patch_urlopen({"success": False, "error-codes": ["invalid-input-response"]})
        response = nohcaptcha.submit("token", "secret")
        assert response.is_valid is False
        assert response.error_code == ["invalid-input-response"]

    def test_failed_verification_without_error_codes(self, patch_urlopen):
        patch_urlopen({"success": False})
        response = nohcaptcha.submit("token", "secret")
        assert response.is_valid is False
        assert response.error_code == []

    def test_request_targets_default_server(self, patch_urlopen):
        captured = patch_urlopen({"success": True})
        nohcaptcha.submit("token", "secret")
        request = captured["request"]
        assert request.full_url == f"https://{nohcaptcha.VERIFY_SERVER}/siteverify"

    def test_request_uses_custom_verify_server(self, patch_urlopen):
        captured = patch_urlopen({"success": True})
        nohcaptcha.submit("token", "secret", verify_server="example.com")
        assert captured["request"].full_url == "https://example.com/siteverify"

    def test_request_encodes_secret_and_response(self, patch_urlopen):
        captured = patch_urlopen({"success": True})
        nohcaptcha.submit("the-token", "the-secret")
        sent = parse.parse_qs(captured["request"].data.decode("utf-8"))
        assert sent["secret"] == ["the-secret"]
        assert sent["response"] == ["the-token"]
