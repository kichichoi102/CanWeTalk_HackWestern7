"""empty message

Revision ID: 942b2e7e3b54
Revises: bfa0ce4ad9e1
Create Date: 2020-11-22 03:21:46.898908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '942b2e7e3b54'
down_revision = 'bfa0ce4ad9e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('studentId', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'User', ['studentId'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User', type_='unique')
    op.drop_column('User', 'studentId')
    # ### end Alembic commands ###
