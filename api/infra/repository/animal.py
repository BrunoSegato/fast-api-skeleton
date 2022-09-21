from api.infra.driver.db import SessionLocal
from api.domain.entity.animal import Animal
from api.domain.exception import EntityNotFoundException


class AnimalRepository:

    __session = None

    def __init__(self):
        self.__session = SessionLocal()

    def create(self, obj):
        try:
            animal = Animal()
            animal.name = obj.name
            animal.type = obj.type
            self.__session.add(animal)
            self.__session.commit()
            self.__session.flush()
            return animal
        except Exception:
            self.__session.rollback()

    def get_all(self):
        return self.__session.query(Animal).filter(
            Animal.deleted_at.is_(None)
        )

    def get_by_identifier(self, identifier: int):
        result = self.__session.query(Animal).filter(
            Animal.id == identifier,
            Animal.deleted_at.is_(None)
        ).first()
        if result is None:
            raise EntityNotFoundException('Animal not found')
        return result
