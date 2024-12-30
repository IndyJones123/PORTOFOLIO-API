import logging
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import connection as pg_connection

class ListenMain:
    def __init__(self, conn: pg_connection, logger: logging.Logger):
        self.logger = logger
        self.conn = conn