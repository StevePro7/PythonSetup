import contextlib
from db.connection import Connection


class Transaction:

    def __init__(self, conn: Connection):
        self.conn: Connection = conn
        self.xid: int = conn.start_transaction()

    def commit(self):
        self.conn.commit_transaction(self.xid)

    def rollback(self):
        self.conn.rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection: Connection):
    tx = Transaction(connection)

    try:
        yield tx
    except Exception:
        tx.rollback()
        raise

    tx.commit()
