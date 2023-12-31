"""migration 1

Revision ID: 7bad3251522d
Revises: 
Create Date: 2023-11-24 17:24:00.268884

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bad3251522d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('async_tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('x', sa.Integer(), nullable=True),
    sa.Column('y', sa.Integer(), nullable=True),
    sa.Column('operator', sa.String(), nullable=True),
    sa.Column('status', sa.Enum(), nullable=True),
    sa.Column('result', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_id'), 'async_tasks', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tasks_id'), table_name='async_tasks')
    op.drop_table('async_tasks')
    # ### end Alembic commands ###
