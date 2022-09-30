"""add user table

Revision ID: 6263e9ea2ea3
Revises: 16f5ed60856e
Create Date: 2022-09-30 14:22:04.430215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6263e9ea2ea3'
down_revision = '16f5ed60856e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              nullable=False, server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')

                    )
    pass


def downgrade() -> None:
    pass
