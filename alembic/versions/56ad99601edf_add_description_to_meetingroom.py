"""Add description to MeetingRoom

Revision ID: 56ad99601edf
Revises: e01ab93deee1
Create Date: 2024-02-19 10:08:22.228811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56ad99601edf'
down_revision = 'e01ab93deee1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meetingroom', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meetingroom', 'description')
    # ### end Alembic commands ###
