from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

user: str = "stevepro"
pwdX: str = ""
host: str = "localhost"
port: str = "5432"
name: str = "mydb"
conn_str: str = f"postgresql+psycopg2://{user}:{pwdX}@{host}:{port}/{name}"

engine: Engine = create_engine(conn_str)

session: Session = sessionmaker(engine)

with session() as my_sess:
    #my_sess.add(obj)
    my_sess.commit()


# OR
# with session.begin() as my_sess