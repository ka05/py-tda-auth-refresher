from web.form_executioner import FormExecutioner
from web.tda_config_provider import TDAConfigProvider
from web.web_driver_provider import WebDriverProvider


class TDATokenRefresher:

    @staticmethod
    def get_oauth_token(use_headless_web_driver=True):
        return FormExecutioner(
            TDAConfigProvider.get_config(),
            WebDriverProvider.get_web_driver(use_headless_web_driver)
        ).get_token()
