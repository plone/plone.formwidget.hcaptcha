# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.formwidget.hcaptcha.i18n import _
from z3c.form import validator
from zope.component import getMultiAdapter
from zope.schema import ValidationError


class WrongCaptchaCode(ValidationError):
    __doc__ = _(
        u"We are not yet sure whether you are human. Please try again."
    )


class HCaptchaValidator(validator.SimpleFieldValidator):
    def validate(self, value):
        super(HCaptchaValidator, self).validate(value)
        captcha = getMultiAdapter(
            (aq_inner(self.context), self.request), name="hcaptcha"
        )
        if not captcha.verify():
            raise WrongCaptchaCode
        return True
