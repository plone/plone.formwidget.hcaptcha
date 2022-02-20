Changelog
=========

.. You should *NOT* be adding new change log entries to this file, this
   file is managed by towncrier. You *may* edit previous change logs to
   fix problems like typo corrections or such.

.. towncrier release notes start

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
