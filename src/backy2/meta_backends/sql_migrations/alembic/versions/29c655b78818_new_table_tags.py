"""New table tags

Revision ID: 29c655b78818
Revises: bbe7904bfc3a
Create Date: 2017-04-11 20:51:40.927156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29c655b78818'
down_revision = 'bbe7904bfc3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('version_uid', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['version_uid'], ['versions.uid'], ),
    sa.PrimaryKeyConstraint('version_uid', 'name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    # ### end Alembic commands ###
