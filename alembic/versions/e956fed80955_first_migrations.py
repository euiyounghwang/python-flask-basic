"""first migrations

Revision ID: e956fed80955
Revises: 5579a9260d41
Create Date: 2024-01-27 00:13:12.584341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e956fed80955'
down_revision: Union[str, None] = '5579a9260d41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
