"""Init and utils."""

from plone.formwidget.hcaptcha.validator import HCaptchaValidator  # noqa
from plone.formwidget.hcaptcha.widget import HCaptchaFieldWidget  # noqa
from plone.formwidget.hcaptcha.widget import HCaptchaWidget  # noqa
from zope.i18nmessageid import MessageFactory

import logging


__version__ = "2.0.1.dev0"

PACKAGE_NAME = "plone.formwidget.hcaptcha"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
