"""adds relationship between board and card

Revision ID: ed953b461cad
Revises: a12453e83e41
Create Date: 2021-07-13 13:44:04.130050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed953b461cad'
down_revision = 'a12453e83e41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('board_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'card', 'board', ['board_id'], ['board_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'card', type_='foreignkey')
    op.drop_column('card', 'board_id')
    # ### end Alembic commands ###