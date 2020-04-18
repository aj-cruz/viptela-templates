class data:
    def __init__(self):
        self.payload = """
        {
            "templateName": "System-Router",
            "templateDescription": "Global Router System Template",
            "templateType": "system-vedge",
            "templateMinVersion": "15.0.0",
            "templateDefinition": {
                "clock": {
                    "timezone": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "UTC",
                        "vipVariableName": "system_timezone"
                    }
                },
                "gps-location": {
                    "latitude": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipVariableName": "system_latitude"
                    },
                    "longitude": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipVariableName": "system_longitude"
                    }
                },
                "timer": {
                    "dns-cache-timeout": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": 2,
                        "vipVariableName": "system_dns_cache_timeout"
                    }
                },
                "location": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "system_location"
                },
                "system-tunnel-mtu": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": 1024,
                    "vipVariableName": "system_system_tunnel_mtu"
                },
                "track-transport": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "true",
                    "vipVariableName": "system_track_transport"
                },
                "track-interface-tag": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "system_track_interface_tag"
                },
                "port-offset": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": 0,
                    "vipVariableName": "system_port_offset"
                },
                "port-hop": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "true",
                    "vipVariableName": "system_port_hop"
                },
                "control-session-pps": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": 300,
                    "vipVariableName": "system_control_session_pps"
                },
                "description": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "system_description"
                },
                "device-groups": {
                    "vipObjectType": "list",
                    "vipType": "ignore",
                    "vipVariableName": "system_device_groups"
                },
                "controller-group-list": {
                    "vipObjectType": "list",
                    "vipType": "ignore",
                    "vipVariableName": "system_controller_group_list"
                },
                "eco-friendly-mode": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "false",
                    "vipVariableName": "system_eco_friendly_mode"
                },
                "site-id": {
                    "vipObjectType": "object",
                    "vipType": "variableName",
                    "vipValue": "",
                    "vipVariableName": "system_site_id"
                },
                "overlay-id": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": 1,
                    "vipVariableName": "system_overlay_id"
                },
                "system-ip": {
                    "vipObjectType": "object",
                    "vipType": "variableName",
                    "vipValue": "",
                    "vipVariableName": "system_system_ip"
                },
                "host-name": {
                    "vipObjectType": "object",
                    "vipType": "variableName",
                    "vipValue": "",
                    "vipVariableName": "system_host_name"
                },
                "console-baud-rate": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": "9600",
                    "vipVariableName": "system_console_baud_rate"
                },
                "max-omp-sessions": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "system_max_omp_sessions"
                },
                "usb-controller": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "false",
                    "vipVariableName": "system_usb_controller"
                },
                "track-default-gateway": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "true",
                    "vipVariableName": "system_track_default_gateway"
                },
                "multicast-buffer-percent": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": 20,
                    "vipVariableName": "system_multicast_buffer_percent"
                },
                "host-policer-pps": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": 20000,
                    "vipVariableName": "system_host_policer_pps"
                },
                "icmp-error-pps": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": 100,
                    "vipVariableName": "system_icmp_error_pps"
                },
                "allow-same-site-tunnels": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "false",
                    "vipVariableName": "system_allow_same_site_tunnels"
                },
                "route-consistency-check": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "false",
                    "vipVariableName": "system_route_consistency_check"
                },
                "idle-timeout": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "system_idle-timeout"
                },
                "admin-tech-on-failure": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "true",
                    "vipVariableName": "system_admin_tech_on_failure"
                },
                "tracker": {
                    "vipType": "ignore",
                    "vipValue": [],
                    "vipObjectType": "tree",
                    "vipPrimaryKey": [
                        "name"
                    ]
                }
            },
            "transitionInProgress": true,
            "viewMode": "add",
            "deviceType": [
                "vedge-cloud",
                "vedge-CSR-1000v",
                "vedge-1000",
                "vedge-2000",
                "vedge-100",
                "vedge-100-B",
                "vedge-100-WM",
                "vedge-100-M",
                "vedge-5000",
                "vedge-ISR-4331",
                "vedge-ISR-4321",
                "vedge-ISR-4351",
                "vedge-ISR-4221",
                "vedge-ISR-4221X",
                "vedge-ISR-4431",
                "vedge-ISR-4451-X",
                "vedge-ASR-1001-HX",
                "vedge-ASR-1002-X",
                "vedge-ASR-1002-HX",
                "vedge-C1111-8P",
                "vedge-C1111X-8P",
                "vedge-C1111-8PLTEEA",
                "vedge-C1111-8PLTELA",
                "vedge-C1117-4PLTEEA",
                "vedge-C1117-4PLTELA",
                "vedge-ISRv",
                "vedge-ASR-1001-X",
                "vedge-C1101-4P",
                "vedge-C1101-4PLTEP",
                "vedge-C1111-4P",
                "vedge-C1111-8PW",
                "vedge-C1111-8PLTEEAW",
                "vedge-C1111-4PLTEEA",
                "vedge-C1111-4PLTELA",
                "vedge-C1116-4P",
                "vedge-C1116-4PLTEEA",
                "vedge-C1117-4P",
                "vedge-C1117-4PM",
                "vedge-C1117-4PMLTEEA"
            ],
            "deviceModels": [
                {
                    "name": "vedge-ASR-1001-HX",
                    "displayName": "ASR1001-HX",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ASR-1001-X",
                    "displayName": "ASR1001-X",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ASR-1002-HX",
                    "displayName": "ASR1002-HX",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ASR-1002-X",
                    "displayName": "ASR1002-X",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1101-4P",
                    "displayName": "C1101-4P",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1101-4PLTEP",
                    "displayName": "C1101-4PLTEP",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1111-4P",
                    "displayName": "C1111-4P",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1111-4PLTEEA",
                    "displayName": "C1111-4PLTEEA",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1111-4PLTELA",
                    "displayName": "C1111-4PLTELA",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1111-8P",
                    "displayName": "C1111-8P",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1111-8PLTEEA",
                    "displayName": "C1111-8PLTEEA",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1111-8PLTEEAW",
                    "displayName": "C1111-8PLTEEAW",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1111-8PLTELA",
                    "displayName": "C1111-8PLTELA",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1111-8PW",
                    "displayName": "C1111-8PW",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1111X-8P",
                    "displayName": "C1111X-8P",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1116-4P",
                    "displayName": "C1116-4P",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1116-4PLTEEA",
                    "displayName": "C1116-4PLTEEA",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1117-4P",
                    "displayName": "C1117-4P",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1117-4PLTEEA",
                    "displayName": "C1117-4PLTEEA",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1117-4PLTELA",
                    "displayName": "C1117-4PLTELA",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1117-4PM",
                    "displayName": "C1117-4PM",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-C1117-4PMLTEEA",
                    "displayName": "C1117-4PMLTEEA",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-CSR-1000v",
                    "displayName": "CSR1000v",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ISR-4221",
                    "displayName": "ISR4221",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ISR-4221X",
                    "displayName": "ISR4221X",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ISR-4321",
                    "displayName": "ISR4321",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ISR-4331",
                    "displayName": "ISR4331",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ISR-4351",
                    "displayName": "ISR4351",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ISR-4431",
                    "displayName": "ISR4431",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ISR-4451-X",
                    "displayName": "ISR4451-X",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-ISRv",
                    "displayName": "ISRv",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
                },
                {
                    "name": "vedge-100",
                    "displayName": "vEdge 100",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vedge-100-B",
                    "displayName": "vEdge 100 B",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vedge-100-M",
                    "displayName": "vEdge 100 M",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vedge-100-WM",
                    "displayName": "vEdge 100 WM",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vedge-1000",
                    "displayName": "vEdge 1000",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vedge-2000",
                    "displayName": "vEdge 2000",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vedge-5000",
                    "displayName": "vEdge 5000",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vedge-cloud",
                    "displayName": "vEdge Cloud",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                }
            ],
            "templateUrl": "/app/configuration/template/feature/templates/system-vedge-15.0.0.html",
            "factoryDefault": false
        }"""
