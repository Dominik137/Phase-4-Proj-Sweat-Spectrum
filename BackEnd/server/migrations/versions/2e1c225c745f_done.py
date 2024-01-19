"""done

Revision ID: 2e1c225c745f
Revises: 2c94df2115d6
Create Date: 2024-01-19 12:39:07.522789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e1c225c745f'
down_revision = '2c94df2115d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('duration', sa.Interval(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('attributes', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_Workouts'))
    )
    op.create_table('Sets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], name=op.f('fk_Sets_user_id_Users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_Sets'))
    )
    op.create_table('Set_Workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('set_id', sa.Integer(), nullable=True),
    sa.Column('workout_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['set_id'], ['Sets.id'], name=op.f('fk_Set_Workouts_set_id_Sets')),
    sa.ForeignKeyConstraint(['workout_id'], ['Workouts.id'], name=op.f('fk_Set_Workouts_workout_id_Workouts')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_Set_Workouts'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Set_Workouts')
    op.drop_table('Sets')
    op.drop_table('Workouts')
    # ### end Alembic commands ###
