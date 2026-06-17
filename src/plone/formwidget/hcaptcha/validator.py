from Acquisition import aq_inner
from plone import api
from plone.formwidget.hcaptcha.browser.view import HcaptchaView
from plone.formwidget.hcaptcha.i18n import _
from z3c.form import validator
from zope.schema import ValidationError


class WrongCaptchaCode(ValidationError):
    __doc__ = _("We are not yet sure whether you are human. Please try again.")


class HCaptchaValidator(validator.SimpleFieldValidator):
    def validate(self, value: str) -> bool:
        super().validate(value)
        captcha: HcaptchaView = api.content.get_view(
            name="hcaptcha", context=aq_inner(self.context), request=self.request
        )
        if not captcha.verify():
            raise WrongCaptchaCode
        return True
