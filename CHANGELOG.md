# Changelog

<!--
   You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
-->

<!-- towncrier release notes start -->

## 2.0.0 (2025-12-23)


### Internal:

- No changes @erral 

## 2.0.0b1 (2025-12-19)


### Breaking changes:

- Drop support to Plone 5.2. @wesleybl [#17](https://github.com/plone/plone.formwidget.hcaptcha/issues/17)


### New features:

- Adds support to Plone 6.1 and 6.0. @wesleybl [#17](https://github.com/plone/plone.formwidget.hcaptcha/issues/17)
- Add pt_BR translation. @wesleybl [#19](https://github.com/plone/plone.formwidget.hcaptcha/issues/19)


### Internal:

- Apply cookieplone template. @wesleybl [#17](https://github.com/plone/plone.formwidget.hcaptcha/issues/17)

1.0.4 (2025-11-14)
------------------

Bug fixes:


- Fix hCaptcha verification to use the documented endpoint (api.hcaptcha.com/siteverify) and allow overriding the host via the HCAPTCHA_VERIFY_SERVER environment variable. @alexandreIFB (#13)
- Fix CI. @wesleybl (#15)


1.0.3 (2024-03-28)
------------------

Bug fixes:


- German translation for public validator error message.
  [ksuess]  (#12)


1.0.2 (2022-06-23)
------------------

New features:


- Add an adapter to show the controlpanel in Volto
  [erral] (#8)
- Dutch translation for public validator error message.
  [fredvd] (#10)


Bug fixes:


- Create translation files
  [erral] (#9)


1.0.1 (2022-02-20)
------------------

New features:


- Move CI from TravisCI to Github Actions [jensens] (#29)


Bug fixes:


- Verify against hcaptcha API with correct URL and api path, code was still checking against recaptcha siteverify api. [fredvd]

  Remove IP from sent api call as it can be considered GDPR violation. [fredvd] (#2)


1.0.0 (2021-06-10)
------------------

- Initial release. [andreasma]