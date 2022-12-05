from typing import Optional, Tuple

from monkeytypes import OperatingSystem
from monkeytypes.agent_plugins import AgentPluginType
from monkeytypes.base_models import InfectionMonkeyBaseModel


class AgentPluginManifest(InfectionMonkeyBaseModel):
    name: str
    plugin_type: AgentPluginType
    supported_operating_systems: Tuple[OperatingSystem, ...] = (
        OperatingSystem.WINDOWS,
        OperatingSystem.LINUX,
    )
    title: Optional[str]
    description: Optional[str]
    link_to_documentation: Optional[str]
    safe: bool = False
