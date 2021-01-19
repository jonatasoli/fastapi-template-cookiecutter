from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
    includes=["{{cookiecutter.app_slug_snakecase}}/*.toml"],
    environments=True,
)
