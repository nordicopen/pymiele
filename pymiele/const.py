"""Constants for pymiele."""

VERSION = "0.6.0b1"

MIELE_API = "https://api.mcs3.miele.com/v1"
OAUTH2_AUTHORIZE = "https://api.mcs3.miele.com/thirdparty/login"
OAUTH2_TOKEN = "https://api.mcs3.miele.com/thirdparty/token"
OAUTH2_SCOPE: set[str] = set()

# pylint: disable=line-too-long
MIELE_API_NEW = "https://api.domestic.miele-iot.com/v1"
OAUTH2_AUTHORIZE_NEW = "https://auth.domestic.miele-iot.com/partner/realms/mcs/protocol/openid-connect/auth"
OAUTH2_TOKEN_NEW = "https://auth.domestic.miele-iot.com/partner/realms/mcs/protocol/openid-connect/token"
OAUTH2_SCOPE_NEW = {
    "openid",
    "mcs_thirdparty_read",
    "mcs_thirdparty_write",
    "mcs_thirdparty_media",
}

AIO_TIMEOUT = 15
