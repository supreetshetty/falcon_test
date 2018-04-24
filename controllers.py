import config
import json
import MySQLdb


class Controller:
    def on_get(self, req, resp):
        """Handles GET requests"""
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
        resp.body = json.dumps(rows)

    def on_post(self, req, resp):
        """Handles POST requests"""
        resp.body = req.stream.read()
        try:
            connection = MySQLdb.connect(**config.db_config)
            cursor = connection.cursor(MySQLdb.cursors.DictCursor)
            prepare_query(req)
            q = ("SELECT * FROM test")
            cursor.execute(q)
            rows = cursor.fetchall()
            resp.body = json.dumps(rows)
            connection.close()
        except:
            raise