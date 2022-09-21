from fastapi import APIRouter, status
from api.domain.enumerator.tags import TagsEnum

default_router = APIRouter(tags=[TagsEnum.defaults])


@default_router.get("/",
                    status_code=status.HTTP_200_OK)
async def home():
    return "Zoo Skeleton"
