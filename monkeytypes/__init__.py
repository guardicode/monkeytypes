"""
Used for a common things between agent and island
"""
from .operating_system import OperatingSystem
from . import base_models
from .agent_plugin_type import AgentPluginType
from .agent_plugin_manifest import PluginName, PluginVersion, AgentPluginManifest
from .concurrency import Lock, Event
from .serialization import JSONSerializable
from .ids import AgentID, HardwareID, MachineID
from .int_range import IntRange
from .networking import (
    NetworkService,
    NetworkPort,
    PortStatus,
    SocketAddress,
    NetworkProtocol,
    DiscoveredService,
)
from .secrets import OTP, Token
from .file_extension import FileExtension
from .percent import Percent, PercentLimited, NonNegativeFloat
from .b64_bytes import B64Bytes
