# MySQL Adapters file
# Lantern
# Created by Abdelrahmam Salem.
# Copyright (c) 2017 Abdelrahmam Salem. All rights reserved.
# mysql.py

import logging
import sqlalchemy

from retrying import retry
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger()

def retry_on_alch_exception(exc):
    return isinstance(exc, SQLAlchemyError)

class MySQLAdapter(object):
    """MySQL Adapter class that handles all MySQL functionality"""
    def __init__(self, connection_str):
        # Set conn_str property for retries
        self.conn_str = connection_str
        self.engine = sqlalchemy.create_engine(connection_str)

    @retry(retry_on_exception=retry_on_alch_exception,
           wait_exponential_multiplier=100,
           wait_exponential_max=500, 
           stop_max_delay=100)
    def execute(self, query, fetch=True):
        """Executes a sql statement"""
        logger.info('Executing query')
        logger.debug(query)
        result = []
        try:
            with self.engine.connect() as conn:
                if fetch:
                    rows = conn.execute(query).fetchall()
                    result = rows if rows else []
                else:
                    conn.execute(query)
                conn.close()
                return result
        except SQLAlchemyError as err:
            logger.error(err)
            logger.error('MySQL Connection lost. Reconnecting.')
            self.engine = sqlalchemy.create_engine(self.conn_str)
            raise
            