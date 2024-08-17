from sqlalchemy import Engine, create_engine, TextClause
from sqlalchemy import text

engine: Engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

info: TextClause = text("select 'hello world'")

with engine.connect() as conn:
    result = conn.execute(info)
    print(result.all())