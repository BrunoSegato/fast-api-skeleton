from pydantic import BaseModel, StrictInt
from api.domain.enumerator.animal import AnimalTypeEnum


class AnimalModel(BaseModel):
    id: StrictInt
    name: str
    type: AnimalTypeEnum
