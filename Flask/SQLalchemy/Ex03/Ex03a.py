from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy import Engine, create_engine

metadat_obj = MetaData()

user_table = Table(
    "user_account",
    metadat_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

address_table = Table(
    "address",
    metadat_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

engine: Engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadat_obj.create_all(engine)