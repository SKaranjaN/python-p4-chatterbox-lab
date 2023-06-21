"""empty message

Revision ID: a29b90ab79b5
Revises: be2f3f7c23b5
Create Date: 2023-06-21 18:05:58.875938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a29b90ab79b5'
down_revision = 'be2f3f7c23b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
