import json
import requests
import sys

def register_ue(webconsole_ipaddress, mnc, mcc, msin):
    def raise_for_status(r):
        http_error_msg = ''
        if 400 <= r.status_code < 500:
            http_error_msg = '%s Client Error: %s' % (r.status_code, r.reason)

        elif 500 <= r.status_code < 600:
            http_error_msg = '%s Server Error: %s' % (r.status_code, r.reason)

        return http_error_msg

    payload = {
        "plmnID": "%s%s" % (mcc, mnc),
        "ueId": "imsi-%s%s%s" % (mcc, mnc, msin),
        "AuthenticationSubscription": {
          "authenticationMethod": "5G_AKA",
          "permanentKey": {
            "permanentKeyValue": "8baf473f2f8fd09487cccbd7097c6862",
            "encryptionKey": 0,
            "encryptionAlgorithm": 0
          },
          "sequenceNumber": "16f3b3f70fc2",
          "authenticationManagementField": "8000",
          "milenage": {
            "op": {
              "opValue": "",
              "encryptionKey": 0,
              "encryptionAlgorithm": 0
            }
          },
          "opc": {
            "opcValue": "8e27b6af0e692e750f32667a3b14605d",
            "encryptionKey": 0,
            "encryptionAlgorithm": 0
          }
        },
        "AccessAndMobilitySubscriptionData": {
          "gpsis": [
            "msisdn-0900000000"
          ],
          "subscribedUeAmbr": {
            "uplink": "1 Gbps",
            "downlink": "2 Gbps"
          },
          "nssai": {
            "defaultSingleNssais": [
              {
                "sst": 1,
                "sd": "010203"
              },
              {
                "sst": 1,
                "sd": "112233"
              }
            ]
          }
        },
        "SessionManagementSubscriptionData": [
          {
            "singleNssai": {
              "sst": 1,
              "sd": "010203"
            },
            "dnnConfigurations": {
              "internet": {
                "pduSessionTypes": {
                  "defaultSessionType": "IPV4",
                  "allowedSessionTypes": [
                    "IPV4"
                  ]
                },
                "sscModes": {
                  "defaultSscMode": "SSC_MODE_1",
                  "allowedSscModes": [
                    "SSC_MODE_2",
                    "SSC_MODE_3"
                  ]
                },
                "5gQosProfile": {
                  "5qi": 9,
                  "arp": {
                    "priorityLevel": 8,
                    "preemptCap": "",
                    "preemptVuln": ""
                  },
                  "priorityLevel": 8
                },
                "sessionAmbr": {
                  "uplink": "200 Mbps",
                  "downlink": "200 Mbps"
                }
              },
              "internet2": {
                "pduSessionTypes": {
                  "defaultSessionType": "IPV4",
                  "allowedSessionTypes": [
                    "IPV4"
                  ]
                },
                "sscModes": {
                  "defaultSscMode": "SSC_MODE_1",
                  "allowedSscModes": [
                    "SSC_MODE_2",
                    "SSC_MODE_3"
                  ]
                },
                "5gQosProfile": {
                  "5qi": 9,
                  "arp": {
                    "priorityLevel": 8,
                    "preemptCap": "",
                    "preemptVuln": ""
                  },
                  "priorityLevel": 8
                },
                "sessionAmbr": {
                  "uplink": "200 Mbps",
                  "downlink": "200 Mbps"
                }
              }
            }
          },
          {
            "singleNssai": {
              "sst": 1,
              "sd": "112233"
            },
            "dnnConfigurations": {
              "internet": {
                "pduSessionTypes": {
                  "defaultSessionType": "IPV4",
                  "allowedSessionTypes": [
                    "IPV4"
                  ]
                },
                "sscModes": {
                  "defaultSscMode": "SSC_MODE_1",
                  "allowedSscModes": [
                    "SSC_MODE_2",
                    "SSC_MODE_3"
                  ]
                },
                "5gQosProfile": {
                  "5qi": 9,
                  "arp": {
                    "priorityLevel": 8,
                    "preemptCap": "",
                    "preemptVuln": ""
                  },
                  "priorityLevel": 8
                },
                "sessionAmbr": {
                  "uplink": "512 Mbps",
                  "downlink": "512 Mbps"
                }
              },
              "internet2": {
                "pduSessionTypes": {
                  "defaultSessionType": "IPV4",
                  "allowedSessionTypes": [
                    "IPV4"
                  ]
                },
                "sscModes": {
                  "defaultSscMode": "SSC_MODE_1",
                  "allowedSscModes": [
                    "SSC_MODE_2",
                    "SSC_MODE_3"
                  ]
                },
                "5gQosProfile": {
                  "5qi": 9,
                  "arp": {
                    "priorityLevel": 8,
                    "preemptCap": "",
                    "preemptVuln": ""
                  },
                  "priorityLevel": 8
                },
                "sessionAmbr": {
                  "uplink": "512 Mbps",
                  "downlink": "512 Mbps"
                }
              }
            }
          }
        ],
        "SmfSelectionSubscriptionData": {
          "subscribedSnssaiInfos": {
            "01010203": {
              "dnnInfos": [
                {
                  "dnn": "internet"
                },
                {
                  "dnn": "internet2"
                }
              ]
            },
            "01112233": {
              "dnnInfos": [
                {
                  "dnn": "internet"
                },
                {
                  "dnn": "internet2"
                }
              ]
            }
          }
        },
        "AmPolicyData": {
          "subscCats": [
            "free5gc"
          ]
        },
        "SmPolicyData": {
          "smPolicySnssaiData": {
            "01010203": {
              "snssai": {
                "sst": 1,
                "sd": "010203"
              },
              "smPolicyDnnData": {
                "internet": {
                  "dnn": "internet"
                },
                "internet2": {
                  "dnn": "internet2"
                }
              }
            },
            "01112233": {
              "snssai": {
                "sst": 1,
                "sd": "112233"
              },
              "smPolicyDnnData": {
                "internet": {
                  "dnn": "internet"
                },
                "internet2": {
                  "dnn": "internet2"
                }
              }
            }
          }
        },
        "FlowRules": None
      }

    plmn = payload['plmnID']
    supi = payload['ueId']

    #curl -v http://172.15.0.150:30050/api/subscriber/imsi-208930000000003/20893 -H "Token: admin"
    headers = {'Content-Type': 'application/json', 'Token': 'admin'}
    r = requests.post("http://%s:5000/api/subscriber/%s/%s" % (webconsole_ipaddress, supi, plmn),
        json=payload, headers=headers)
    sys.stdout.write('r.text [%s]\n' % r.text)

    error_msg = raise_for_status(r)
    if error_msg:
        raise Exception('%s. %s' % (error_msg, r.text))

if __name__ == "__main__":
    webconsole_ipaddress = "172.15.0.208"
    
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000001')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000002')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000003')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000004')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000005')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000006')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000007')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000008')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000009')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000010')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000011')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000012')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000013')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000014')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000015')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000016')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000017')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000018')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000019')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000020')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000021')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000022')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000023')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000024')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000025')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000026')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000027')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000028')
    register_ue(webconsole_ipaddress=webconsole_ipaddress, mnc='93', mcc='208', msin='0000000029')
