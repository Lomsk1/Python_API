"""create posts table

Revision ID: a99b4b153d49
Revises: 
Create Date: 2022-09-28 21:48:26.538327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a99b4b153d49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                                       primary_key=True), sa.Column('title', sa.String(),
                                                                    nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
