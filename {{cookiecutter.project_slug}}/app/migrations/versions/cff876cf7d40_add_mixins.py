"""add mixins

Revision ID: cff876cf7d40
Revises: 6535654405d4
Create Date: 2021-01-18 15:51:03.279756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cff876cf7d40"
down_revision = "6535654405d4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("{{cookiecutter.model_slug_snakecase|replace('_', '')}}", sa.Column("created_by_id", sa.Integer(), nullable=True))
    op.add_column("{{cookiecutter.model_slug_snakecase|replace('_', '')}}", sa.Column("date_created", sa.DateTime(), nullable=True))
    op.add_column("{{cookiecutter.model_slug_snakecase|replace('_', '')}}", sa.Column("date_updated", sa.DateTime(), nullable=True))
    op.add_column("{{cookiecutter.model_slug_snakecase|replace('_', '')}}", sa.Column("updated_by_id", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("{{cookiecutter.model_slug_snakecase|replace('_', '')}}", "updated_by_id")
    op.drop_column("{{cookiecutter.model_slug_snakecase|replace('_', '')}}", "date_updated")
    op.drop_column("{{cookiecutter.model_slug_snakecase|replace('_', '')}}", "date_created")
    op.drop_column("{{cookiecutter.model_slug_snakecase|replace('_', '')}}", "created_by_id")
    # ### end Alembic commands ###
