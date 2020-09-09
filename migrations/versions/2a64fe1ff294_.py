"""empty message

Revision ID: 2a64fe1ff294
Revises: c50e1d60f49d
Create Date: 2020-09-09 20:16:40.111418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a64fe1ff294'
down_revision = 'c50e1d60f49d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('web_page', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dish',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('is_typical', sa.Boolean(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preferredDishes',
    sa.Column('dish_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dish_id'], ['dish.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('dish_id', 'user_id')
    )
    op.add_column('user', sa.Column('gender', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('phone', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'user', ['phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'name')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'gender')
    op.drop_table('preferredDishes')
    op.drop_table('dish')
    op.drop_table('role')
    op.drop_table('restaurant')
    # ### end Alembic commands ###
