import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

import config

BaseModel = declarative_base()
_db_engine = create_engine(config.db_url, poolclass=NullPool)
_db_session = sessionmaker(bind=_db_engine)


def connection_cursor():
	connection = MySQLdb.connect(**config.db_config)
	cursor = connection.cursor(MySQLdb.cursors.DictCursor)
	return connection, cursor


