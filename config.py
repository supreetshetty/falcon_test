import os

#MySQL config 
db_host = os.environ.get('DB_HOST', 'localhost')
db_username = os.environ.get('DB_USERNAME', 'root')
db_passwd = os.environ.get('DB_PASSWORD', '')
db_name = os.environ.get('DB_NAME', 'falcon_db')
db_config = {'host': db_host, 'user': db_username, 'passwd': db_passwd, 'db': db_name}
db_url = 'mysql://{}:{}@{}/{}'.format(db_username, db_passwd, db_host, db_name)