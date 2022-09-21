from pydantic import BaseModel, constr
from api.domain.enumerator.animal import AnimalTypeEnum


class AnimalSchema(BaseModel):
    name: constr(max_length=80)
    type: AnimalTypeEnum
