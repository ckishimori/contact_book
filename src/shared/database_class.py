import pathlib
import sqlite3

DATABASE_PATH = pathlib.Path().home() / "contacts.db"

class Database:
    def __init__(self, db_path=DATABASE_PATH):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_table()