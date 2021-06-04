# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from z3c.form import validator
from zope.component import getMultiAdapter
from zope.i18nmessageid import MessageFactory
from zope.schema import ValidationError


_ = MessageFactory("plone.formwidget.hcaptcha")


class WrongCaptchaCode(ValidationError):
    __doc__ = _(u"The code you entered was wrong, please enter the new one.")


class HCaptchaValidator(validator.SimpleFieldValidator):
    def validate(self, value):
        super(HCaptchaValidator, self).validate(value)
        captcha = getMultiAdapter(
            (aq_inner(self.context), self.request), name="hcaptcha"
        )
        if not captcha.verify():
            raise WrongCaptchaCode
        return True
