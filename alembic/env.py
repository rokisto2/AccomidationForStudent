# alembic/env.py
from alembic import context
from alembic.context import config
from sqlalchemy import engine_from_config

from config import settings
from models.base import Base
from models import *  # Импортируйте все модели

target_metadata = Base.metadata

def run_migrations_offline():
    url = settings.db_url
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        url=settings.db_url
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()