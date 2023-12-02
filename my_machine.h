/*
  my_machine.h - configuration for Raspberry RP2040 ARM processors

  Part of grblHAL

  Copyright (c) 2021-2023 Terje Io

  Grbl is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  Grbl is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with Grbl.  If not, see <http://www.gnu.org/licenses/>.
*/

// NOTE: Only one board may be enabled!
// If none is enabled pin mappings from generic_map.h will be used.
//#define BOARD_PICO_CNC
//#define BOARD_PICOBOB
//#define BOARD_PICOBOB_G540
//#define BOARD_BTT_SKR_PICO_10 // incomplete and untested!
//#define BOARD_CNC_BOOSTERPACK
//#define BOARD_CITOH_CX6000    // C.ITOH CX-6000 HPGL plotter
//#define BOARD_GENERIC_4AXIS
//#define BOARD_MY_MACHINE      // Add my_machine_map.h before enabling this!
#define BOARD_MY_MACHINE      // Add my_machine_map.h before enabling this!

// Configuration
// Uncomment to enable.

#ifndef USB_SERIAL_CDC
#define USB_SERIAL_CDC       1 // Serial communication via native USB.
#endif
//#define SAFETY_DOOR_ENABLE   1 // Enable safety door input.
//#define BLUETOOTH_ENABLE     2 // Set to 2 for HC-05 module, enable in CMakeLists.txt if for Pico W Bluetooth.
#define VFD_ENABLE             1 // Set to 1 works or 2 for Huanyang VFD spindle. More here https://github.com/grblHAL/Plugins_spindle
#define MODBUS_ENABLE          1 // Set to 1 for auto direction, 2 for direction signal on auxillary output pin.
#define MODBUS_BAUDRATE 2 // 9600
#define WIFI_ENABLE            1 // Do NOT enable here, enable in CMakeLists.txt!
#define WIFI_SOFTAP            1 // Use Soft AP mode for WiFi. NOTE: WIP - not yet complete!
//#define ETHERNET_ENABLE      0 // Do NOT enable here, enable in CMakeLists.txt!
//#define _WIZCHIP_         5500 // Selects WIZnet ethernet breakout connected via SPI.
                                 // Uncomment to enable W5500 chip, default is W5100S. Requires ethernet enabled in CMakeLists.txt.
//#define WEBUI_ENABLE         1 // Enable ESP3D-WEBUI plugin along with networking and SD card plugins. Requires WiFi enabled.
//#define WEBUI_AUTH_ENABLE    1 // Enable ESP3D-WEBUI authentication.
//#define WEBUI_INFLASH        1 // Store WebUI files in flash instead of on SD card.
//#define SDCARD_ENABLE        2 // Run gcode programs from SD card. Set to 2 to enable YModem upload.
#define MPG_ENABLE           1 // Enable MPG interface. Requires serial port and one handshake pin unless
                                 // KEYPAD_ENABLE is set to 2 when mode switching is done by the CMD_MPG_MODE_TOGGLE (0x8B)
                                 // command character. Set both MPG_ENABLE and KEYPAD_ENABLE to 2 to use a handshake pin anyway.
//ig added for MPG
#define SERIAL1_PORT 1 
#define MPG_MODE 2

#define KEYPAD_ENABLE        2 // Set to 1 for I2C keypad, 2 for other input such as serial data. If KEYPAD_ENABLE is set to 2 
                                 // and MPG_ENABLE is uncommented then the serial stream is shared with the MPG.
//#define DISPLAY_ENABLE       1 // Set to 1 for I2C display protocol, 2 for I2C LED protocol.
//#define ODOMETER_ENABLE      1 // Odometer plugin.
//#define PPI_ENABLE           1 // Laser PPI plugin. To be completed.
//#define LASER_COOLANT_ENABLE 1 // Laser coolant plugin. To be completed.
//#define FANS_ENABLE          1 // Enable fan control via M106/M107. Activates fan plugin.
//#define EMBROIDERY_ENABLE    1 // Embroidery plugin. To be completed.

