from datetime import datetime
from dataclasses import asdict, dataclass, field
from typing import Optional, Union

@dataclass
class BasePropertiesClass:
    pass

@dataclass
class BaseDataclass:
    
    id: Optional[str] = None
    created_time: Optional[datetime] = None
    archived: Optional[bool] = None
    url: Optional[bool] = None
    properties: Union[dict, BasePropertiesClass] = field(default_factory=dict)

    def as_dict(self):
        return asdict(self)

    def _sanitize_properties_data(self, data: dict) -> BasePropertiesClass:  # pyright: ignore
        """This method is implemented by it's childs to deal with it's own properties data"""
        pass

