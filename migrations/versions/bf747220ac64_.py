"""empty message

Revision ID: bf747220ac64
Revises: f3f9ec31bc6f
Create Date: 2020-03-29 23:15:08.405721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf747220ac64'
down_revision = 'f3f9ec31bc6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('indice', sa.Column('pb_minValDate', sa.Date(), nullable=True))
    op.add_column('indice', sa.Column('pe_ttm_minValDate', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('indice', 'pe_ttm_minValDate')
    op.drop_column('indice', 'pb_minValDate')
    # ### end Alembic commands ###