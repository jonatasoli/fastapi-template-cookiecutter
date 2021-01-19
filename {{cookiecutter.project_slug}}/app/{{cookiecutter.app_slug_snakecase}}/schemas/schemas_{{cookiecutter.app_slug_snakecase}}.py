from pydantic import BaseModel


class {{cookiecutter.model_name}}Base(BaseModel):
    name: str


class {{cookiecutter.model_name}}Create({{cookiecutter.model_name}}Base):
    ...


class {{cookiecutter.model_name}}CreateResponse({{cookiecutter.model_name}}Base):
    id: int

    class Config:
        orm_mode = True


class {{cookiecutter.model_name}}Update({{cookiecutter.model_name}}Base):
    ...


class {{cookiecutter.model_name}}UpdateResponse({{cookiecutter.model_name}}Base):
    id: int

    class Config:
        orm_mode = True


class {{cookiecutter.model_name}}GetResponse({{cookiecutter.model_name}}Base):
    id: int

    class Config:
        orm_mode = True


class {{cookiecutter.model_name}}Endpoint({{cookiecutter.model_name}}Base):
    current_user_id: int
