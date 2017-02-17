from pymongo import MongoClient
from bson.objectid import ObjectId
from state import State
import settings


class StateDao(object):
    def __init__(self):
        self.client = MongoClient(settings.MONGO_URL)
        self.database = self.client[settings.MONGO_DB_NAME]


    def create(self, state):
        created_id = None
        if state is not None:
            created_id = self.database.states.insert(state.get_as_json())            
        return created_id


    def read(self, obj_id=None, prefix1=None, prefix2=None, frequency=None):
        if prefix1 is not None and prefix2 is not None:
            return self.database.states.find({ '$and' : [{'prefix1': prefix1}, {'prefix2': prefix2}]})
        elif prefix2 is None:
            return self.database.states.find({"prefix1":prefix1})


    def update(self, state):
        if state is not None:
            self.database.states.save(state.get_as_json())            


    def delete(self, state):
        if state is not None:
            self.database.states.remove(state.get_as_json())            


    def delete_all(self):
        self.database.states.remove({})
