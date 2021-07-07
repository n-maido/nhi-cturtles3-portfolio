"""empty message

Revision ID: 244a95e6e475
Revises: 
Create Date: 2021-07-07 01:08:18.729353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '244a95e6e475'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###