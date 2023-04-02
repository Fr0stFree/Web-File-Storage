"""remove content field from files table

Revision ID: ffe0342fbcf7
Revises: 33ca2755444c
Create Date: 2023-04-02 18:06:00.255018

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ffe0342fbcf7'
down_revision = '33ca2755444c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stored_file', 'content')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stored_file', sa.Column('content', postgresql.BYTEA(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###