class Connection:

    def __init__(self):
        self.xid: int = 0

    def start_transaction(self):
        print(f"starting transaction {self.xid}")
        result: int = self.xid
        self.xid += 1
        return result

    @staticmethod
    def commit_transaction(xid):
        print(f"committing transaction {xid}")

    @staticmethod
    def rollback_transaction(xid):
        print(f"rolling back transaction {xid}")
