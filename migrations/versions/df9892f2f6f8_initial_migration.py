"""Initial migration.

Revision ID: df9892f2f6f8
Revises: 
Create Date: 2024-05-25 23:22:37.931511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df9892f2f6f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('altitude', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('flight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flight_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=False),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('setting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flight_id', sa.Integer(), nullable=False),
    sa.Column('parameter', sa.String(length=64), nullable=False),
    sa.Column('value', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flight_id', sa.Integer(), nullable=False),
    sa.Column('command', sa.Text(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['flight_id'], ['flight.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('detection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('point_id', sa.Integer(), nullable=False),
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(length=64), nullable=False),
    sa.Column('frame', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], ),
    sa.ForeignKeyConstraint(['point_id'], ['point.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('detection_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['detection_id'], ['detection.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('object')
    op.drop_table('detection')
    op.drop_table('task')
    op.drop_table('setting')
    op.drop_table('image')
    op.drop_table('flight')
    op.drop_table('user')
    op.drop_table('point')
    # ### end Alembic commands ###
