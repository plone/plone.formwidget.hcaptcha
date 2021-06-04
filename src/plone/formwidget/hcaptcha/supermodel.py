# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.formwidget.recaptcha.validator import WrongCaptchaCode
from plone.supermodel.exportimport import ObjectHandler
from zope.component import getMultiAdapter
from zope.interface import implementer
from zope.schema import Field
from zope.schema.interfaces import IField


class ICaptchaField(IField):
    """Field containing a captcha."""


@implementer(ICaptchaField)
class CaptchaField(Field):
    def get(self, object):
        # Captcha field should never save anything in the object itself
        return None

    def set(self, object, value):
        # Captcha field should never save anything in the object itself
        return None

    def validate(self, value):
        captcha = getMultiAdapter(
            (aq_inner(self.context), self.context.REQUEST), name="recaptcha"
        )
        if not captcha.verify():
            raise WrongCaptchaCode
        return True


CaptchaHandler = ObjectHandler(CaptchaField)
