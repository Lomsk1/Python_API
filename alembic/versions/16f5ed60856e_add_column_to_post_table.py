"""add column to post table

Revision ID: 16f5ed60856e
Revises: a99b4b153d49
Create Date: 2022-09-30 13:37:43.572874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16f5ed60856e'
down_revision = 'a99b4b153d49'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(),  nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'column')
    pass
