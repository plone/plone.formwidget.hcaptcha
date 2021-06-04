# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import plone.formwidget.recaptcha


class PloneFormwidgetRecaptchaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plone.formwidget.recaptcha)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plone.formwidget.recaptcha:default")


PLONE_FORMWIDGET_RECAPTCHA_FIXTURE = PloneFormwidgetRecaptchaLayer()


PLONE_FORMWIDGET_RECAPTCHA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_FORMWIDGET_RECAPTCHA_FIXTURE,),
    name="PloneFormwidgetRecaptchaLayer:IntegrationTesting",
)
