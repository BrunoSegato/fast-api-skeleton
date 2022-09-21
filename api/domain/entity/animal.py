from sqlalchemy import Column, String, Integer, Enum, DateTime, func, UniqueConstraint, Index
from api.infra.driver.db import Base
from api.domain.enumerator.animal import AnimalTypeEnum
from api.domain.model.animal import AnimalModel


class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(80), nullable=False)
    type = Column(Enum(AnimalTypeEnum), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.utc_timestamp())
    updated_at = Column(DateTime(timezone=True), server_default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    Index('animal_name_idx', "Animal.name")
    Index('animal_created_at_idx', 'Animal.created_at')
    Index('animal_updated_at_idx', 'Animal.updated_at')
    Index('animal_deleted_at_idx', 'Animal.deleted_at')
    UniqueConstraint('name', name='animal_name_idx')

    def to_model(self):
        return AnimalModel(id=self.id, name=self.name, type=self.type.value)
