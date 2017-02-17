#-*- coding: utf-8 -*-
import os


MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://<dbuser>:<dbpassword>@xxxxxxxx.mlab.com:xxxxx/hogehoge"

MONGO_DB_NAME = 'hogehoge'

DEFAULT_KEYWORD = 'プロテイン'

KEYWORD_REPLASED = 'KEYWORD'

NUMBER_OF_SENTENCES = 1
