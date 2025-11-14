# plone.formwidget.hcaptcha

plone.formwidget.hcaptcha is a `z3c.form` HCaptcha widget for use with Plone.

It is a re-work of the [plone.formwidget.recaptcha](http://github.com/plone/plone.formwidget.recaptcha) package original written by Timo Stollenwerk.

## HCaptcha setup

There is a control panel at `http://path/to/site/@@hcaptcha-settings` to configure the Addon.
HCaptcha provides test keys, that can be used to try out the hcaptcha form and
documentation at https://docs.hcaptcha.com/.

**Site key:** `10000000-ffff-ffff-ffff-000000000001`

**Secret key:** `0x0000000000000000000000000000000000000000`

To actually use the service, you must obtain a site key and secret key from
[https://www.hcaptcha.com/signup-interstitial](https://www.hcaptcha.com/signup-interstitial/)

## Verification endpoint

According to the official hCaptcha documentation (https://docs.hcaptcha.com/#server),
the token verification endpoint is:

`https://api.hcaptcha.com/siteverify`

This package now uses `api.hcaptcha.com` by default instead of `hcaptcha.com`.
If you need to change the host (e.g. staging or internal testing), set the environment
variable before starting your Plone instance:

`HCAPTCHA_VERIFY_SERVER=api.hcaptcha.com`

If the variable is not defined, the safe default (`api.hcaptcha.com`) will be used.

## Usage

See the [demo](https://github.com/plone/plone.formwidget.hcaptcha/tree/master/src/plone/formwidget/hcaptcha/demo) folder inside the distribution for an example usage.

### Supermodel

You can add a captcha field in an XML model by adding something like this:

```xml
<field name="captcha" type="plone.formwidget.hcaptcha.HCaptchaWidget">
  <title>Solve Captcha</title>
  <description></description>
</field>
```

## Source Code

Contributors please read the document [Process for Plone core's development](http://docs.plone.org/develop/plone-coredev/index.html)

Sources are at the [Plone code repository hosted at Github](https://github.com/plone/plone.formwidget.hcaptcha).


## Features

TODO: List our awesome features

## Installation

Install plone.formwidget.hcaptcha with `pip`:

```shell
pip install plone.formwidget.hcaptcha
```

And to create the Plone site:

```shell
make create-site
```

## Contribute

- [Issue tracker](https://github.com/plone/plone.formwidget.hcaptcha/issues)
- [Source code](https://github.com/plone/plone.formwidget.hcaptcha/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:plone/plone.formwidget.hcaptcha.git
    cd plone.formwidget.hcaptcha
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

```{seealso}
You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.
```

## License

The project is licensed under GPLv2.

## Credits and acknowledgements 🙏

Generated using [Cookieplone (0.9.10)](https://github.com/plone/cookieplone) and [cookieplone-templates (c0b5a93)](https://github.com/plone/cookieplone-templates/commit/c0b5a93e16bc7da0fb36f37242a5dcf7f792323f) on 2025-11-14 18:16:57.945239. A special thanks to all contributors and supporters!
