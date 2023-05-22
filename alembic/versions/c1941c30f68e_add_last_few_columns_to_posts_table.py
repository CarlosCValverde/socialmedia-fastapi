"""add last few columns to posts table

Revision ID: c1941c30f68e
Revises: 0c3bc1a73d60
Create Date: 2023-05-22 12:04:26.774589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1941c30f68e'
down_revision = '0c3bc1a73d60'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False,
                                     server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
