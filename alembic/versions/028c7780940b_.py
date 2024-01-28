"""empty message

Revision ID: 028c7780940b
Revises: b6129056dfe7
Create Date: 2024-01-27 22:35:44.319808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '028c7780940b'
down_revision: Union[str, None] = 'b6129056dfe7'
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
