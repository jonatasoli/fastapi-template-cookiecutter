from fastapi import status

from {{cookiecutter.app_slug_snakecase}}.schemas.schemas_{{cookiecutter.app_slug_snakecase}} import {{cookiecutter.model_name}}Endpoint

HEADERS = {"Content-Type": "application/json"}


def test_error_route(client):
    response = client.get(
        "/{{cookiecutter.app_slug}}/error_route", headers=HEADERS
    )
    response_data = response.json().get("detail")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response_data == "Not Found"


def add_{{cookiecutter.model_slug_snakecase}}(client):
    data = {{cookiecutter.model_name}}Endpoint(name="{{cookiecutter.model_name}} 1", current_user_id=1)
    response = client.post(
        "/{{cookiecutter.app_slug}}/add", headers=HEADERS, json=data.dict()
    )
    return response


def test_add_{{cookiecutter.model_slug_snakecase}}(client):
    response = add_{{cookiecutter.model_slug_snakecase}}(client)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"name": "{{cookiecutter.model_name}} 1", "id": 1}


def test_add_{{cookiecutter.model_slug_snakecase}}_error_validate(client):
    """Must be error on validate data"""
    {{cookiecutter.model_slug_snakecase}} = {"name": "{{cookiecutter.model_name}} 1"}
    response = client.post(
        "/{{cookiecutter.app_slug}}/add", headers=HEADERS, json={{cookiecutter.model_slug_snakecase}}
    )
    response_data = response.json().get("detail")[0]
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response_data.get("msg") == "field required"
    assert response_data.get("type") == "value_error.missing"
    assert response_data.get("loc") == ["body", "current_user_id"]


def test_get_{{cookiecutter.model_slug_snakecase}}(client):
    response = add_{{cookiecutter.model_slug_snakecase}}(client)

    response = client.get(
        f"/{{cookiecutter.app_slug}}/get/{response.json()['id']}", headers=HEADERS
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"name": "{{cookiecutter.model_name}} 1", "id": 1}


def test_list_{{cookiecutter.model_slug_snakecase}}s():
    ...


def test_update_{{cookiecutter.model_slug_snakecase}}(client):
    response = add_{{cookiecutter.model_slug_snakecase}}(client)

    new_name = f"{response.json()['id']} Updated"

    data = {{cookiecutter.model_name}}Endpoint(name=new_name, current_user_id=1)
    response = client.put(
        f"/{{cookiecutter.app_slug}}/update/{response.json()['id']}", headers=HEADERS, json=data.dict()
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"name": new_name, "id": 1}


def test_delete_{{cookiecutter.model_slug_snakecase}}():
    ...
