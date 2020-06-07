"""Application Configuration""" 

from os import environ 
based_dir = os.path.abspath(os.path.dirname(__file__))

class Config: 

  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = '123456789'
  DATABASE_URL="mysql:///vod_channel"
  SQLALCHEMY_DATABASE_URI = os.environ(DATABASE_URL)

class ProductionConfig(Config): 
  DEBUG = False 

class DevConfig(Config): 
  DEBUG = True 
