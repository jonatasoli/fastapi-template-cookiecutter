from fastapi import APIRouter, status
from loguru import logger

from {{cookiecutter.app_slug_snakecase}}.schemas.schemas_{{cookiecutter.app_slug_snakecase}} import {{cookiecutter.model_name}}Endpoint
from {{cookiecutter.app_slug_snakecase}}.services import services_{{cookiecutter.app_slug_snakecase}}

{{cookiecutter.app_slug_snakecase}}_router = APIRouter()


@{{cookiecutter.app_slug_snakecase}}_router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_{{cookiecutter.model_slug_snakecase}}(*, data: {{cookiecutter.model_name}}Endpoint):
    try:
        return await services_{{cookiecutter.app_slug_snakecase}}.add_{{cookiecutter.model_slug_snakecase}}(data)
    except Exception as e:
        logger.error(f"Error return endpoint {e}")
        raise e


@{{cookiecutter.app_slug_snakecase}}_router.put("/update/{id}", status_code=status.HTTP_200_OK)
async def update_{{cookiecutter.model_slug_snakecase}}(*, id: int, data: {{cookiecutter.model_name}}Endpoint):
    try:
        return await services_{{cookiecutter.app_slug_snakecase}}.update_{{cookiecutter.model_slug_snakecase}}(id, data)
    except Exception as e:
        logger.error(f"Error return endpoint {e}")
        raise e


@{{cookiecutter.app_slug_snakecase}}_router.get("/get/{id}", status_code=status.HTTP_200_OK)
async def update_{{cookiecutter.model_slug_snakecase}}(*, id: int):
    try:
        return await services_{{cookiecutter.app_slug_snakecase}}.get_{{cookiecutter.model_slug_snakecase}}(id)
    except Exception as e:
        logger.error(f"Error return endpoint {e}")
        raise e
