from plone.formwidget.hcaptcha.supermodel import CaptchaField


class TestCaptchaField:
    """The captcha field is transient: it never persists anything."""

    def test_get_returns_none(self):
        field = CaptchaField()
        assert field.get(object()) is None

    def test_set_returns_none(self):
        field = CaptchaField()
        assert field.set(object(), "any-value") is None
