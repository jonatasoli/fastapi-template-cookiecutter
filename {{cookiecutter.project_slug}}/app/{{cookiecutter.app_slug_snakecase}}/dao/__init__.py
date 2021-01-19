from .dao_{{cookiecutter.app_slug_snakecase}} import CRUD{{cookiecutter.model_name}}
from {{cookiecutter.app_slug_snakecase}}.models.models_{{cookiecutter.app_slug_snakecase}} import {{cookiecutter.model_name}}


{{cookiecutter.model_slug_snakecase}} = CRUD{{cookiecutter.model_name}}({{cookiecutter.model_name}})
