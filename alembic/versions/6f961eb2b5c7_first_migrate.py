"""first_migrate

Revision ID: 6f961eb2b5c7
Revises: 
Create Date: 2023-11-22 07:31:35.531322

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f961eb2b5c7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('ID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('UUID', sa.Integer(), nullable=False),
    sa.Column('RegisterDate', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    # ### end Alembic commands ###