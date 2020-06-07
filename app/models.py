from flask import current_app as app 
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root' 
app.config['MYSQL_DB'] = 'vod_channel'

