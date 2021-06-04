# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from plone.formwidget.hcaptcha.interfaces import IHCaptchaWidget
from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text
from zope.component import getMultiAdapter
from zope.interface import implementer_only

import zope.component
import zope.interface
import zope.schema.interfaces


@implementer_only(IHCaptchaWidget)
class HCaptchaWidget(text.TextWidget):
    maxlength = 7
    size = 8

    def captchaImage(self):
        self.captcha = getMultiAdapter(
            (aq_inner(self.context), self.request), name="captcha"
        )
        return self.captcha.image_tag()

    def captchaAudio(self):
        self.captcha = getMultiAdapter(
            (aq_inner(self.context), self.request), name="captcha"
        )
        return self.captcha.audio_url()


@zope.component.adapter(zope.schema.interfaces.IField, interfaces.IFormLayer)
@zope.interface.implementer(interfaces.IFieldWidget)
def HCaptchaFieldWidget(field, request):
    """IFieldWidget factory for CaptchaWidget."""
    return widget.FieldWidget(field, HCaptchaWidget(request))
