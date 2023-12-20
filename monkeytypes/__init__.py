"""
Used for a common things between agent and island
"""
from .operating_system import OperatingSystem

from .base_models import (
    InfectionMonkeyBaseModel,
    InfectionMonkeyModelConfig,
    MutableInfectionMonkeyBaseModel,
    MutableInfectionMonkeyModelConfig,
    IllegalMutationError,
    INVALID_UNION_MEMBER_ERROR,
)
from .agent_plugin_type import AgentPluginType
from .agent_plugin_manifest import PluginName, PluginVersion, AgentPluginManifest
from .concurrency import BasicLock, Event, Lock, RLock
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
from .network_range import InvalidNetworkRangeError, NetworkRange, CidrRange, IpRange, SingleIpRange

from .credentials.email_address import EmailAddress
from .credentials.username import Username

from .credentials.lm_hash import LMHash
from .credentials.nt_hash import NTHash
from .credentials.password import Password
from .credentials.ssh_keypair import SSHKeypair

from .credentials.encoding import get_plaintext

from .credentials.credentials import Credentials, CredentialsComponent, Identity, Secret
