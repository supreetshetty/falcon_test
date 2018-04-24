
import falcon
from controllers import Controller

api = falcon.API()
api.add_route('/call', Controller())
