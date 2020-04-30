"""Event messages on state changes."""

#  https://demo.ui.com/manage/locales/en/eventStrings.json?v=5.4.11.2

CONTROLLER_UPDATE_AVAILABLE = "EVT_AD_Update_Available"

ACCESS_POINT_ADOPTED = "EVT_AP_Adopted"
ACCESS_POINT_CONFIGURED = "EVT_AP_Configured"
ACCESS_POINT_CONNECTED = "EVT_AP_Connected"
ACCESS_POINT_DELETED = "EVT_AP_Deleted"
ACCESS_POINT_RESTARTED = "EVT_AP_Restarted"
ACCESS_POINT_UPGRADED = "EVT_AP_Upgraded"

GATEWAY_ADOPTED = "EVT_GW_Adopted"
GATEWAY_CONNECTED = "EVT_GW_Connected"
GATEWAY_DELETED = "EVT_GW_Deleted"
GATEWAY_LOST_CONTACT = "EVT_GW_Lost_Contact"
GATEWAY_RESTART = "EVT_GW_Restarted"
GATEWAY_UPGRADED = "EVT_GW_Upgraded"

SWITCH_ADOPTED = "EVT_SW_Adopted"
SWITCH_CONNECTED = "EVT_SW_Connected"
SWITCH_DELETED = "EVT_SW_Deleted"
SWITCH_LOST_CONTACT = "EVT_SW_Lost_Contact"
SWITCH_OVERHEAT = "EVT_SW_Overheat"
SWITCH_POE_OVERLOAD = "EVT_SW_POE_Overload"
SWITCH_POE_DISCONNECT = "EVT_SW_POE_Disconnect"
SWITCH_RESTARTED = "EVT_SW_Restarted"
SWITCH_RESTARTED_UNKNOWN = "EVT_SW_RestartedUnknown"
SWITCH_UPGRADED = "EVT_SW_Upgraded"

WIRED_CLIENT_CONNECTED = "EVT_LU_Connected"
WIRED_CLIENT_DISCONNECTED = "EVT_LU_Disconnected"
WIRED_CLIENT_BLOCKED = "EVT_LC_Blocked"
WIRED_CLIENT_UNBLOCKED = "EVT_LC_Unblocked"
WIRELESS_CLIENT_CONNECTED = "EVT_WU_Connected"
WIRELESS_CLIENT_DISCONNECTED = "EVT_WU_Disconnected"
WIRELESS_CLIENT_BLOCKED = "EVT_WC_Blocked"
WIRELESS_CLIENT_UNBLOCKED = "EVT_WC_Unblocked"
WIRELESS_CLIENT_ROAM = "EVT_WU_Roam"
WIRELESS_GUEST_CONNECTED = "EVT_WG_Connected"
WIRELESS_GUEST_DISCONNECTED = "EVT_WG_Disconnected"
WIRELESS_GUEST_ROAM = "EVT_WG_Roam"

CLIENT_EVENTS = (
    WIRED_CLIENT_CONNECTED,
    WIRED_CLIENT_DISCONNECTED,
    WIRED_CLIENT_BLOCKED,
    WIRED_CLIENT_UNBLOCKED,
    WIRELESS_CLIENT_CONNECTED,
    WIRELESS_CLIENT_DISCONNECTED,
    WIRELESS_CLIENT_BLOCKED,
    WIRELESS_CLIENT_UNBLOCKED,
    WIRELESS_CLIENT_ROAM,
    WIRELESS_GUEST_CONNECTED,
    WIRELESS_GUEST_DISCONNECTED,
    WIRELESS_GUEST_ROAM,
)
DEVICE_EVENTS = (
    ACCESS_POINT_ADOPTED,
    ACCESS_POINT_CONFIGURED,
    ACCESS_POINT_CONNECTED,
    ACCESS_POINT_DELETED,
    ACCESS_POINT_RESTARTED,
    ACCESS_POINT_UPGRADED,
    GATEWAY_ADOPTED,
    GATEWAY_CONNECTED,
    GATEWAY_DELETED,
    GATEWAY_LOST_CONTACT,
    GATEWAY_RESTART,
    GATEWAY_UPGRADED,
    SWITCH_ADOPTED,
    SWITCH_CONNECTED,
    SWITCH_DELETED,
    SWITCH_LOST_CONTACT,
    SWITCH_OVERHEAT,
    SWITCH_POE_OVERLOAD,
    SWITCH_POE_DISCONNECT,
    SWITCH_RESTARTED,
    SWITCH_UPGRADED,
)


class event:
    def __init__(self, raw):
        self.raw = raw

    @property
    def event(self) -> str:
        """Event key e.g. 'EVT_WU_Disconnected'"""
        return self.raw["key"]

    @property
    def msg(self) -> str:
        """Message 'User[00:00:00:00:00:01] disconnected from "Access point" (1h 27m connected, 58.97M bytes, last AP[00:11:22:33:44:55])'"""
        return self.raw["msg"]

    @property
    def time(self) -> int:
        """Time of event 1583076908000"""
        return self.raw["time"]

    @property
    def datetime(self) -> str:
        """Datetime of event '2020-03-01T15:35:08Z'."""
        return self.raw["datetime"]

    @property
    def ap(self) -> str:
        """Access point connected to."""
        return self.raw("ap", "")

    @property
    def client(self) -> str:
        """MAC address of client."""
        return (
            self.raw.get("user")
            or self.raw.get("client")
            or self.raw.get("guest")
            or ""
        )

    @property
    def device(self) -> str:
        """MAC address of device."""
        return self.raw.get("ap") or self.raw.get("gw") or self.raw.get("sw") or ""

    @property
    def hostname(self) -> str:
        """Nice name"""
        return self.raw.get("hostname", "")

    @property
    def subsystem(self) -> str:
        """Subsystem like 'lan' or 'wlan'"""
        return self.raw.get("subsystem", "")

    @property
    def ssid(self) -> str:
        return self.raw.get("ssid", "")

    @property
    def mac(self) -> str:
        if self.client:
            return self.client
        if self.device:
            return self.device
        return ""
