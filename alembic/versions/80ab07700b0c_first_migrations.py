"""first migrations

Revision ID: 80ab07700b0c
Revises: f94b08cbc79d
Create Date: 2024-01-27 00:15:11.910114

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80ab07700b0c'
down_revision: Union[str, None] = 'f94b08cbc79d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
