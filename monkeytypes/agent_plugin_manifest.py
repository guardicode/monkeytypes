from typing import Optional, Self, Any
from collections.abc import Callable, Mapping


from pydantic_core import core_schema
from pydantic import StringConstraints, HttpUrl, GetCoreSchemaHandler
from semver import VersionInfo

from monkeytypes import (
    AgentPluginType,
    InfectionMonkeyBaseModel,
    InfectionMonkeyModelConfig,
    OperatingSystem,
)


class PluginName(StringConstraints):
    """
    A plugin name

    Allowed characters are alphanumerics and underscore.
    """

    strip_whitespace = True
    regex = "^[a-zA-Z0-9_]+$"


class PluginVersion(VersionInfo):
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: Any,
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls.from_str,
            handler(source_type),
        )

    @classmethod
    # TODO[pydantic]: We couldn't refactor `__modify_schema__`, please create the `__get_pydantic_json_schema__` manually.
    # Check https://docs.pydantic.dev/latest/migration/#defining-custom-types for more information.
    def __modify_schema__(cls, field_schema):
        """Inject/mutate the pydantic field schema in-place."""
        field_schema.update(
            examples=[
                "1.0.2",
                "2.15.3-alpha",
                "21.3.15-beta+12345",
            ]
        )

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
    description: Optional[str]
    remediation_suggestion: Optional[str] = None
    link_to_documentation: Optional[HttpUrl] = None
    safe: bool = False

    # TODO[pydantic]: The `Config` class inherits from another class, please create the `model_config` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    class Config(InfectionMonkeyModelConfig):
        json_encoders: Mapping[type, Callable] = {PluginVersion: lambda v: str(v)}
