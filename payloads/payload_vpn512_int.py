class data:
    def __init__(self):
        self.payload = """
        {
            "templateName": "VPN512-Interface",
            "templateDescription": "VPN512 (mgmt) Interface for all routers",
            "templateType": "vpn-vedge-interface",
            "templateMinVersion": "15.0.0",
            "templateDefinition": {
                "if-name": {
                    "vipObjectType": "object",
                    "vipType": "variableName",
                    "vipValue": "",
                    "vipVariableName": "vpn512_if_name"
                },
                "description": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": "Management",
                    "vipVariableName": "vpn_if_description"
                },
                "ip": {
                    "address": {
                        "vipObjectType": "object",
                        "vipType": "variableName",
                        "vipValue": "",
                        "vipVariableName": "vpn512_if_ipv4_address"
                    },
                    "secondary-address": {
                        "vipType": "ignore",
                        "vipValue": [],
                        "vipObjectType": "tree",
                        "vipPrimaryKey": [
                            "address"
                        ]
                    }
                },
                "dhcp-helper": {
                    "vipObjectType": "list",
                    "vipType": "ignore",
                    "vipVariableName": "vpn_if_dhcp_helper"
                },
                "flow-control": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "autoneg",
                    "vipVariableName": "vpn_if_flow_control"
                },
                "clear-dont-fragment": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "false",
                    "vipVariableName": "vpn_if_clear_dont_fragment"
                },
                "pmtu": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "false",
                    "vipVariableName": "vpn_if_pmtu"
                },
                "mtu": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": 1500,
                    "vipVariableName": "vpn_if_ip_mtu"
                },
                "static-ingress-qos": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "vpn_if_static_ingress_qos"
                },
                "tcp-mss-adjust": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "vpn_if_tcp_mss_adjust"
                },
                "mac-address": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "vpn_if_mac_address"
                },
                "speed": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "_empty",
                    "vipVariableName": "vpn_if_speed"
                },
                "duplex": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "_empty",
                    "vipVariableName": "vpn_if_duplex"
                },
                "shutdown": {
                    "vipObjectType": "object",
                    "vipType": "constant",
                    "vipValue": "false",
                    "vipVariableName": "vpn_if_shutdown"
                },
                "arp-timeout": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": 1200,
                    "vipVariableName": "vpn_if_arp_timeout"
                },
                "autonegotiate": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "true",
                    "vipVariableName": "vpn_if_autonegotiate"
                },
                "shaping-rate": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "qos_shaping_rate"
                },
                "qos-map": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "qos_map"
                },
                "tracker": {
                    "vipObjectType": "list",
                    "vipType": "ignore",
                    "vipVariableName": "vpn_if_tracker"
                },
                "bandwidth-upstream": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "vpn_if_bandwidth_upstream"
                },
                "bandwidth-downstream": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "vpn_if_bandwidth_downstream"
                },
                "block-non-source-ip": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "false",
                    "vipVariableName": "vpn_if_block_non_source_ip"
                },
                "rewrite-rule": {
                    "rule-name": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipVariableName": "rewrite_rule_name"
                    }
                },
                "tloc-extension": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipVariableName": "vpn_if_tloc_extension"
                },
                "icmp-redirect-disable": {
                    "vipObjectType": "object",
                    "vipType": "ignore",
                    "vipValue": "false",
                    "vipVariableName": "vpn_if_icmp_redirect_disable"
                },
                "tloc-extension-gre-from": {
                    "src-ip": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipVariableName": "vpn_if_tloc-ext_gre_from_src_ip"
                    },
                    "xconnect": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipVariableName": "vpn_if_tloc-ext_gre_from_xconnect"
                    }
                },
                "access-list": {
                    "vipType": "ignore",
                    "vipValue": [],
                    "vipObjectType": "tree",
                    "vipPrimaryKey": [
                        "direction"
                    ]
                },
                "policer": {
                    "vipType": "ignore",
                    "vipValue": [],
                    "vipObjectType": "tree",
                    "vipPrimaryKey": [
                        "policer-name",
                        "direction"
                    ]
                },
                "ipv6": {
                    "access-list": {
                        "vipType": "ignore",
                        "vipValue": [],
                        "vipObjectType": "tree",
                        "vipPrimaryKey": [
                            "direction"
                        ]
                    },
                    "address": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipValue": "",
                        "vipVariableName": "vpn_if_ipv6_ipv6_address"
                    },
                    "dhcp-helper-v6": {
                        "vipType": "ignore",
                        "vipValue": [],
                        "vipObjectType": "tree",
                        "vipPrimaryKey": [
                            "address"
                        ]
                    },
                    "secondary-address": {
                        "vipType": "ignore",
                        "vipValue": [],
                        "vipObjectType": "tree",
                        "vipPrimaryKey": [
                            "address"
                        ]
                    }
                },
                "arp": {
                    "ip": {
                        "vipType": "ignore",
                        "vipValue": [],
                        "vipObjectType": "tree",
                        "vipPrimaryKey": [
                            "addr"
                        ]
                    }
                },
                "vrrp": {
                    "vipType": "ignore",
                    "vipValue": [],
                    "vipObjectType": "tree",
                    "vipPrimaryKey": [
                        "grp-id"
                    ]
                },
                "ipv6-vrrp": {
                    "vipType": "ignore",
                    "vipValue": [],
                    "vipObjectType": "tree",
                    "vipPrimaryKey": [
                        "grp-id"
                    ]
                },
                "dot1x": {
                    "vipType": "ignore",
                    "vipObjectType": "node-only"
                }
            },
            "transitionInProgress": true,
            "secAddrIndex": 0,
            "secondaryIpv6AddrIndex": 0,
            "dhcpHelperv6Indx": 0,
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
            "templateUrl": "/app/configuration/template/feature/templates/vpn-vedge-interface-15.0.0.html",
            "factoryDefault": false
        }
        """
