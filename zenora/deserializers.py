# Copyright (c) 2022 DevGuyAhnaf

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from zenora import Snowflake, User  # type: ignore[attr-defined]
from .models.integration import Integration  # type: ignore[attr-defined]
from typing import Final, Type, List, Dict, Any


__all__: Final[List[str]] = [
    "deserialize_model",
    "deserialize_server_integration",
]


def deserialize_model(
    cls: Type[Any],
    payload: Dict[str, Any],
) -> object:
    """A deserializer used for most model classes

    By default, attrs throws errors if it gets some properties from the API which do not
    exist on the model class. Example, the JSON data contains a property called 'accent color' but the class
    does not (maybe because Zenora wasn't updated after the API change). If that happens, attrs will throw an error.

    This deserializer will only map those values, which the class and the JSON data have in common (including private properties).
    As a result, that error will not be thrown
    """
    try:  # If there are no attribute issues by default, no need to loop over properties
        return cls(**payload)
    except TypeError:
        pass

    data = {}
    for x in cls.__attrs_attrs__:
        if x.name.startswith("_"):
            if (prop := x.name[1:]) in payload:
                data[prop] = payload[prop]
        if x.name in payload:
            data[x.name] = payload[x.name]
    return cls(**data)


def deserialize_server_integration(
    payload: List[Dict[str, Any]]
) -> List[Integration]:
    integrations = []

    for x in payload:
        if "user" in x:
            x["user"] = deserialize_model(User, x["user"])
        if "role_id" in x:
            x["role_id"] = Snowflake(x["role_id"])
        integrations.append(Integration(**x))
    return integrations
