# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from plone.formwidget.recaptcha.interfaces import _
from plone.formwidget.recaptcha.interfaces import IHCaptchaSettings


class ReCaptchaSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IHCaptchaSettings
    label = _(u"HCaptcha settings")
    description = _(
        u"In order to use HCaptcha on your Plone site, go to "
        u"https://www.hcaptcha.com/ to create an account and "
        u"to receive your private and public key. Then configure them at "
        u"https://host/path/to/site/@@recaptcha-settings. If you don't want to "
        u"rely on an external service for captcha, you might want to consider "
        u"using plone.formwidget.captcha instead."
    )

    def updateFields(self):
        super(ReCaptchaSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(ReCaptchaSettingsEditForm, self).updateWidgets()


class ReCaptchaSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = ReCaptchaSettingsEditForm
