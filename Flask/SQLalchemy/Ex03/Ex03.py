from sqlalchemy import MetaData, Table, Column, Integer, String

metadat_obj = MetaData()

user_table = Table(
    "user_account",
    metadat_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String)
)

print(user_table.c.name)
print(user_table.c.keys())