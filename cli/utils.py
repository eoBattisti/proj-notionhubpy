from typing import Callable, List, Type
from cli.custom_dataclasses import BaseDataclass


def process_data(data: List[dict], obj: Type[BaseDataclass]) -> List[BaseDataclass]:
    """
    Process a list of dictionaries and convert each dictionary into an instance of a specified dataclass.

    Parameters:
    - data (List[dict]): A list of dictionaries containing data to be processed.
    - obj (Type[BaseDataclass]): The type of the dataclass used to create instances.

    Returns:
    - List[BaseDataclass]: A list of instances of BaseDataclass created from the input dictionaries.
    """
    _items = []
    for i in data:
        _items.append(obj(**i))
    return _items

