from typing import List
from fastapi import APIRouter, status
from api.domain.schema.animal import AnimalSchema
from api.domain.model.animal import AnimalModel
from api.domain.model.response import ResponseMessageModel
from api.application.service.animal import AnimalService
from api.domain.enumerator.tags import TagsEnum

animal_router = APIRouter(prefix='/animals', tags=[TagsEnum.animals])
animal_service = AnimalService()


@animal_router.get("/",
                   status_code=status.HTTP_200_OK,
                   response_description='A list of animals',
                   responses={
                       500: {'model': ResponseMessageModel, 'description': 'Internal server error'}
                   },
                   response_model=List[AnimalModel])
async def get_animals():
    return animal_service.get_all()


@animal_router.get("/{animal_id}",
                   status_code=status.HTTP_200_OK,
                   response_description='An animal',
                   responses={
                       404: {'model': ResponseMessageModel, 'description': 'The animal was not found'},
                       500: {'model': ResponseMessageModel, 'description': 'Internal server error'}
                              },
                   response_model=AnimalModel)
async def get_animal(animal_id: int):
    return animal_service.get_by_identifier(identifier=animal_id)


@animal_router.post("/",
                    status_code=status.HTTP_201_CREATED,
                    response_model=AnimalModel,
                    responses={
                        422: {'model': ResponseMessageModel, 'description': 'Unprocessable entity'},
                        500: {'model': ResponseMessageModel, 'description': 'Internal server error'}
                    },
                    response_description='The created animal')
async def create_animal(animal: AnimalSchema):
    return animal_service.create(obj=animal)
