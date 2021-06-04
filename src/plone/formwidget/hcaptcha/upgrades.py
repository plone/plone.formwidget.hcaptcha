# -*- coding: utf-8 -*-
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility


def install_browserlayer(context):
    setup = getToolByName(context, "portal_setup")
    setup.runImportStepFromProfile(
        "profile-plone.formwidget.recaptcha:default",
        "browserlayer",
        run_dependencies=False,
        purge_old=False,
    )


def reapply_registry(context):
    setup = getToolByName(context, "portal_setup")
    setup.runImportStepFromProfile(
        "profile-plone.formwidget.recaptcha:default",
        "plone.app.registry",
        run_dependencies=False,
        purge_old=False,
    )


def to_4(context):

    jstool = getToolByName(context, "portal_javascripts", None)
    if jstool:
        jstool.manage_removeScript(
            "++resource++plone.formwidget.recaptcha/recaptcha_ajax.js"
        )

    registry = getUtility(IRegistry)
    record = "plone.bundles/plone-legacy.resources"
    if record in registry.records:
        # Plone 5
        resources = registry.records[record]
        res = "resource-plone-formwidget-recaptcha-recaptcha_ajax"
        if res in resources.value:
            resources.value.remove(res)

        if res in registry.records:
            del registry.records["plone.resources/%s" % res]
