# -*- coding: utf-8 -*-
from z3c.form import interfaces
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


_ = MessageFactory("plone.formwidget.hcaptcha")

display_themes = SimpleVocabulary(
    [
        SimpleTerm(value=u"light", title=_(u"light")),
        SimpleTerm(value=u"dark", title=_(u"dark")),
    ]
)
display_types = SimpleVocabulary(
    [
        SimpleTerm(value=u"image", title=_(u"image")),
        SimpleTerm(value=u"audio", title=_(u"audio")),
    ]
)
display_sizes = SimpleVocabulary(
    [
        SimpleTerm(value=u"normal", title=_(u"normal")),
        SimpleTerm(value=u"compact", title=_(u"compact")),
    ]
)


class IHCaptchaLayer(Interface):
    """Browser layer for plone.formwdiget.hcaptcha"""


class IHCaptchaWidget(interfaces.IWidget):
    """Marker interface for the HCaptcha widget
    """


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
        title=_(u"Public Key / Site Key"), description=_(u""), required=True, default=u""
    )

    private_key = schema.TextLine(
        title=_(u"Private Key / Secret Key"), description=_(u""), required=True, default=u""
    )

    display_theme = schema.Choice(
        title=_(u"Theme"),
        description=_(u"The color theme of the widget."),
        required=True,
        default=u"light",
        vocabulary=display_themes,
    )

    display_type = schema.Choice(
        title=_(u"Type"),
        description=_(u"The type of CAPTCHA to serve."),
        required=True,
        default=u"image",
        vocabulary=display_types,
    )

    display_size = schema.Choice(
        title=_(u"Size"),
        description=_(u"The size of the widget."),
        required=True,
        default=u"normal",
        vocabulary=display_sizes,
    )
