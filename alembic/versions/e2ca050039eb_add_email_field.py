"""add email field

Revision ID: e2ca050039eb
Revises: 028c7780940b
Create Date: 2024-01-27 22:35:59.205373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2ca050039eb'
down_revision: Union[str, None] = '028c7780940b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
