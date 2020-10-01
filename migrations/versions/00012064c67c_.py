"""empty message

Revision ID: 00012064c67c
Revises: e80923fee4a8
Create Date: 2020-10-01 15:08:15.086727

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '00012064c67c'
down_revision = 'e80923fee4a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('latitude', table_name='city')
    op.drop_index('longitude', table_name='city')
    op.drop_column('city', 'longitude')
    op.drop_column('city', 'latitude')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('city', sa.Column('latitude', mysql.VARCHAR(length=120), nullable=False))
    op.add_column('city', sa.Column('longitude', mysql.VARCHAR(length=120), nullable=False))
    op.create_index('longitude', 'city', ['longitude'], unique=True)
    op.create_index('latitude', 'city', ['latitude'], unique=True)
    # ### end Alembic commands ###
