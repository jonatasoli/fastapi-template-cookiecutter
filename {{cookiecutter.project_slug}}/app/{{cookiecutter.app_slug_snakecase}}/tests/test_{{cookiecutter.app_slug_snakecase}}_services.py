import pytest
from unittest import mock
from {{cookiecutter.app_slug_snakecase}}.services.services_{{cookiecutter.app_slug_snakecase}} import add_{{cookiecutter.model_slug_snakecase}}
from {{cookiecutter.app_slug_snakecase}}.schemas.schemas_{{cookiecutter.app_slug_snakecase}} import {{cookiecutter.model_name}}CreateResponse, {{cookiecutter.model_name}}Endpoint, {{cookiecutter.model_name}}Create


response_obj = {{cookiecutter.model_name}}CreateResponse(id=1, name="{{cookiecutter.model_name}} 1", completed=False)


@pytest.mark.asyncio
@mock.patch("{{cookiecutter.app_slug_snakecase}}.dao.{{cookiecutter.model_slug_snakecase}}.create", return_value=response_obj)
async def test_add_{{cookiecutter.model_slug_snakecase}}(mocker):
    data = {{cookiecutter.model_name}}Endpoint(name="{{cookiecutter.model_name}} 1", completed=False, current_user_id=1)
    response = await add_{{cookiecutter.model_slug_snakecase}}({{cookiecutter.model_slug_snakecase}}_data=data)
    assert response == response_obj
