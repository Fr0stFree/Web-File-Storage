"""init user table

Revision ID: fdeda40edcbc
Revises: 
Create Date: 2023-03-28 22:55:57.331369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdeda40edcbc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('hashed_password', sa.String(length=128), nullable=False),
    sa.CheckConstraint('length(username) > 5'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
