import config
import json


from controller_logic import logic

class Controller:
    def on_get(self, req, resp):
        """Handles GET requests"""
        rows = logic.get_call()
        resp.body = json.dumps(rows)

    def on_post(self, req, resp):
        """Handles POST requests"""
        resp.body = req.stream.read()
