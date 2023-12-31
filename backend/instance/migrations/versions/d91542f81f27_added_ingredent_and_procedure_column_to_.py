"""Added ingredent and procedure column to recipe table

Revision ID: d91542f81f27
Revises: 
Create Date: 2023-07-12 12:18:21.865463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd91542f81f27'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ingredient', sa.String(), nullable=False, server_default="rice"))
        batch_op.add_column(sa.Column('preparation_instruction', sa.String(), nullable=False, server_default="cook it..."))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_column('preparation_instruction')
        batch_op.drop_column('ingredient')

    # ### end Alembic commands ###
