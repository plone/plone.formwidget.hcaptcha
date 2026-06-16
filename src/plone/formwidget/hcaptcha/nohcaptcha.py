from urllib import parse
from urllib.request import Request
from urllib.request import urlopen

import json
import os


VERIFY_SERVER = os.getenv("HCAPTCHA_VERIFY_SERVER", "api.hcaptcha.com")


class HcaptchaResponse:
    def __init__(self, is_valid: bool, error_code: str | list | None = None):
        self.is_valid = is_valid
        self.error_code = error_code

    def __repr__(self) -> str:
        return f"Hcaptcha response: {self.is_valid} {self.error_code}"

    def __str__(self) -> str:
        return self.__repr__()


def displayhtml(
    site_key: str,
    language: str = "",
    theme: str = "light",
    fallback: bool = False,
    d_type: str = "image",
    size: str = "normal",
) -> str:
    """Get the HTML to display for HCaptcha.

    :param site_key: The site key.
    :param language: The language code for the widget.
    :param theme: The color theme of the widget, ``light`` or ``dark``.
    :param fallback: Old version hcaptcha.
    :param d_type: The type of CAPTCHA to serve, ``image`` or ``audio``.
    :param size: The size of the displayed CAPTCHA, ``normal`` or ``compact``.
    :returns: The HTML snippet rendering the HCaptcha widget.
    """
    return f"""
<script
  src="https://hcaptcha.com/1/api.js?hl={language}&fallback={fallback}&"
  async="async" defer="defer"></script>
<div class="h-captcha"
    data-sitekey="{site_key}"
    data-theme="{theme}"
    data-type="{d_type}"
    data-size="{size}">
</div>
"""


def submit(
    hcaptcha_response_field: str,
    secret_key: str,
    verify_server: str = VERIFY_SERVER,
) -> HcaptchaResponse:
    """Submit a HCaptcha request for verification.

    :param hcaptcha_response_field: The value from the form.
    :param secret_key: Your HCaptcha secret key.
    :param verify_server: The HCaptcha verification server host.
    :returns: The :class:`HcaptchaResponse` for the request.
    """
    if not hcaptcha_response_field:
        return HcaptchaResponse(is_valid=False, error_code="incorrect-captcha-sol")

    params = parse.urlencode({
        "secret": secret_key,
        "response": hcaptcha_response_field,
    }).encode("utf-8")

    request = Request(
        url=f"https://{verify_server}/siteverify",
        data=params,
        headers={
            "Content-type": "application/x-www-form-urlencoded",
            "User-agent": "HCAPTCHA Python",
        },
    )

    with urlopen(request) as httpresp:  # noqa: S310
        return_values = json.loads(httpresp.read())

    return_code = return_values["success"]
    error_codes = return_values.get("error-codes", [])

    if return_code:
        return HcaptchaResponse(is_valid=True)
    return HcaptchaResponse(is_valid=False, error_code=error_codes)
