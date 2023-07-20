from typing import List, TYPE_CHECKING
from beanie import Document, Link
from pydantic import Field

if TYPE_CHECKING:
    from .pet import Pet

class Human(Document):
    name: str = Field()
    pets: List[Link["Pet"]] = Field(default_factory=list)

# Update Forward Refs (works in v1, not yet removed in v2)

from .pet import Pet
Human.update_forward_refs()
