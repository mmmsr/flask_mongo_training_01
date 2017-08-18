#-*- coding: utf-8 -*-
import os


MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = 'mongodb://admin:admin@ds127429.mlab.com:27429/markovchain-sandobox-db'

MONGO_DB_NAME = 'markovchain-sandobox-db'

DEFAULT_KEYWORD = 'プロテイン'

KEYWORD_REPLASED = 'KEYWORD'

NUMBER_OF_SENTENCES = 1
