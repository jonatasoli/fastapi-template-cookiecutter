from loguru import logger

from {{cookiecutter.app_slug_snakecase}}.dao import {{cookiecutter.model_slug_snakecase}}


async def add_{{cookiecutter.model_slug_snakecase}}({{cookiecutter.model_slug_snakecase}}_data):
    try:
        name = {{cookiecutter.model_slug_snakecase}}_data.name
        name.join("Include")
        {{cookiecutter.model_slug_snakecase}}_data.name = name

        logger.info({{cookiecutter.model_slug_snakecase}}_data.name)
        return await {{cookiecutter.model_slug_snakecase}}.create(obj_in={{cookiecutter.model_slug_snakecase}}_data)
    except Exception as e:
        logger.error(f"Error in add {{cookiecutter.model_slug_snakecase}} {e}")
        raise e


async def update_{{cookiecutter.model_slug_snakecase}}({{cookiecutter.model_slug_snakecase}}_id, {{cookiecutter.model_slug_snakecase}}_data):
    try:
        name = {{cookiecutter.model_slug_snakecase}}_data.name
        name.join("Update")
        {{cookiecutter.model_slug_snakecase}}_data.name = name

        logger.info({{cookiecutter.model_slug_snakecase}}_data.name)
        return await {{cookiecutter.model_slug_snakecase}}.update(id={{cookiecutter.model_slug_snakecase}}_id, obj_in={{cookiecutter.model_slug_snakecase}}_data)
    except Exception as e:
        logger.error(f"Error in add {{cookiecutter.model_slug_snakecase}} {e}")
        raise e


async def get_{{cookiecutter.model_slug_snakecase}}({{cookiecutter.model_slug_snakecase}}_id):
    try:
        logger.info({{cookiecutter.model_slug_snakecase}}_id)
        return await {{cookiecutter.model_slug_snakecase}}.get(id={{cookiecutter.model_slug_snakecase}}_id)
    except Exception as e:
        logger.error(f"Error in add {{cookiecutter.model_slug_snakecase}} {e}")
        raise e
