"""first migrations

Revision ID: 19d3f4d30abb
Revises: 80ab07700b0c
Create Date: 2024-01-27 22:05:59.644180

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19d3f4d30abb'
down_revision: Union[str, None] = '80ab07700b0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_tb',
        sa.Column('id', sa.String(20), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user_tb')
