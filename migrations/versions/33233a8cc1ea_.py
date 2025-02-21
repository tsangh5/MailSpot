"""empty message

Revision ID: 33233a8cc1ea
Revises: 738fe6677a75
Create Date: 2022-12-22 12:16:20.605835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33233a8cc1ea'
down_revision = '738fe6677a75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inbox', schema=None) as batch_op:
        batch_op.add_column(sa.Column('inboxpw', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('inbox', schema=None) as batch_op:
        batch_op.drop_column('inboxpw')

    # ### end Alembic commands ###
