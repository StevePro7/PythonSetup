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

Ex03c
ORM Mapped classes
available for ORM persistence + query operations

DeclarativeBase.__tablename__

vs.
DeclarativeBase.__table__           imperative table

mapped_column()                     details OR
Mapped()

nullable = Optional
relationship

NB:
__init__()
automatically given
accepts all attribute names as optional keyword args


Emitting DDL to the database from an ORM mapping¶
ORM mapped classes refer to Table objects contained within MetaData collection
emitting DDL given Declarative Base

Ex03c
Base.metadata.create_all(engine))


Table Reflection
how to generate Table objects from existing DB
some_table = Table("some_table", metadata_obj, autoload_with=engine)


Working with Data
https://docs.sqlalchemy.org/en/20/tutorial/data.html

ORM
select use Session.scalars()

Subqueries and CTEs
Common Table Expression
used in a similar way as a subquery but includes additional features

Working with SQL Functions

Window Functions
SQL aggregate function which calculates aggregate value over the rows
being returned in a group as the individual result rows are processed


Data Manipulation with the ORM
https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#tutorial-inserting-orm

ORM
Session
Declarative forms tod define Table Metadata - setup ORM mappings

Insert by adding object entries to Session and then persist to DB via flush()

Ex04
transient state
two objects are not associated with any DB state
yet to be associated with a Session object that can generate INSERT statements

Ex04a
pending state
two objects added to Session => session.add()

session.new
IdentitySet
Python set that hashes on object identity 

Flushing
Session makes use of pattern: "unit of work"
accumulate changes one at a time but does not communcate them to the DB until needed

flush()
emit SQL to database to push the current set of changes
session.flush()


NOTE
some database backends such as postgresql-psycopg2 can INSERT many rows at once
while still being able to retrieve the primary key values


Getting Objects by Primary Key from the Identity Map

identity map
in-memory store that links all objects currently loaded in memory to primary key identity

Session.get()


Committing
session.commit()

detached state
use the object after closing the Session


Updating ORM Objects using the Unit of Work pattern

Python object acts as a proxy for the row in the database
DB row in terms of the current transaction


Deleting ORM Objects using the Unit of Work pattern

cascade
work more efficiently by allowing the database to handle related rows automatically


Bulk / Multi Row INSERT, upsert, UPDATE and DELETE

Rolling Back
Session.rollback()

NB:
object.__dict__
{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x...>}

SQL Alchemy internal state object


Closing a Session
session.close()

releases the connection resources to the connection pool
cancelling out [i.e. rolling back] any transactions in progress

expunges all objects from Session
i.e.
all objects added to Session are in state "detached"

Avoid detached state
Session.expire_on_commit = False


Working with ORM Related Objects
https://docs.sqlalchemy.org/en/20/tutorial/orm_related_objects.html

relationship()
linkage btwn two different mapped classes OR
linkage from mapped class to itself [self-referential]
e.g.
Ex04a
addresses: Mapped[List["Address"]] = relationship(back_populates="user")
user: Mapped[User] = relationship(back_populates="addresses")

relationship back_populates
two relationships considered to be complimentary to each other


Persisting and Loading Relationships
list not mutated = not appended OR not extended

transient = changes not actually associated with the object yet


Cascading Objects into the Session
objects transient state until they are associated with a Session object

session.add( obj )
save-update-cascade
pending state


Loader Strategies
lazy loading is one of the most famous ORM patterns
implicit queries may cause errors when no longer DB transaction
or when using alternative concurrency patterns like asyncio

Loader Strategies SELECT statements using Select.options()

WILL STOP HERE - not really so relevant to our use case


Further reading
https://docs.sqlalchemy.org/en/20/tutorial/further_reading.html