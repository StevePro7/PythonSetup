from sqlalchemy import Engine, create_engine, text, TextClause
from sqlalchemy.orm import Session

engine: Engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
with Session(engine) as session:
    table: TextClause = text("CREATE TABLE some_table (x int, y int)")
    session.execute(table)

    store: TextClause = text("INSERT INTO some_table (x, y) VALUES (:x, :y)")
    param: list = [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    session.execute(store, param)

    stmt: TextClause = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
    result = session.execute(stmt, {"y": 2})
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
