from bson.objectid import ObjectId
from datetime import datetime

class State(object):
    def __init__(self, obj_id=None, prefix1=None, prefix2=None, suffix=None, frequency=None):
        if obj_id is None:
            self._id = ObjectId()
        else:
            self._id = obj_id
        self.prefix1 = prefix1
        self.prefix2 = prefix2
        self.suffix = suffix
        self.frequency = frequency


    def get_as_json(self):
        return self.__dict__
    

    @staticmethod    
    def build_from_json(json_data):
        if json_data is not None:
            try:                            
                return State(json_data.get('_id', None),
                    json_data['prefix1'],
                    json_data['prefix2'],
                    json_data['suffix'],
                    json_data['frequency'])
            except KeyError as e:
                raise Exception("キーがありません: {}".format(str(e)))
        else:
            raise Exception("データがありません")
