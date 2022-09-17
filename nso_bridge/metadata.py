from nso_bridge import NintendoSwitchAccount as _NSA

_app = _NSA()

ZNCA_PLATFORM: str = "IOS"
ZNCA_PLATFORM_VERSION: str = "8.0.0"
ZNCA_VERSION: str = _app.get_nso_app_version()
ZNCA_USER_AGENT: str = (
    f"com.nintendo.znca/{ZNCA_VERSION}({ZNCA_PLATFORM}/{ZNCA_PLATFORM_VERSION})"
)

__all__ = [
    ZNCA_PLATFORM,
    ZNCA_PLATFORM_VERSION,
    ZNCA_VERSION,
    ZNCA_USER_AGENT,
]
