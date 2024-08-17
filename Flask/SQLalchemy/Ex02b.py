from sqlalchemy import Engine, create_engine, TextClause
from sqlalchemy import text

engine: Engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.begin() as conn:
    table: TextClause = text("CREATE TABLE some_table (x int, y int)")
    conn.execute(table)

    input: TextClause = text("INSERT INTO some_table (x, y) VALUES (:x, :y)")
    param: list = [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    conn.execute(input, param)

    conn.commit()
