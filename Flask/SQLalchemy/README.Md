SQL Alchemy Tutorial
12-Aug-2024


https://docs.sqlalchemy.org/en/20/tutorial/index.html

SQL Alchemy CORE    sqlalchemy
SQL Alchemy ORM     sqlalchemy.orm

ORM                 Object Relational Mapping
allow user-defined Python classes to be mapped to database tables

Session
object persistence mechanism

pip install -r requirements.txt
pip install --upgrade pip


00. https://docs.sqlalchemy.org/en/20/tutorial/index.html#version-check
>>> import sqlalchemy
>>> sqlalchemy.__version__
'2.0.32'


https://docs.sqlalchemy.org/en/20/tutorial/engine.html
Establishing Connectivity - the Engine

Engine
central source of DB conntect

Ex01
"sqlite+pysqlite:///:memory:"
    01. Kind of database    dialect                     sqlite
    02. DB API 3rd party driver to interact w/ DB       pysqlite
    03. how to locate database                          memory

Lazy initialization     
create Engine but not invoke until at least one DB activity

NB: echo=True
Engine log all SQL to Python logger => standard out


Working with Transactions and the DBAPI
https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html

Core        Connection
ORM         Session

ORM
Engine is managed by the Sesson


text()      textual SQL
Getting a Connection

Connection
object purpose to connect to Engine
limit open resource against the database to specific context
i.e.
use Python context manager => with statement
Ex02

NB: ROLLBACK
if we want to commit data then we need to call Conneciton.commit()


Committing Changes