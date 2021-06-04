# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import plone.formwidget.hcaptcha


class PloneFormwidgetHcaptchaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plone.formwidget.hcaptcha)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plone.formwidget.hcaptcha:default")


PLONE_FORMWIDGET_HCAPTCHA_FIXTURE = PloneFormwidgetHcaptchaLayer()


PLONE_FORMWIDGET_HCAPTCHA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_FORMWIDGET_HCAPTCHA_FIXTURE,),
    name="PloneFormwidgetHcaptchaLayer:IntegrationTesting",
)
