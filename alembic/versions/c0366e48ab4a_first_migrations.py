"""first migrations

Revision ID: c0366e48ab4a
Revises: 61cff5f8f1a8
Create Date: 2024-01-27 22:08:14.868864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0366e48ab4a'
down_revision: Union[str, None] = '61cff5f8f1a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
