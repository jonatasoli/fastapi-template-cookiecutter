from typing import Generator
from loguru import logger

import pytest
from fastapi.testclient import TestClient
from alembic.config import main

import sys
from os.path import dirname as d
from os.path import abspath, join

root_dir = d(abspath(__file__))
sys.path.append(root_dir)

from config import settings
from main import create_app as app


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")


@pytest.fixture
def client():

    main(["--raiseerr", "upgrade", "head"])

    with TestClient(app()) as client:
        yield client

    main(["--raiseerr", "downgrade", "base"])
