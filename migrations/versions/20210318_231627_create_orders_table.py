"""create orders table

Revision ID: 79790895e36b
Revises: 37c2f0f2eecb
Create Date: 2021-03-18 23:16:27.474977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79790895e36b'
down_revision = '37c2f0f2eecb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('subtotal', sa.Float(), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###