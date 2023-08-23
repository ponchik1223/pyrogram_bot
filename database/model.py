from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP

metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("name_user", String, nullable=False),
    Column("user_id", Integer, nullable=True),
    Column("user_register", TIMESTAMP, default=datetime.utcnow),
)

