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
Ex02a
commit as you go
vs.
Engine.begin()
begin once
Ex02b

Prefer "begin once" but tutorial uses "commit as you go"


Basics of Statement Execution
CORE
Connection.execute()
text()              returns Result      

ORM
Session.execute()
result rows delivered using same Result interface [CORE]


Fetching Rows
Ex02c

IMPORTANT
engine.connect()        ROLLBACK     if no commit()
engine.begin()          COMMIT

Result
rows                    named tuples

Tuple assignment
for x, y in result:

Integer index
for row in result:
    x = row[0]

Attribute name
for row in result:
    y = row.y

Mapping access
for dict_row in result.mappings():
    x = dict_row["x"]


Sending Parameters
bound parameter syntax
:y      colon format
":y"    actual value

Ex02d
REMEMBER
here we separate input from param


Sending Multiple Parameters
pass a list of dictionary objects instead of a single dictionary
thus single SQL statement invoked multiple times - once for each parameter set

style = executemany
NB: we have already seen this with INSERT the data prior
e.g.
conn.execute(
    text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
    [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
)


Executing with an ORM Session

Session
transactional / database interactive object when using ORM
refers to Core Connection internally which it uses to emit SQL

Follow previous examples with connection but now with ORM session

Ex02e
replace
with engine.connect() as conn:
with Session(engine) as session:

make use of Session.execute() method like Connection.execute() method

Session also "commit as you go" Session.commit()
e.g.
text UPDATE
Ex02f

Session
does not hold onto Connection object after transaction completes
gets new Connection object from the Engine next time it executes SQL against DB

See also    README02.md
https://docs.sqlalchemy.org/en/20/orm/session_basics.html#id1


Database Metadata
https://docs.sqlalchemy.org/en/20/tutorial/metadata.html
Metadata
Table
Column

Ex03
Metadata accessed via ORM-centric registry OR
Declarative Base base class
so same Metadata object shared amongy ORM Table objects

Components of Table
Column objects accessed via associative array located at Table.c


Declaring Simple Constraints
e.g.
PrimaryKeyConstraint
ForeignKeyConstraint

Ex03a


Emitting DDL to the Database
metadata_obj.create_all(engine)
Ex03a


Migration tools
long term DB schema management use schema management tool like Alembic
which builds upon SQL Alchemy = better choice = can manage + orchestrate
process of incrementally altering fixed DB schema over time as design of
application changes


Using ORM Declarative Forms to Define Table Metadata
ORM
provides facade around Table declaration process = Declarative Table
same as Table but includes ORM "mapped class"

allows use to declare our user-defined classes and Table metadata at once


Establishing a Declarative Base
Ex03b

ORM mapped class
Declarative base refers to MetaData collection created automatically
Base.metadata

registry
central "mapper configuration" unit in SQL Alchemy ORM
Base.registry


Declaring Mapped Classes
define ORM mapped classes
illustrate modern form of Declarative driven from PEP 484 type "Mapped" annotations
