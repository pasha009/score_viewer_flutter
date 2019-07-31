"""empty message

Revision ID: 7bf61dc7552e
Revises: 
Create Date: 2019-07-30 16:02:26.198677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bf61dc7552e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('mobile', sa.String(length=15), nullable=False),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('age', sa.String(length=20), nullable=True),
    sa.Column('rollno', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile')
    )
    op.create_table('doublematch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('winner1_id', sa.Integer(), nullable=True),
    sa.Column('winner2_id', sa.Integer(), nullable=True),
    sa.Column('loser1_id', sa.Integer(), nullable=True),
    sa.Column('loser2_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['loser1_id'], ['player.id'], ),
    sa.ForeignKeyConstraint(['loser2_id'], ['player.id'], ),
    sa.ForeignKeyConstraint(['winner1_id'], ['player.id'], ),
    sa.ForeignKeyConstraint(['winner2_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_doublematch_date'), 'doublematch', ['date'], unique=False)
    op.create_table('singlematch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('winner_id', sa.Integer(), nullable=True),
    sa.Column('loser_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['loser_id'], ['player.id'], ),
    sa.ForeignKeyConstraint(['winner_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_singlematch_date'), 'singlematch', ['date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_singlematch_date'), table_name='singlematch')
    op.drop_table('singlematch')
    op.drop_index(op.f('ix_doublematch_date'), table_name='doublematch')
    op.drop_table('doublematch')
    op.drop_table('player')
    # ### end Alembic commands ###