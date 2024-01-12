import mariadb


class ConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDatabase:
    def __init__(self, config: dict) -> 'cursor':
        self.configuration = config

    def __enter__(self) -> None:
        try:
            self.conn = mariadb.connect(**self.configuration)
            self.cursor = self.conn.cursor()
        except mariadb.InterfaceError as err:
            raise ConnectionError(err)
        except mariadb.ProgrammingError as err:
            raise CredentialsError(err)
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mariadb.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)