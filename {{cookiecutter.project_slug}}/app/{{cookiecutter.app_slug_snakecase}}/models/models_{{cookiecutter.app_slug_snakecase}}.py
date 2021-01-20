from ext.database import Base
from .audit_mixins import AuditMixin
from sqlalchemy import Column, String, Integer


class {{cookiecutter.model_name}}(Base, AuditMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String, default="unnamed")
