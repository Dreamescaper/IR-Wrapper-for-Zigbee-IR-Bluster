"""Config flow for Z2M IR Bridge."""

from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries

from .const import (
    CONF_BASE_TOPIC,
    CONF_DISCOVERY_PREFIX,
    CONF_ENABLE_AUTO,
    CONF_ENABLE_Z2M,
    CONF_MANUAL_FRIENDLY_NAMES,
    CONF_ZHA_DEVICES,
    DEFAULT_BASE_TOPIC,
    DEFAULT_DISCOVERY_PREFIX,
    DOMAIN,
)


class Z2MIRConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Z2M IR Bridge."""

    VERSION = 1

    @staticmethod
    def async_get_options_flow(config_entry):
        """Create the options flow."""

        return Z2MIROptionsFlow(config_entry)

    async def async_step_user(self, user_input=None):
        """Create the integration entry."""

        if user_input is not None:
            await self.async_set_unique_id(DOMAIN)
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title="Z2M IR Bridge",
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Optional(CONF_ENABLE_AUTO, default=True): bool,
                    vol.Optional(CONF_ENABLE_Z2M, default=True): bool,
                    vol.Optional(CONF_BASE_TOPIC, default=DEFAULT_BASE_TOPIC): str,
                    vol.Optional(
                        CONF_DISCOVERY_PREFIX,
                        default=DEFAULT_DISCOVERY_PREFIX,
                    ): str,
                    vol.Optional(
                        CONF_MANUAL_FRIENDLY_NAMES,
                        default="",
                    ): str,
                    vol.Optional(
                        CONF_ZHA_DEVICES,
                        default="",
                    ): str,
                }
            ),
        )


class Z2MIROptionsFlow(config_entries.OptionsFlow):
    """Handle options for Z2M IR Bridge."""

    def __init__(self, config_entry):
        """Initialize the options flow."""

        self._config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Update integration options."""

        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data = {**self._config_entry.data, **self._config_entry.options}
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_ENABLE_AUTO,
                        default=data.get(CONF_ENABLE_AUTO, True),
                    ): bool,
                    vol.Optional(
                        CONF_ENABLE_Z2M,
                        default=data.get(CONF_ENABLE_Z2M, True),
                    ): bool,
                    vol.Optional(
                        CONF_BASE_TOPIC,
                        default=data.get(CONF_BASE_TOPIC, DEFAULT_BASE_TOPIC),
                    ): str,
                    vol.Optional(
                        CONF_DISCOVERY_PREFIX,
                        default=data.get(
                            CONF_DISCOVERY_PREFIX,
                            DEFAULT_DISCOVERY_PREFIX,
                        ),
                    ): str,
                    vol.Optional(
                        CONF_MANUAL_FRIENDLY_NAMES,
                        default=data.get(CONF_MANUAL_FRIENDLY_NAMES, ""),
                    ): str,
                    vol.Optional(
                        CONF_ZHA_DEVICES,
                        default=data.get(CONF_ZHA_DEVICES, ""),
                    ): str,
                }
            ),
        )
