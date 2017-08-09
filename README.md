# Lantern
Shed some light onto your community center, business, or your personal profile. Lantern is a social network aimed at event driven institutions.

- - - -

# Help

## To Do ##

Please read the [To Do](https://github.com/abubakir1997/Lantern/blob/master/TODO.md) file and constantly update it. After completing task mark complete and **do not delete**.

## Install NPM ##

Install npm and nodejs from the following site [NodeJS](https://nodejs.org/en/) then type in the command line:
```
shell:~$ cd path/to/Lantern
shell:Lantern$  npm install
```

## Built Application ##

Run:

```
shell:Lantern$ npm run build
```


## Start Application ##

You can start the application in three different configurations (Production, Test, and Development) choose one of the following:

```
shell:Lantern$ npm run prod
```
```
shell:Lantern$ npm run test
```
```
shell:Lantern$ npm run dev
```

**Note:** A page will open in your browser with an error message, **just refresh the page.**

## Learn ##
- [Learn X (Python) in Y Minutes](https://learnxinyminutes.com/docs/python/)
- [Learn X (Git) in Y Minutes](https://learnxinyminutes.com/docs/git/)
- [Clean Architecture Exaplined](https://subvisual.co/blog/posts/20-clean-architecture/)

- - - -

# Clean Architecture Example
- Components:
	- Adapter
	- Handler
	- Route
	- Context

## Steps ##
- Create:
	- Adapter Object
	- Handler Object
	- Context Methods (setters | getters)
	- Route Method(s)
- Initiate (in route):
	- Adapter Object
	- Handler Object with Adapter Object
	- Context Object with Handler Object
- Call Context Handler(s) Method(s)
- Return Result(s)

## Adapter Example ##
```/app/adapters/mysql.py```

```
import logging
import os
import sys
import sqlalchemy
 
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)) + '/../../config')
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)) + '/../../app')

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
```

## Handler Example ##
```/app/handlers/dump_times.py```

```
import logging
import os
import sys

from app.handlers.sql import *

logger = logging.getLogger('cost-of-outages')

class DumpTimesHandler(object):
	"""docstring for DumpTimesHandler"""
	def __init__(self, adapter):
		self.adapter = adapter

	def getDumpTimes(self):
		return self.adapter.execute(GET_DUMP_TIMES, True)
```

## Context Example ##
```/app/handlers/__init__.py```

```
from app.handlers.dump_times import DumpTimesHandler

class Context(object):
	"""docstring for context"""
	def __init__(self):
		self._dump_times_handler = None
		
	""" dump_times """
	@property
	def dump_times_handler(self):
		if not self._dump_times_handler:
			raise NotImplementedError("No Dump Handler exists")
		else:
			return self._dump_times_handler

	@dump_times_handler.setter
	def dump_times_handler(self, handler):
		self._dump_times_handler = handler
```

## Route Example ##
```/app/routes/__init__.py```

```
from flask import Blueprint

api = Blueprint('routes', __name__)

from .login import *
```

```/app/routes/login.py```

```
from . import api
from flask import (jsonify, request, render_template, redirect, session, url_for)


@api.route('/login')
def login():
	return render_template('pages/login.html')
```