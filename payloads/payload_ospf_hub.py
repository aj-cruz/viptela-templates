class data:
    def __init__(self):
        self.payload = """
        {
            "templateName": "OSPF-HUB",
            "templateDescription": "OSPF Template for hub routers",
            "templateType": "ospf",
            "templateMinVersion": "15.0.0",
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
            "templateUrl": "/app/configuration/template/feature/templates/ospf-15.0.0.html",
            "removeTableRow": {},
            "templateDefinition": {
                "ospf": {
                    "router-id": {
                        "vipObjectType": "object",
                        "vipType": "ignore",
                        "vipVariableName": "ospf_router_id"
                    },
                    "auto-cost": {
                        "reference-bandwidth": {
                            "vipObjectType": "object",
                            "vipType": "constant",
                            "vipValue": 10000,
                            "vipVariableName": "ospf_reference_bandwidth"
                        }
                    },
                    "compatible": {
                        "rfc1583": {
                            "vipObjectType": "object",
                            "vipType": "ignore",
                            "vipValue": "true",
                            "vipVariableName": "ospf_rfc1583"
                        }
                    },
                    "distance": {
                        "external": {
                            "vipObjectType": "object",
                            "vipType": "ignore",
                            "vipValue": 110,
                            "vipVariableName": "ospf_distance_external"
                        },
                        "inter-area": {
                            "vipObjectType": "object",
                            "vipType": "ignore",
                            "vipValue": 110,
                            "vipVariableName": "ospf_distance_inter_area"
                        },
                        "intra-area": {
                            "vipObjectType": "object",
                            "vipType": "ignore",
                            "vipValue": 110,
                            "vipVariableName": "ospf_distance_intra_area"
                        }
                    },
                    "timers": {
                        "spf": {
                            "delay": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": 200,
                                "vipVariableName": "ospf_delay"
                            },
                            "initial-hold": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": 1000,
                                "vipVariableName": "ospf_initial_hold"
                            },
                            "max-hold": {
                                "vipObjectType": "object",
                                "vipType": "ignore",
                                "vipValue": 10000,
                                "vipVariableName": "ospf_max_hold"
                            }
                        }
                    },
                    "redistribute": {
                        "vipType": "constant",
                        "vipValue": [
                            {
                                "protocol": {
                                    "vipObjectType": "object",
                                    "vipType": "constant",
                                    "vipValue": "omp",
                                    "vipVariableName": "ospf_redistribute_protocol"
                                },
                                "route-policy": {
                                    "vipObjectType": "object",
                                    "vipType": "ignore",
                                    "vipVariableName": "ospf_redistribute_route_policy"
                                },
                                "priority-order": [
                                    "protocol",
                                    "route-policy"
                                ]
                            }
                        ],
                        "vipObjectType": "tree",
                        "vipPrimaryKey": [
                            "protocol"
                        ]
                    },
                    "max-metric": {
                        "router-lsa": {
                            "vipType": "ignore",
                            "vipValue": [],
                            "vipObjectType": "tree",
                            "vipPrimaryKey": [
                                "ad-type"
                            ]
                        }
                    },
                    "area": {
                        "vipType": "constant",
                        "vipValue": [
                            {
                                "a-num": {
                                    "originalDefaultOption": "constant",
                                    "dataPath": [],
                                    "vipObjectType": "object",
                                    "vipType": "variableName",
                                    "vipVariableName": "ospf_hub_vpn10_area_num",
                                    "vipValue": ""
                                },
                                "stub": {
                                    "no-summary": {
                                        "vipType": "ignore",
                                        "vipObjectType": "node-only"
                                    }
                                },
                                "nssa": {
                                    "no-summary": {
                                        "vipType": "ignore",
                                        "vipObjectType": "node-only"
                                    },
                                    "translate": {
                                        "vipType": "ignore",
                                        "vipObjectType": "object"
                                    }
                                },
                                "interface": {
                                    "vipType": "constant",
                                    "vipValue": [
                                        {
                                            "name": {
                                                "originalDefaultOption": "constant",
                                                "dataPath": [],
                                                "vipObjectType": "object",
                                                "vipType": "variableName",
                                                "vipVariableName": "ospf_hub_vpn10_if_name",
                                                "vipValue": ""
                                            },
                                            "hello-interval": {
                                                "originalDefaultOption": "ignore",
                                                "dataPath": [],
                                                "vipObjectType": "object",
                                                "vipValue": 1,
                                                "vipType": "constant",
                                                "vipVariableName": "ospf_hello_interval"
                                            },
                                            "dead-interval": {
                                                "originalDefaultOption": "ignore",
                                                "dataPath": [],
                                                "vipObjectType": "object",
                                                "vipValue": 4,
                                                "vipType": "constant",
                                                "vipVariableName": "ospf_dead_interval"
                                            },
                                            "retransmit-interval": {
                                                "originalDefaultOption": "ignore",
                                                "dataPath": [],
                                                "vipObjectType": "object",
                                                "vipValue": 3,
                                                "vipType": "constant",
                                                "vipVariableName": "ospf_retransmit_interval"
                                            },
                                            "cost": {
                                                "originalDefaultOption": "ignore",
                                                "dataPath": [],
                                                "vipObjectType": "object",
                                                "vipType": "ignore",
                                                "vipVariableName": "ospf_cost"
                                            },
                                            "priority": {
                                                "originalDefaultOption": "ignore",
                                                "dataPath": [],
                                                "vipObjectType": "object",
                                                "vipValue": 1,
                                                "vipType": "ignore",
                                                "vipVariableName": "ospf_priority"
                                            },
                                            "network": {
                                                "originalDefaultOption": "ignore",
                                                "dataPath": [],
                                                "vipObjectType": "object",
                                                "vipValue": "broadcast",
                                                "vipType": "ignore",
                                                "vipVariableName": "ospf_network"
                                            },
                                            "passive-interface": {
                                                "originalDefaultOption": "ignore",
                                                "dataPath": [],
                                                "vipObjectType": "node-only",
                                                "vipValue": "false",
                                                "vipType": "ignore",
                                                "vipVariableName": "ospf_passive_interface"
                                            },
                                            "authentication": {
                                                "type": {
                                                    "vipObjectType": "object",
                                                    "vipType": "ignore",
                                                    "vipValue": "_empty",
                                                    "vipVariableName": "ospf_authentication_type"
                                                },
                                                "authentication-key": {
                                                    "vipObjectType": "object",
                                                    "vipType": "ignore",
                                                    "vipValue": "",
                                                    "vipVariableName": "ospf_authentication_key"
                                                },
                                                "message-digest": {
                                                    "message-digest-key": {
                                                        "vipObjectType": "object",
                                                        "vipType": "ignore",
                                                        "vipValue": "",
                                                        "vipVariableName": "ospf_message_digest_key"
                                                    },
                                                    "md5": {
                                                        "vipObjectType": "object",
                                                        "vipType": "ignore",
                                                        "vipValue": "",
                                                        "vipVariableName": "ospf_md5"
                                                    }
                                                }
                                            },
                                            "priority-order": [
                                                "name",
                                                "hello-interval",
                                                "dead-interval",
                                                "retransmit-interval",
                                                "cost",
                                                "priority",
                                                "network",
                                                "passive-interface",
                                                "authentication"
                                            ]
                                        }
                                    ],
                                    "vipObjectType": "tree",
                                    "vipPrimaryKey": [
                                        "name"
                                    ]
                                },
                                "priority-order": [
                                    "a-num",
                                    "interface"
                                ]
                            }
                        ],
                        "vipObjectType": "tree",
                        "vipPrimaryKey": [
                            "a-num"
                        ]
                    }
                }
            },
            "factoryDefault": false
        }
        """
