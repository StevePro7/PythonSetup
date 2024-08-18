SQL Alchemy ORM
17-Aug-2024


https://docs.sqlalchemy.org/en/20/orm/session_basics.html


NB:  SQL Alchemy Core
https://docs.sqlalchemy.org/en/20/core/metadata.html


Session basics

Session
establishes all conversations w/ DB and represents a "holding zone" for objects
loaded / associated during its lifespan

ORM objects maintained inside Session structure called "identity map"

Session requests connection resource from Engine and establishes
transaction on that connection - con't until commit or rollback

Transaction ends connection resource with Engine release to the connection pool
managed by Engine

Unit of work pattern
when DB queried or transaction committed the Session first flushes all pending
changes stored in memroy to the database [unit of work]

Session
ORM mapped objects mainteined are proxy object to database rows
local to transaction held by the Session

Ex11


Sessionmaker
provide a factory for Session objects with a fixed configuration
Application = Engine object in module scope

sessionmaker
provide factory for Session objects that are contstructed against this engine

Ex11a
sessionmaker analogous to Engine as module-level factory for function-level
sessions / connections

sessionmaker.begin()
Egnie.begin()


Flusing
https://docs.sqlalchemy.org/en/20/orm/cascades.htmlNT is issued when 
Session.begin_nested()

IMPORTANT
flush process always occurs when transactional methods occur
Session.commit()
Session.begin_nested()



FAQs
https://docs.sqlalchemy.org/en/20/orm/session_basics.html

General rule
application should manage the lifecycle of the session externally 
to functions that deal with specific data

Seaparation of concerns which keeps data-specific operations
agnostic of hte context in which they access + manipulate the data


Session
mutable stateful object that represents a single database transaction
an instance of Session therefore cannot be shared among concurrent threads OR
asyncio tasks without careful synchronization

Session is intended to be used in a non-concurrent fashion i.e.
Session instance should be used in only one thread [task] at a time

scoped_session approach can provide "thread local" Sesison object


State Management
https://docs.sqlalchemy.org/en/20/orm/session_state_management.html

Transient           no database identity
Pending             session.add()
Persistent          present in session and database
Deleted             deleted within flush
Detached            previous record in DB but not in session


Cascades
https://docs.sqlalchemy.org/en/20/orm/cascades.html
e.g.
delete cascade with many-to-many relationships
ON DELETE cascade with ORM relationships


Transactions and Connection Management
https://docs.sqlalchemy.org/en/20/orm/session_transaction.html

Using SAVEPOINT
SAVEPOINT transactions supported by underlying engine using this method:
session.begin_nested()

Pattern ideal for PostgreSQL catching IntegrityError to detect duplicate rows
Normally abort entire transaction when error raised however when using
SAVEPOINT the outer transaction is maintained
Thus data is persisted into DB even with "duplicate primary key" record skipped
without rolling back the entire operation


sessionmaker    vs. Engine
Session         vs. Connection

Transaction Isolation level
READ UNCOMMITTED
READ COMMITTED      
REPEATABLE READ     default
SERIALIZABLE


Contextual/Thread-local Sessions
https://docs.sqlalchemy.org/en/20/orm/contextual.html

Reference
When do I construct a Session, when do I commit it, and when do I close it?
https://docs.sqlalchemy.org/en/20/orm/session_basics.html#session-faq-whentocreate

Introduce concept of "session scopes"
Web applications link scope of a DB Session to the web request

scoped_session


Tracking queries, object and Session Changes with Events
https://docs.sqlalchemy.org/en/20/orm/session_events.html


Session API
https://docs.sqlalchemy.org/en/20/orm/session_api.html