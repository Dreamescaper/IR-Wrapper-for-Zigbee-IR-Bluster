# Z2M IR Bridge

Home Assistant custom integration that exposes Zigbee2MQTT IR emitters, such as ZS06 and similar Tuya IR blasters, as Home Assistant infrared entities.

## Installation with HACS

1. In Home Assistant, open HACS.
2. Open the three-dot menu and choose **Custom repositories**.
3. Add this repository URL:

   ```text
   https://github.com/tomer2526/IR-Wrapper-for-Zigbee-IR-Bluster
   ```

4. Select **Integration** as the category.
5. Download **Z2M IR Bridge**.
6. Restart Home Assistant.
7. Go to **Settings** -> **Devices & services** -> **Add integration** and search for **Z2M IR Bridge**.

## Requirements

- Home Assistant with the MQTT integration configured.
- Zigbee2MQTT publishing device data under the configured base topic, usually `zigbee2mqtt`.

## Notes

The integration listens to Zigbee2MQTT bridge device payloads and MQTT discovery topics, detects IR-capable devices by known model or exposed IR properties, and publishes IR send commands back to Zigbee2MQTT.
