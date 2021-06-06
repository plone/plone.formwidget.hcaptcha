# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from plone.formwidget.hcaptcha.interfaces import _
from plone.formwidget.hcaptcha.interfaces import IHCaptchaSettings


class HCaptchaSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IHCaptchaSettings
    label = _(u"HCaptcha settings")
    description = _(
        u"In order to use HCaptcha on your Plone site, go to "
        u"https://www.hcaptcha.com/ to create an account and "
        u"to receive your private/secret and public/site key. Then configure them at "
        u"https://host/path/to/site/@@hcaptcha-settings. If you don't want to "
        u"rely on an external service for captcha, you might want to consider "
        u"using plone.formwidget.captcha instead."
    )

    def updateFields(self):
        super(HCaptchaSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(HCaptchaSettingsEditForm, self).updateWidgets()


class HCaptchaSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = HCaptchaSettingsEditForm
