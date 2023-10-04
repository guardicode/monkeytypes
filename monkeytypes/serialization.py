from typing import List, Union

JSONSerializable = Union[  # type: ignore[misc]
    dict[str, "JSONSerializable"],  # type: ignore[misc]
    List["JSONSerializable"],  # type: ignore[misc]
    int,
    str,
    float,
    bool,
    None,
]
