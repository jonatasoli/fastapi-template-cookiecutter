# Introduction

Template to create FastAPI

# Structure

The project is separated into subapps, the main app is not used as a feature.

This template creates a subapp with a basic structure if you prefer.

The data structure uses clean architecture concepts, so we have:
* Adapters - external subapp communication
* Endpoints - The communication layer of the API.
* Services - Business rules
* DAO - is the system queries
* Models - Data models

# Features

* Sqlalchemy 1.4 alpha to async queries
* Tests with pytest
* Config with Dynaconf
* Static analisis with prospectors

## How to use?

```
$ pip install cookiecutter
```

```
$ pip install kamidana
```

```
$ cookiecutter ./fastapi-template-cookiecutter
```
