"""Constants for the Z2M IR Bridge integration."""

from __future__ import annotations

DOMAIN = "z2m_ir_bridge"

DEFAULT_BASE_TOPIC = "zigbee2mqtt"
DEFAULT_DISCOVERY_PREFIX = "homeassistant"
DEFAULT_ZHA_CLUSTER_ID = 57348
DEFAULT_ZHA_COMMAND = 2
DEFAULT_ZHA_ENDPOINT_ID = 1

PLATFORMS = ["infrared"]

BACKEND_Z2M = "z2m"
BACKEND_ZHA = "zha"

CONF_BASE_TOPIC = "base_topic"
CONF_DISCOVERY_PREFIX = "discovery_prefix"
CONF_ENABLE_AUTO = "enable_auto"
CONF_ENABLE_Z2M = "enable_z2m"
CONF_MANUAL_FRIENDLY_NAMES = "manual_friendly_names"
CONF_ZHA_DEVICES = "zha_devices"

ATTR_BACKEND = "backend"
ATTR_CODE = "code"
ATTR_FRIENDLY_NAME = "friendly_name"
ATTR_REPEAT = "repeat"
ATTR_ZHA_CLUSTER_ID = "zha_cluster_id"
ATTR_ZHA_COMMAND = "zha_command"
ATTR_ZHA_ENDPOINT_ID = "zha_endpoint_id"
ATTR_ZHA_IEEE = "zha_ieee"

SERVICE_SEND_CODE = "send_code"

SIGNAL_NEW_IR_DEVICE = "z2m_ir_bridge_new_ir_device_{}"

IR_MODELS = {
    "ZS06",
    "TS120F",
    "TUYA_IR_BLASTER",
}

IR_KEYS = {
    "ir_code_to_send",
    "learn_ir_code",
    "learned_ir_code",
}
