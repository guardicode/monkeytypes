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
    InfectionMonkeyModelConfig,
    IntRange,
    IpRange,
    JSONSerializable,
    LMHash,
    Lock,
    MachineID,
    MutableInfectionMonkeyBaseModel,
    MutableInfectionMonkeyModelConfig,
    NetworkPort,
    NetworkProtocol,
    NetworkRange,
    NetworkService,
    NTHash,
    Percent,
    PercentLimited,
    PluginName,
    PortStatus,
    RLock,
    SecretEncodingConfig,
    SingleIpRange,
    SocketAddress,
    Token,
)
from monkeytypes.base64_bytes import b64_bytes_validator

PluginName.strip_whitespace
PluginName.regex

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

AgentPluginManifest.Config
AgentPluginManifest.Config.json_encoders

AgentPluginType.CREDENTIALS_COLLECTOR
AgentPluginType.EXPLOITER
AgentPluginType.FINGERPRINTER
AgentPluginType.PAYLOAD

B64Bytes
b64_bytes_validator.msg_template

InfectionMonkeyModelConfig.allow_mutation
InfectionMonkeyModelConfig.underscore_attrs_are_private
InfectionMonkeyModelConfig.extra
MutableInfectionMonkeyModelConfig.allow_mutation
MutableInfectionMonkeyModelConfig.validate_assignment
InfectionMonkeyBaseModel.Config
InfectionMonkeyBaseModel.args
MutableInfectionMonkeyBaseModel
MutableInfectionMonkeyBaseModel.Config

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
Credentials
Credentials.Config
SecretEncodingConfig.json_encoders
LMHash.validate_hash_format
NTHash.validate_hash_format

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

NetworkPort.ge
NetworkPort.le

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
