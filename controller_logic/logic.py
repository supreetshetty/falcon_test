import config
import json


from models import model

def get_call():
	rows = model.get_call_data()
	return rows

def post_call():
	return rows
