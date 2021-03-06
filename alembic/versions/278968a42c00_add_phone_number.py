"""add phone number

Revision ID: 278968a42c00
Revises: b4e18255bb7d
Create Date: 2022-03-16 10:21:57.530780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '278968a42c00'
down_revision = 'b4e18255bb7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
