from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings


def get_engine():
    """'postgresql://scott:tiger@localhost:5432/mydatabase'"""
    return create_async_engine(
        settings.DB_DSN,
        echo=True,
    )


def get_session():
    _engine = get_engine()
    return AsyncSession(_engine)


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
