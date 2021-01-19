from fastapi import FastAPI

from {{cookiecutter.app_slug_snakecase}} import {{cookiecutter.app_slug_snakecase}}


def create_app():
    app = FastAPI()
    app.mount("/{{cookiecutter.app_slug}}", {{cookiecutter.app_slug_snakecase}})
    return app
