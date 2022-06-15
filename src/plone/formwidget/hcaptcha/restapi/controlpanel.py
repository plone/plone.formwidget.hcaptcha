# -*- coding: utf-8 -*-
from plone.formwidget.hcaptcha.i18n import _
from plone.formwidget.hcaptcha.interfaces import IHCaptchaSettings
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface


@adapter(Interface, Interface)
class HCaptchaConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IHCaptchaSettings
    configlet_id = "hcaptcha"
    configlet_category_id = "Products"
    title = _("HCaptcha Control Panel")
    group = ""
    schema_prefix = "plone.formwidget.hcaptcha.interfaces.IHCaptchaSettings"
