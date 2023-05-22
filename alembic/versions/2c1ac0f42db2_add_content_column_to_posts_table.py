"""add content column to posts table

Revision ID: 2c1ac0f42db2
Revises: ccf9dcc900cd
Create Date: 2023-04-17 10:16:33.567381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c1ac0f42db2'
down_revision = 'ccf9dcc900cd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
