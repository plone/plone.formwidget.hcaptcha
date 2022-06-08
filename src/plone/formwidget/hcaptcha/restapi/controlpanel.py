# -*- coding: utf-8 -*-
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.interface import Interface
from zope.component import adapter
from plone.formwidget.hcaptcha.interfaces import IHCaptchaSettings
from zope.i18nmessageid import MessageFactory

_ = MessageFactory("plone.formwidget.hcaptcha")


@adapter(Interface, Interface)
class HCaptchaConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IHCaptchaSettings
    configlet_id = "hcaptcha"
    configlet_category_id = "Products"
    title = _("HCaptcha Control Panel")
    group = ""
    schema_prefix = "plone.formwidget.hcaptcha.interfaces.IHCaptchaSettings"
