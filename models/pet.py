from typing import List, TYPE_CHECKING
from beanie import Document, BackLink
from pydantic import Field

if TYPE_CHECKING:
    from .human import Human


class Pet(Document):
    name: str = Field()
    owners: List[BackLink["Human"]] = Field(original_field="pets")

# Update Forward Refs (works in v1, not yet removed in v2)

from .human import Human
Pet.update_forward_refs()
