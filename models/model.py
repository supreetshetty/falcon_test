import json

from connectors import mysql
import config
from oto import response


def get_call_data():
	try:
		connection, cursor = mysql.connection_cursor()
		q = ("SELECT * FROM test")
		cursor.execute(q)
		rows = cursor.fetchall()
		connection.close()
	except:
			rows = {}

	return json.dumps(rows)
