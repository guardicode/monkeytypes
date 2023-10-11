from typing import Optional, Self

from pydantic import (
    GetCoreSchemaHandler,
    GetJsonSchemaHandler,
    HttpUrl,
    StringConstraints,
    field_serializer,
)
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from semver import VersionInfo
from typing_extensions import Annotated

from monkeytypes import AgentPluginType, InfectionMonkeyBaseModel, OperatingSystem

PluginName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[a-zA-Z0-9_]+$"),
]


class PluginVersion(VersionInfo):
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _,
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls.from_str,
            handler(str),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        json_schema = handler(core_schema)
        json_schema = handler.resolve_ref_schema(json_schema)
        json_schema["examples"] = [
            "1.0.2",
            "2.15.3-alpha",
            "21.3.15-beta+12345",
        ]
        return json_schema

    @classmethod
    def from_str(cls, version: str) -> Self:
        """Convert a string to a PluginVersion."""
        return cls.parse(version)


class AgentPluginManifest(InfectionMonkeyBaseModel):
    """
    Class describing agent plugin

    Attributes:
        :param name: Plugin name in snake case
        :param plugin_type: Type of the plugin (exploiter, fingerprinter,
         credentials collector, etc.)
        :param supported_operating_systems: Operating systems that the plugin can run on
        :param target_operating_systems: Operating systems that the plugin can target
        :param title: Human readable name for the plugin
        :param description: Description of the plugin
        :param version: Version of the plugin
        :param link_to_documentation: Link to the documentation of the plugin
        :param safe: Is the plugin safe to run. If there's a chance that running the plugin could
         disrupt the regular activities of the servers or the network, then the plugin is not safe.
    """

    name: PluginName
    plugin_type: AgentPluginType
    supported_operating_systems: tuple[OperatingSystem, ...] = (
        OperatingSystem.WINDOWS,
        OperatingSystem.LINUX,
    )
    target_operating_systems: tuple[OperatingSystem, ...] = (
        OperatingSystem.WINDOWS,
        OperatingSystem.LINUX,
    )
    title: Optional[str]
    version: PluginVersion
    description: Optional[str] = None
    remediation_suggestion: Optional[str] = None
    link_to_documentation: Optional[HttpUrl] = None
    safe: bool = False

    @field_serializer("version", when_used="json")
    def version_serialize(self, v):
        return str(v)
