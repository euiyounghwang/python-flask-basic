"""empty message

Revision ID: a42b17e93c30
Revises: c0366e48ab4a
Create Date: 2024-01-27 22:27:42.733312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a42b17e93c30'
down_revision: Union[str, None] = 'c0366e48ab4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
