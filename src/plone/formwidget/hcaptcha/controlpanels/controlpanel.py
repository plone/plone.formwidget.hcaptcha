from plone.app.registry.browser import controlpanel
from plone.formwidget.hcaptcha.i18n import _
from plone.formwidget.hcaptcha.interfaces import IHCaptchaLayer
from plone.formwidget.hcaptcha.interfaces import IHCaptchaSettings
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface


class HCaptchaSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IHCaptchaSettings
    label = _("HCaptcha settings")
    description = _(
        "In order to use HCaptcha on your Plone site, go to"
        " https://www.hcaptcha.com/ to create an account and to receive your"
        " private/secret and public/site key. Then configure them at"
        " https://host/path/to/site/@@hcaptcha-settings. If you don't want to"
        " rely on an external service for captcha, you might want to consider"
        " using plone.formwidget.captcha instead."
    )

    def updateFields(self):
        super().updateFields()

    def updateWidgets(self):
        super().updateWidgets()


class HCaptchaSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = HCaptchaSettingsEditForm


@adapter(Interface, IHCaptchaLayer)
class HCaptchaConfigletPanel(RegistryConfigletPanel):
    """REST API control-panel endpoint for HCaptcha settings."""

    schema = IHCaptchaSettings
    configlet_id = "hcaptcha"
    configlet_category_id = "Products"
    title = _("HCaptcha Control Panel")
    group = ""
    schema_prefix = "plone.formwidget.hcaptcha.interfaces.IHCaptchaSettings"
