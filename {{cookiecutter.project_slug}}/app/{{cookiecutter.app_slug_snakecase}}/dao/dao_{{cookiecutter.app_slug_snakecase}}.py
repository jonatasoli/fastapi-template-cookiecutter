from .base import CRUDBase
from {{cookiecutter.app_slug_snakecase}}.schemas.schemas_{{cookiecutter.app_slug_snakecase}} import (
    {{cookiecutter.model_name}}CreateResponse,
    {{cookiecutter.model_name}}UpdateResponse,
    {{cookiecutter.model_name}}GetResponse,
    {{cookiecutter.model_name}}Base,
    {{cookiecutter.model_name}}Create,
    {{cookiecutter.model_name}}Update,
)


class CRUD{{cookiecutter.model_name}}(
    CRUDBase[
        {{cookiecutter.model_name}}Base,
        {{cookiecutter.model_name}}Create,
        {{cookiecutter.model_name}}Update,
    ]
):
    class Meta:
        response_create_type = {{cookiecutter.model_name}}CreateResponse
        response_update_type = {{cookiecutter.model_name}}UpdateResponse
        response_get_type = {{cookiecutter.model_name}}GetResponse
