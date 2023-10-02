# monkeytypes

This project contains a collection of types and models used by Infection
Monkey-related projects.

## Installation
`pip install monkey-types`

## Usage

```python
from monkeytypes import InfectionMonkeyBaseModel

class MyModel(InfectionMonkeyBaseModel):
    ...
```

## Running tests
```
$> poetry install
$> poetry run pytest
```
