import psycopg2
from utils.config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cur = self.conn.cursor()

    def select_from_table_with_condition(
        self, table_name: str, condition: str, ID: str
    ):
        self.cur.execute(
            f'''SELECT * FROM {table_name} WHERE name = %s AND "ID" = %s''',
            (
                condition,
                ID,
            ),
        )
        return self.cur.fetchall()

    def close_connection(self):
        self.cur.close()
        self.conn.close()


db = Database(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
)
