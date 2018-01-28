from enum import Enum

class Protocol(Enum):
    HTTP = 1,
    ICMP = 2,
    SMTP = 3,
    DNS = 4,
    ALL = 5

machines = {
    "192.168.0.4": {
        "users": [
            {
                "username": "jaywon",
                "password": "taco",
                "groups": [
                    "sudo",
                    "admin"
                ]
            },
        ],
        "commands": {
            "nmap": {
                "groups": [
                    "sudo",
                    "admin"
                ]
            },
            "nc": {
                "groups": [
                    "sudo",
                    "networkers"
                ]
            }
        },
        "history": [
            "ls",
            "cd ~/passwords/",
            "cat supersecret.txt",
            "ssh dave@123.45.67.89"
        ],
        "processes": [
            "firewall"
        ],
        "firewall_rules": {
            "allow": [
                {
                    "port": 80,
                    "protocol": Protocol.HTTP
                },
                {
                    "port": 1384,
                    "protocol": Protocol.ICMP
                }
            ],
            "deny": [
                {
                    "port": 443,
                    "protocol": Protocol.ALL
                }
            ]
        },
        "directories": {
            "/": {
               "etc": "",
               "var": ""
            }
        }
    },
    "192.168.0.14": {
        "users": [
            {
                "username": "tyler",
                "password": "hax0r",
                "groups": [
                    "sudo",
                    "admin"
                ]
            },
        ],
        "commands": {
            "nc": {
                "groups": [
                    "sudo",
                    "networkers"
                ]
            },
            "wireshark": {
                "groups": [
                    "sudo",
                    "networkers"
                ]
            }
        },
        "history": [
            "ls",
            "cd ~/passwords/",
            "cat supersecret.txt",
            "ssh dave@123.45.67.89"
        ],
        "processes": [
            "firewall"
        ],
        "firewall_rules": {
            "allow": [
                {
                    "port": 80,
                    "protocol": Protocol.HTTP
                },
                {
                    "port": 1384,
                    "protocol": Protocol.ICMP
                }
            ],
            "deny": [
                {
                    "port": 443,
                    "protocol": Protocol.ALL
                }
            ]
        },
        "directories": {
            "/": {
               "etc": "",
               "var": ""
            }
        }
    }
}
