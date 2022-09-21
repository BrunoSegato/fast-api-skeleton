from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from api.router import routes
from api.domain.exception import ZooException
from pydantic import ValidationError


def create_app() -> FastAPI:
    current_app = FastAPI(
        title='Zoo Skeleton FastAPI',
        version='1.0.0'
    )
    for route in routes:
        current_app.include_router(route)

    current_app.add_exception_handler(ZooException, zoo_exception_handler)
    current_app.add_exception_handler(RequestValidationError, validation_exception_handler)

    return current_app


def zoo_exception_handler(request: Request, error: ZooException):
    return JSONResponse(
        status_code=error.code,
        content={'message': error.message}
    )


def validation_exception_handler(request: Request, error: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={'message': str(error)}
    )
