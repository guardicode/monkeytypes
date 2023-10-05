from typing import Union

JSONSerializable = Union[  # type: ignore[misc]
    dict[str, "JSONSerializable"],  # type: ignore[misc]
    list["JSONSerializable"],  # type: ignore[misc]
    int,
    str,
    float,
    bool,
    None,
]
