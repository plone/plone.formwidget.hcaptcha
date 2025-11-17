from Acquisition import aq_inner
from plone.formwidget.hcaptcha.widget import HCaptchaFieldWidget
from plone.z3cform.layout import wrap_form
from z3c.form import button
from z3c.form import field
from z3c.form import form
from zope import interface
from zope import schema
from zope.component import getMultiAdapter

import logging


logger = logging.getLogger(__name__)


class IHCaptchaForm(interface.Interface):
    subject = schema.TextLine(title="Subject", description="", required=True)

    captcha = schema.TextLine(title="HCaptcha", description="", required=False)


class HCaptcha:
    subject = ""
    captcha = ""

    def __init__(self, context):
        self.context = context


class BaseForm(form.Form):
    """example captcha form"""

    fields = field.Fields(IHCaptchaForm)
    fields["captcha"].widgetFactory = HCaptchaFieldWidget

    @button.buttonAndHandler("Save")
    def handleApply(self, action):
        data, errors = self.extractData()
        captcha = getMultiAdapter(
            (aq_inner(self.context), self.request), name="hcaptcha"
        )
        if captcha.verify():
            logger.info("HCaptcha validation passed.")
        else:
            logger.info("The code you entered was wrong, please enter the new one.")
        return


HCaptchaForm = wrap_form(BaseForm)
