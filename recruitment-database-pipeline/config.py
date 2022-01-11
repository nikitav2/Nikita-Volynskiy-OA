from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'Nikita'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Nik01ita'
app.config['MYSQL_DATABASE_DB'] = 'new_schema'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)