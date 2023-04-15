"""Amenity model class."""
from datetime import datetime

from dataclasses import dataclass
from typing import Any
import json

@dataclass
class Amenity(object):

    type: str
    id: int
    lat: float
    lon: float
    timestamp: datetime
    version: int
    uid: int
    tags: dict[str, Any]

    @property
    def tags_str(self):
        """returns tags as string."""
        return json.dumps(self.tags).replace("\'", "")


