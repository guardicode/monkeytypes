# Changelog
All notable changes to this project will be documented in this
file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to
the [PEP 440 version scheme](https://peps.python.org/pep-0440/#version-scheme).


## [1.0.0] - 2024-07-09
### Added
- Missing return type hints

## [0.7.0] - 2024-06-13
### Fixed
- Incomplete Percent/PercentLimited JSON schema generation.

## [0.6.0] - 2024-02-26
### Changed
- Allow error handling to be overridden in InfectionMonkeyBaseModel.

## [0.5.0] - 2024-02-24
### Changed
- Respect aliases when serializing/deserializing JSON

## [0.4.0] - 2023-12-20
### Changed
- Raise explicit TypeErrors when parsing LM/NT hashes
- Raise clearer errors when parsing identities and secrets


## [0.3.0] - 2023-10-12
### Added
- InfectionMonkeyBaseModel.to_dict()
- InfectionMonkeyBaseModel.to_json()
- InfectionMonkeyBaseModel.to_json_dict()
- InfectionMonkeyBaseModel.from_json()
- InfectionMonkeyBaseModel.copy()
- InfectionMonkeyBaseModel.deep_copy()

### Changed
- Upgraded from pydantic v1.x to pydantic v2.x
- get_secret_value() method to get_plaintext() function


## [0.2.0] - 2023-10-03
### Added
- Installation and usage to the README
- Support for type checking
- Export BasicLock
- Export RLock
- Export InfectionMonkeyBaseModel
- Export MutableInfectionMonkeyBaseModel
- Export InfectionMonkeyModelConfig
- Export MutableInfectionMonkeyModelConfig

### Changed
- The way base models are exported

### Removed
- `monkeytypes.base_models` export
