"""first migrations

Revision ID: f94b08cbc79d
Revises: e956fed80955
Create Date: 2024-01-27 00:13:47.060281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f94b08cbc79d'
down_revision: Union[str, None] = 'e956fed80955'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
