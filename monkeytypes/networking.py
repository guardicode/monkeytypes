from __future__ import annotations

from enum import Enum
from ipaddress import IPv4Address

from pydantic import Field
from typing_extensions import Annotated

from monkeytypes import InfectionMonkeyBaseModel


class NetworkProtocol(Enum):
    """
    An Enum representing network protocols

    This Enum represents network protocols. The value of each
    member is the member's name in all lower-case characters.
    """

    TCP = "tcp"
    UDP = "udp"
    ICMP = "icmp"
    UNKNOWN = "unknown"


class NetworkService(Enum):
    """
    An Enum representing network services

    This Enum represents all network services that Infection Monkey supports. The value of each
    member is the member's name in all lower-case characters.
    """

    HTTP = "http"
    HTTPS = "https"
    MSSQL = "mssql"
    SMB = "smb"
    SSH = "ssh"
    MSSQL_BROWSER = "mssql_browser"
    UNKNOWN = "unknown"


NetworkPort = Annotated[int, Field(ge=0, le=65535)]


class PortStatus(Enum):
    """
    An Enum representing the status of the port.

    This Enum represents the status of a network pork. The value of each
    member is the member's name in all lower-case characters.
    """

    OPEN = "open"
    CLOSED = "closed"


class SocketAddress(InfectionMonkeyBaseModel):
    ip: IPv4Address
    port: NetworkPort

    @classmethod
    def from_string(cls, address_str: str) -> SocketAddress:
        """
        Parse a SocketAddress object from a string

        :param address_str: A string of ip:port
        :raises ValueError: If the string is not a valid ip:port
        :return: SocketAddress with the IP and port
        """
        ip, port = address_str.split(":")

        return SocketAddress(ip=IPv4Address(ip), port=NetworkPort(port))

    def __hash__(self) -> int:
        return hash(str(self))

    def __str__(self) -> str:
        return f"{self.ip}:{self.port}"


class DiscoveredService(InfectionMonkeyBaseModel):
    protocol: NetworkProtocol
    port: NetworkPort
    service: NetworkService

    def __hash__(self) -> int:
        return hash((self.protocol, self.port))
