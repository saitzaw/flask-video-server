"""Application Configuration""" 

from os import environ 

class Config: 
  #database config 
  #SQLite
  DB_NAME = "test.db"
  USER = "stz"
  PASSWORD = "frontiir"

  # storage path 
  PATH = "mnt"
  VODs = "vods"
  CHANNEL = "channels"
