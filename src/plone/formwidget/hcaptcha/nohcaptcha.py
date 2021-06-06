# -*- coding: utf-8 -*-
# Code taken from external dependency
# https://pypi.org/project/nohcaptcha/, which is not
# updated to Python 3
from six.moves.urllib import parse
from six.moves.urllib.request import Request
from six.moves.urllib.request import urlopen

import six


try:
    import json
except ImportError:
    import simplejson as json


VERIFY_SERVER = "www.google.com"


class HcaptchaResponse(object):
    def __init__(self, is_valid, error_code=None):
        self.is_valid = is_valid
        self.error_code = error_code

    def __repr__(self):
        return "Hcaptcha response: {0} {1}".format(self.is_valid, self.error_code)

    def __str__(self):
        return self.__repr__()


def displayhtml(
    site_key, language="", theme="light", fallback=False, d_type="image", size="normal"
):
    """
    Gets the HTML to display for HCAPTCHA

    site_key -- The site key
    language -- The language code for the widget.
    theme -- The color theme of the widget. `light` or `dark`
    fallback -- Old version hcaptcha.
    d_type -- The type of CAPTCHA to serve. `image` or `audio`
    size -- The size of the dispalyed CAPTCHA, 'normal' or 'compact'

    For more detail, refer to:
      - https://developers.google.com/hcaptcha/docs/display
    """

    return """
<script
  src="https://hcaptcha.com/1/api.js?hl=%(LanguageCode)s&fallback=%(Fallback)s&"
  async="async" defer="defer"></script>
<div class="h-captcha"
    data-sitekey="%(SiteKey)s"
    data-theme="%(Theme)s"
    data-type="%(Type)s"
    data-size="%(Size)s">
</div>
""" % {
        "LanguageCode": language,
        "SiteKey": site_key,
        "Theme": theme,
        "Type": d_type,
        "Size": size,
        "Fallback": fallback,
    }


def submit(hcaptcha_response_field, secret_key, remoteip, verify_server=VERIFY_SERVER):
    """
    Submits a HCAPTCHA request for verification. Returns HcaptchaResponse
    for the request

    hcaptcha_response_field -- The value from the form
    secret_key -- your HCAPTCHA secret key
    remoteip -- the user's ip address
    """

    if not (hcaptcha_response_field and len(hcaptcha_response_field)):
        return HcaptchaResponse(is_valid=False, error_code="incorrect-captcha-sol")

    def encode_if_necessary(s):
        if isinstance(s, six.text_type):
            return s.encode("utf-8")
        return s

    if six.PY2:
        secret_key = encode_if_necessary(secret_key)
        remoteip = encode_if_necessary(remoteip)
        hcaptcha_response_field = encode_if_necessary(hcaptcha_response_field)

    params = parse.urlencode(
        {
            "secret": secret_key,
            "remoteip": remoteip,
            "response": hcaptcha_response_field,
        }
    )

    request = Request(
        url="https://{0}/recaptcha/api/siteverify".format(verify_server),
        data=params,
        headers={
            "Content-type": "application/x-www-form-urlencoded",
            "User-agent": "noReCAPTCHA Python",
        },
    )

    if six.PY3:
        request.data = request.data.encode("utf-8")

    httpresp = urlopen(request)

    return_values = json.loads(httpresp.read())
    httpresp.close()

    return_code = return_values["success"]
    error_codes = return_values.get("error-codes", [])

    if return_code:
        return HcaptchaResponse(is_valid=True)
    else:
        return HcaptchaResponse(is_valid=False, error_code=error_codes)
