"""Constants for pymiele."""

VERSION = "0.6.0"

MIELE_API_OLD = "https://api.mcs3.miele.com/v1"
OAUTH2_AUTHORIZE_OLD = "https://api.mcs3.miele.com/thirdparty/login"
OAUTH2_TOKEN_OLD = "https://api.mcs3.miele.com/thirdparty/token"
OAUTH2_SCOPE_OLD = {}

# pylint: disable=line-too-long
MIELE_API = "https://api.domestic.miele-iot.com/v1"
OAUTH2_AUTHORIZE = "https://auth.domestic.miele-iot.com/partner/realms/mcs/protocol/openid-connect/auth"
OAUTH2_TOKEN = "https://auth.domestic.miele-iot.com/partner/realms/mcs/protocol/openid-connect/token"
OAUTH2_SCOPE = {
    "openid",
    "mcs_thirdparty_read",
    "mcs_thirdparty_write",
    "mcs_thirdparty_media",
}

AIO_TIMEOUT = 15
