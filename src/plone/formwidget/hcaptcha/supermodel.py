# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.formwidget.hcaptcha.validator import WrongCaptchaCode
from plone.supermodel.exportimport import ObjectHandler
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.interface import Interface
from zope.interface import implementer
from zope.schema._bootstrapinterfaces import IFromUnicode
from zope.schema import Field
from zope.schema.interfaces import IField


class ICaptchaField(IField):
    """Field containing a captcha."""

@adapter(Interface, IFromUnicode)
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
            (aq_inner(self.context), self.context.REQUEST), name="hcaptcha"
        )
        if not captcha.verify():
            raise WrongCaptchaCode
        return True


CaptchaHandler = ObjectHandler(CaptchaField)
