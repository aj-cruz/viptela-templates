class data:
    def __init__(self):
        self.payload = """
        {
            "templateName": "NTP-Template",
            "templateDescription": "Global NTP Template",
            "templateType": "ntp",
            "templateMinVersion": "15.0.0",
            "templateDefinition": {
                "keys": {
                    "trusted": {
                        "vipObjectType": "list",
                        "vipType": "ignore",
                        "vipVariableName": "trusted_key"
                    }
                },
                "server": {
                    "vipType": "constant",
                    "vipValue": [
                        {
                            "name": {
                                "vipObjectType": "object",
                                "vipType": "variableName",
                                "vipValue": "",
                                "vipVariableName": "ntp_server_host1"
                            },
                            "key": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipVariableName": "ntp_server_server_auth_key"
                            },
                            "vpn": {
                                "vipObjectType": "object",
                                "vipType": "constant",
                                "vipValue": 0,
                                "vipVariableName": "ntp_server_vpn"
                            },
                            "version": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": 4,
                                "vipVariableName": "ntp_server_version"
                            },
                            "source-interface": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipVariableName": "ntp_server_source_interface"
                            },
                            "prefer": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": "false",
                                "vipVariableName": "ntp_server_prefer"
                            },
                            "priority-order": [
                                "name",
                                "key",
                                "vpn",
                                "version",
                                "source-interface",
                                "prefer"
                            ],
                            "vipOptional": true
                        },
                        {
                            "name": {
                                "vipObjectType": "object",
                                "vipType": "variableName",
                                "vipValue": "",
                                "vipVariableName": "ntp_server_host2"
                            },
                            "key": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipVariableName": "ntp_server_server_auth_key"
                            },
                            "vpn": {
                                "vipObjectType": "object",
                                "vipType": "constant",
                                "vipValue": 0,
                                "vipVariableName": "ntp_server_vpn"
                            },
                            "version": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": 4,
                                "vipVariableName": "ntp_server_version"
                            },
                            "source-interface": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipVariableName": "ntp_server_source_interface"
                            },
                            "prefer": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": "false",
                                "vipVariableName": "ntp_server_prefer"
                            },
                            "priority-order": [
                                "name",
                                "key",
                                "vpn",
                                "version",
                                "source-interface",
                                "prefer"
                            ],
                            "vipOptional": true
                        }
                    ],
                    "vipObjectType": "tree",
                    "vipPrimaryKey": [
                        "name"
                    ]
                }
            },
            "transitionInProgress": false,
            "templateId": "bd78f083-dfe4-408e-9593-76cd434c24e4",
            "viewMode": "edit",
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
                "vedge-C1117-4PMLTEEA",
                "vmanage",
                "vsmart"
            ],
            "lastUpdatedBy": "admin",
            "editedTemplateDefinition": {
                "keys": {
                    "trusted": {
                        "vipObjectType": "list",
                        "vipType": "ignore",
                        "vipVariableName": "trusted_key"
                    }
                },
                "server": {
                    "vipType": "constant",
                    "vipValue": [
                        {
                            "name": {
                                "vipObjectType": "object",
                                "vipType": "variableName",
                                "vipValue": "",
                                "vipVariableName": "ntp_server_host1"
                            },
                            "key": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipVariableName": "ntp_server_server_auth_key"
                            },
                            "vpn": {
                                "vipObjectType": "object",
                                "vipType": "constant",
                                "vipValue": 0,
                                "vipVariableName": "ntp_server_vpn"
                            },
                            "version": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": 4,
                                "vipVariableName": "ntp_server_version"
                            },
                            "source-interface": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipVariableName": "ntp_server_source_interface"
                            },
                            "prefer": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": "false",
                                "vipVariableName": "ntp_server_prefer"
                            },
                            "priority-order": [
                                "name",
                                "key",
                                "vpn",
                                "version",
                                "source-interface",
                                "prefer"
                            ]
                        },
                        {
                            "name": {
                                "vipObjectType": "object",
                                "vipType": "variableName",
                                "vipValue": "",
                                "vipVariableName": "ntp_server_host2"
                            },
                            "key": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipVariableName": "ntp_server_server_auth_key"
                            },
                            "vpn": {
                                "vipObjectType": "object",
                                "vipType": "constant",
                                "vipValue": 0,
                                "vipVariableName": "ntp_server_vpn"
                            },
                            "version": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": 4,
                                "vipVariableName": "ntp_server_version"
                            },
                            "source-interface": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipVariableName": "ntp_server_source_interface"
                            },
                            "prefer": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": "false",
                                "vipVariableName": "ntp_server_prefer"
                            },
                            "priority-order": [
                                "name",
                                "key",
                                "vpn",
                                "version",
                                "source-interface",
                                "prefer"
                            ]
                        }
                    ],
                    "vipObjectType": "tree",
                    "vipPrimaryKey": [
                        "name"
                    ]
                }
            },
            "configType": "xml",
            "attachedMastersCount": 1,
            "createdOn": 1587169225673,
            "@rid": 377,
            "feature": "vmanage-default",
            "factoryDefault": false,
            "createdBy": "admin",
            "devicesAttached": 0,
            "lastUpdatedOn": 1587169225673,
            "httpResponseHeader": {
                "cache-control": "no-cache, no-store, must-revalidate",
                "connection": "keep-alive",
                "content-encoding": "gzip",
                "content-length": "725",
                "content-type": "application/json",
                "date": "Sat, 18 Apr 2020 00:27:41 GMT",
                "strict-transport-security": "max-age=31536000; includeSubDomains",
                "vary": "Accept-Encoding",
                "x-content-type-options": "nosniff",
                "x-frame-options": "DENY",
                "x-xss-protection": "1; mode=block"
            },
            "deviceModels": [
                {
                    "name": "vedge-cloud",
                    "displayName": "vEdge Cloud",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vedge-CSR-1000v",
                    "displayName": "CSR1000v",
                    "deviceType": "vedge",
                    "isCliSupported": false,
                    "isCiscoDeviceModel": true
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
                    "name": "vedge-100-WM",
                    "displayName": "vEdge 100 WM",
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
                    "name": "vedge-5000",
                    "displayName": "vEdge 5000",
                    "deviceType": "vedge",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vedge-ISR-4331",
                    "displayName": "ISR4331",
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
                    "name": "vedge-ISR-4351",
                    "displayName": "ISR4351",
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
                    "name": "vedge-ASR-1001-HX",
                    "displayName": "ASR1001-HX",
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
                    "name": "vedge-ASR-1002-HX",
                    "displayName": "ASR1002-HX",
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
                    "name": "vedge-C1111X-8P",
                    "displayName": "C1111X-8P",
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
                    "name": "vedge-C1111-8PLTELA",
                    "displayName": "C1111-8PLTELA",
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
                    "name": "vedge-ISRv",
                    "displayName": "ISRv",
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
                    "name": "vedge-C1111-8PW",
                    "displayName": "C1111-8PW",
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
                    "name": "vmanage",
                    "displayName": "vManage",
                    "deviceType": "vmanage",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                },
                {
                    "name": "vsmart",
                    "displayName": "vSmart",
                    "deviceType": "vsmart",
                    "isCliSupported": true,
                    "isCiscoDeviceModel": false
                }
            ],
            "templateUrl": "/app/configuration/template/feature/templates/ntp-15.0.0.html"
        }
        """
