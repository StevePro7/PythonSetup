class Connection:

    def __init__(self):
        self.xid: int = 0

    def _start_transaciton(self):
        print(f"starting transaction {self.xid}")
        result: int = self.xid
        self.xid += 1
        return result

    def _commit_transaction(cls, xid):
        print(f"committing transaction {xid}")

    def rollback_transaction(self, xid):
        print(f"rolling back transaction {xid}")
