"""empty message

Revision ID: 61cff5f8f1a8
Revises: 19d3f4d30abb
Create Date: 2024-01-27 22:08:12.581822

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61cff5f8f1a8'
down_revision: Union[str, None] = '19d3f4d30abb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
