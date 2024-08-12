from sqlalchemy import Engine, create_engine

engine: Engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)