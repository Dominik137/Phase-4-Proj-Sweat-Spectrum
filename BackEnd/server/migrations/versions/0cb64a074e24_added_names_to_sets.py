"""added names to sets

Revision ID: 0cb64a074e24
Revises: 6be6db1d4241
Create Date: 2024-01-25 10:45:51.349328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cb64a074e24'
down_revision = '6be6db1d4241'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Sets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Sets', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
