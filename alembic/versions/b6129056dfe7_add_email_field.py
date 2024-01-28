"""add email field

Revision ID: b6129056dfe7
Revises: a42b17e93c30
Create Date: 2024-01-27 22:27:55.903904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6129056dfe7'
down_revision: Union[str, None] = 'a42b17e93c30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
