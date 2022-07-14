"""create words table

Revision ID: 14470aef53a1
Revises: 
Create Date: 2022-07-13 10:19:14.087747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14470aef53a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'words',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('word', sa.String(50), nullable=False),
        sa.Column('is_accented', sa.Boolean),
    )


def downgrade() -> None:
    op.drop_table('words')
