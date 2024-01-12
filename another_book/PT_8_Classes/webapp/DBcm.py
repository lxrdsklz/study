import mariadb


class UseDatabase:
    def __init__(self, config: dict) -> 'cursor':
        self.configuration = config

    def __enter__(self) -> None:
        self.conn = mariadb.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()