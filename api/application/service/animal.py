from api.infra.repository.animal import AnimalRepository


class AnimalService:

    __repository = None

    def __init__(self):
        self.__repository = AnimalRepository()

    def get_all(self):
        items = []
        results = self.__repository.get_all()
        for result in results:
            items.append(result.to_model())
        return items

    def get_by_identifier(self, identifier: int):
        return self.__repository.get_by_identifier(identifier=identifier).to_model()

    def create(self, obj):
        return self.__repository.create(obj=obj).to_model()
