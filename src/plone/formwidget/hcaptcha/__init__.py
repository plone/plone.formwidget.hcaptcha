"""Init and utils."""

from plone.formwidget.hcaptcha.browser.widget import HCaptchaFieldWidget  # noqa: F401
from plone.formwidget.hcaptcha.browser.widget import HCaptchaWidget  # noqa: F401
from plone.formwidget.hcaptcha.validator import HCaptchaValidator  # noqa: F401
from zope.i18nmessageid import MessageFactory

import logging


__version__ = "3.0.1.dev0"

PACKAGE_NAME = "plone.formwidget.hcaptcha"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
