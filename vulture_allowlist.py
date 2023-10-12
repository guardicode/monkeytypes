from monkeytypes import (
    OTP,
    AgentID,
    AgentPluginManifest,
    AgentPluginType,
    B64Bytes,
    BasicLock,
    CidrRange,
    Credentials,
    CredentialsComponent,
    DiscoveredService,
    Event,
    FileExtension,
    HardwareID,
    InfectionMonkeyBaseModel,
    IntRange,
    IpRange,
    JSONSerializable,
    LMHash,
    Lock,
    MachineID,
    MutableInfectionMonkeyBaseModel,
    NetworkProtocol,
    NetworkRange,
    NetworkService,
    NTHash,
    Password,
    Percent,
    PercentLimited,
    PortStatus,
    RLock,
    SingleIpRange,
    SocketAddress,
    SSHKeypair,
    Token,
)
from monkeytypes.base64_bytes import b64_bytes_validator

AgentPluginManifest
AgentPluginManifest.name
AgentPluginManifest.plugin_type
AgentPluginManifest.supported_operating_systems
AgentPluginManifest.target_operating_systems
AgentPluginManifest.title
AgentPluginManifest.description
AgentPluginManifest.remediation_suggestion
AgentPluginManifest.link_to_documentation
AgentPluginManifest.safe

AgentPluginManifest.version_serialize

AgentPluginType.CREDENTIALS_COLLECTOR
AgentPluginType.EXPLOITER
AgentPluginType.FINGERPRINTER
AgentPluginType.PAYLOAD

B64Bytes
b64_bytes_validator.msg_template

InfectionMonkeyBaseModel.model_config
InfectionMonkeyBaseModel.to_json_dict
InfectionMonkeyBaseModel.to_dict
InfectionMonkeyBaseModel.to_json
InfectionMonkeyBaseModel.from_json
InfectionMonkeyBaseModel.copy
InfectionMonkeyBaseModel.deep_copy
MutableInfectionMonkeyBaseModel.model_config

BasicLock.exc_type
BasicLock.exc_val
BasicLock.exc_tb
BasicLock.acquire
BasicLock.release
Lock
Lock.locked
RLock
RLock.blocking
RLock.timeout
BasicLock.blocking
RLock.timeout
Event
Event.is_set
Event.set
Event.clear
Event.wait
Event.timeout

CredentialsComponent
Credentials.serialize
LMHash.dump_secret
LMHash.validate_hash_format
NTHash.dump_secret
NTHash.validate_hash_format
Password.dump_secret
SSHKeypair.dump_secret

FileExtension

AgentID
HardwareID
MachineID

IntRange
IntRange.max
IntRange.min

NetworkRange.is_in_range
NetworkRange.filter_invalid_ranges
CidrRange.is_in_range
IpRange.is_in_range
SingleIpRange.is_in_range

NetworkProtocol.TCP
NetworkProtocol.UDP
NetworkProtocol.ICMP
NetworkProtocol.UNKNOWN

NetworkService.HTTP
NetworkService.HTTPS
NetworkService.MSSQL
NetworkService.SMB
NetworkService.SSH
NetworkService.MSSQL_BROWSER
NetworkService.UNKNOWN

PortStatus
PortStatus.OPEN
PortStatus.CLOSED

SocketAddress.from_string

DiscoveredService
DiscoveredService.service

Percent.as_decimal_fraction
PercentLimited.le

OTP
Token

JSONSerializable
