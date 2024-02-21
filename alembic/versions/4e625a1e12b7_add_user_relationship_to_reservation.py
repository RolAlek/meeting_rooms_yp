"""Add user relationship to Reservation

Revision ID: 4e625a1e12b7
Revises: 8dec4afc65be
Create Date: 2024-02-21 10:10:17.242128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e625a1e12b7'
down_revision = '8dec4afc65be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_reservation_user_id_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reservation_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