// If the selected board map supports more than three motors ganging and/or auto-squaring
// of axes can be enabled here.
//#define X_GANGED             1
//#define X_AUTO_SQUARE        1
//#define Y_GANGED             1
//#define Y_AUTO_SQUARE        1
//#define Z_GANGED             1
//#define Z_AUTO_SQUARE        1
// For ganged axes the limit switch input (if available) can be configured to act as a max travel limit switch.
// NOTE: If board map already has max limit inputs defined this configuration will be ignored.
//#define X_GANGED_LIM_MAX     1
//#define Y_GANGED_LIM_MAX     1
//#define Z_GANGED_LIM_MAX     1
//

//#define _WIZCHIP_ 5500

#if WIFI_ENABLE || ETHERNET_ENABLE || WEBUI_ENABLE
#define TELNET_ENABLE        1 // Telnet daemon - requires WiFi streaming enabled.
#define WEBSOCKET_ENABLE     1 // Websocket daemon - requires WiFi streaming enabled.
//#define MDNS_ENABLE          0 // mDNS daemon. Do NOT enable here, enable in CMakeLists.txt!
//#define SSDP_ENABLE          1 // SSDP daemon - requires HTTP enabled.
#if SDCARD_ENABLE || WEBUI_ENABLE
//#define FTP_ENABLE           1 // Ftp daemon - requires SD card enabled.
//#define HTTP_ENABLE          1 // http daemon - requires SD card enabled.
//#define WEBDAV_ENABLE        1 // webdav protocol - requires http daemon and SD card enabled.
#endif
// The following symbols have the default values as shown, uncomment and change as needed.
#define NETWORK_STA_HOSTNAME    "grblHAL"
#define NETWORK_STA_IPMODE      1 // 0 = static, 1 = DHCP, 2 = AutoIP
#define COMPATIBILITY_LEVEL 2

#define NETWORK_HOSTNAME        "grbl"
#define NETWORK_IPMODE          1 // 0 = static, 1 = DHCP, 2 = AutoIP
#define NETWORK_IP              "192.168.4.1"
#define NETWORK_GATEWAY         "192.168.4.1"
#define NETWORK_PASSWORD     "grbl"
#define NETWORK_MASK            "255.255.255.0"

#define NETWORK_STA_SSID         "IGORNET"
#define NETWORK_STA_PASSWORD     "IG0RNET29041971" 

#define NETWORK_STA_IP          "10.80.39.130"
#define NETWORK_STA_GATEWAY     "10.80.39.3"
#define NETWORK_STA_MASK        "255.255.255.0"

#if WIFI_SOFTAP > 0
#define NETWORK_AP_SSID         "grblHAL_AP"
#define NETWORK_AP_PASSWORD     "grbl"
#define NETWORK_AP_HOSTNAME     "grbl"
#define NETWORK_AP_IPMODE       1              // Do not change!
#define NETWORK_AP_IP           "192.168.4.1"  // Do not change!
#define NETWORK_AP_GATEWAY      "192.168.4.1"  // Do not change!
#define NETWORK_AP_MASK         "255.255.255.0"
#define WIFI_STA_SSID "IGORNET"
#define WIFI_STA_PASSWORD "IG0RNET29041971" // Minimum 8 characters, or blank for open

#else
#define WIFI_SOFTAP 0
#define WIFI_MODE WiFiMode_STA; // Do not change!
//#define WIFI_STA_SSID "IGORNET"
//#define WIFI_STA_PASSWORD "IG0RNET29041971" // Minimum 8 characters, or blank for open
//#define MQTT_IP_ADDRESS "10.80.39.78"
//#define MQTT_USERNAME "igor"
//#define MQTT_PASSWORD "p29041971"
#endif

//#define NETWORK_FTP_PORT     21
//#define NETWORK_TELNET_PORT  23
#define NETWORK_HTTP_PORT    80
#if HTTP_ENABLE
#define NETWORK_WEBSOCKET_PORT  81
#else
#define NETWORK_WEBSOCKET_PORT  80
#endif
#endif // WIFI_ENABLE

/**/
