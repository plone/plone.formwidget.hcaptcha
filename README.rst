Introduction
============

plone.formwidget.hcaptcha is a ``z3c.form`` HCaptcha widget for use with Plone.

It is a re-work of the 'plone.formwidget.recaptcha'_ package original written by Timo Stollenwerk.

.. _plone.forwwidget.recaptcha: http://github.com/plone/plone.formwidget.recaptcha


Buildout Installation
---------------------

Add the following code to your buildout.cfg to install plone.formwidget.hcaptcha::

    [buildout]
    ...

    [instance]
    ...
    eggs =
        ...
        plone.formwidget.hcaptcha
        ...


HCaptcha setup
--------------

There is a control panel at ``http://path/to/site/@@hcaptcha-settings`` to configure the Addon.
HCaptcha provides test keys, that can be used to try out the hcaptcha form and
documentation at https://docs.hcaptcha.com/.

``Site key: 10000000-ffff-ffff-ffff-000000000001``

``Secret key: 0x0000000000000000000000000000000000000000``

To actually use the service, you must obtain a site key and secret key from
`https://www.hcaptcha.com/signup-interstitial <https://www.hcaptcha.com/signup-interstitial/>`_

Usage
-----
See the `demo <https://github.com/plone/plone.formwidget.hcaptcha/tree/master/src/plone/formwidget/hcaptcha/demo>`_ folder inside the distribution for an example usage.

Supermodel
----------
You can add a captcha field in an XML model by adding something like this::

    <field name="captcha" type="plone.formwidget.hcaptcha.HCaptchaWidget">
      <title>Solve Captcha</title>
      <description></description>
    </field>

Translations
------------

The only day to day visible message will be the error message when a hcaptcha validation fails. The message string is located in validator.py and has been put in the 'plone' domain.
Translations will be added to plone.app.locales. 

If you want to add/override your own translation for this, for buildout you can use the locales attribute of plone.recipe.zope2instance to register a locales directory in your project where you can add a plone.po file. Alternatively you can add the same plone.po file
in a policy package, but you have to make sure the zcml of that package is called first.



Source Code
-----------

Contributors please read the document `Process for Plone core's development <http://docs.plone.org/develop/plone-coredev/index.html>`_

Sources are at the `Plone code repository hosted at Github <https://github.com/plone/plone.formwidget.hcaptcha>`_.
