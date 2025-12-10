from plone.formwidget.hcaptcha.i18n import _
from z3c.form import interfaces
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


display_themes = SimpleVocabulary([
    SimpleTerm(value="light", title=_("light")),
    SimpleTerm(value="dark", title=_("dark")),
])
display_types = SimpleVocabulary([
    SimpleTerm(value="image", title=_("image")),
    SimpleTerm(value="audio", title=_("audio")),
])
display_sizes = SimpleVocabulary([
    SimpleTerm(value="normal", title=_("normal")),
    SimpleTerm(value="compact", title=_("compact")),
])


class IHCaptchaLayer(Interface):
    """Browser layer for plone.formwdiget.hcaptcha"""


class IHCaptchaWidget(interfaces.IWidget):
    """Marker interface for the HCaptcha widget"""


class IHCaptchaSettings(Interface):
    """Global discussion settings.

    This describes records stored in the configuration registry and
    obtainable via plone.registry.
    """

    # Todo: Write a short hint, that other discussion related options can
    # be found elsewhere in the Plone control panel:
    #
    # - Types control panel: Allow comments on content types
    # - Search control panel: Show comments in search results

    public_key = schema.TextLine(
        title=_("Public Key / Site Key"),
        description=_(""),
        required=True,
        default="",
    )

    private_key = schema.TextLine(
        title=_("Private Key / Secret Key"),
        description=_(""),
        required=True,
        default="",
    )

    display_theme = schema.Choice(
        title=_("Theme"),
        description=_("The color theme of the widget."),
        required=True,
        default="light",
        vocabulary=display_themes,
    )

    display_type = schema.Choice(
        title=_("Type"),
        description=_("The type of CAPTCHA to serve."),
        required=True,
        default="image",
        vocabulary=display_types,
    )

    display_size = schema.Choice(
        title=_("Size"),
        description=_("The size of the widget."),
        required=True,
        default="normal",
        vocabulary=display_sizes,
    )
