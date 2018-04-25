import config
import json
import MySQLdb

import logic
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

BaseModel = declarative_base()


_db_engine = create_engine(config.db_url, poolclass=NullPool)

_db_session = sessionmaker(bind=_db_engine)


class Controller:
    def on_get(self, req, resp):
        """Handles GET requests"""
        rows = logic.get_call()
        resp.body = json.dumps(rows)

    def on_post(self, req, resp):
        """Handles POST requests"""
        resp.body = req.stream.read()
        try:
            connection = MySQLdb.connect(**config.db_config)
            cursor = connection.cursor(MySQLdb.cursors.DictCursor)
            q = ("SELECT * FROM test")
            cursor.execute(q)
            rows = cursor.fetchall()
            resp.body = json.dumps(rows)
            connection.close()
        except:
            raise