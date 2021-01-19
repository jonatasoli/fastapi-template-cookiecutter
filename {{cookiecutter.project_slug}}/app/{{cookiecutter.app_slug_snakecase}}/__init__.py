from config import settings
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from {{cookiecutter.app_slug_snakecase}}.api.endpoints import {{cookiecutter.app_slug_snakecase}}_router


{{cookiecutter.app_slug_snakecase}} = FastAPI(
    title=settings.APP_NAME,
    # openapi_url=f"{settings.API_V1_STR}/openapi.json",
    # docs_url=f"{settings.API_V1_STR}",
    # redoc_url=None
)


origins = [
    "*",
]

{{cookiecutter.app_slug_snakecase}}.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

{{cookiecutter.app_slug_snakecase}}.include_router({{cookiecutter.app_slug_snakecase}}_router, responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}})
