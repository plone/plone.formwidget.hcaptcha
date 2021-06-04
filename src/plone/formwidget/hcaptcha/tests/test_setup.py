# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.formwidget.hcaptcha.testing import PLONE_FORMWIDGET_HCAPTCHA_INTEGRATION_TESTING  # noqa: E501

import plone.api
import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that plone.formwidget.hcaptcha is properly installed."""

    layer = PLONE_FORMWIDGET_HCAPTCHA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = plone.api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if plone.formwidget.hcaptcha is installed."""
        self.assertTrue(self.installer.isProductInstalled("plone.formwidget.hcaptcha"))

    def test_browserlayer(self):
        """Test that IHCaptchaLayer is registered."""
        from plone.formwidget.hcaptcha.interfaces import IHCaptchaLayer
        from plone.browserlayer import utils

        self.assertIn(IHCaptchaLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_FORMWIDGET_HCAPTCHA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = plone.api.portal.get_tool("portal_quickinstaller")
        roles_before = plone.api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["plone.formwidget.hcaptcha"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone.formwidget.hcaptcha is cleanly uninstalled."""
        self.assertFalse(
            self.installer.isProductInstalled("plone.formwidget.hcaptcha")
        )

    def test_browserlayer_removed(self):
        """Test that IHCaptchaLayer is removed."""
        from plone.formwidget.hcaptcha.interfaces import IHCaptchaLayer
        from plone.browserlayer import utils

        self.assertNotIn(IHCaptchaLayer, utils.registered_layers())
