
import json

class NamelinkDB:

    def __init__(self, from_dict=None):
        self.length = 0
        self.hlink_names = {
            #name(string): url
        }
        
        if from_dict != None:
            self.hlink_names = from_dict
            self.length = len(from_dict.keys())
    
    def put(self, name, url):
        self.hlink_names[name] = url

    def get(self, name):
        if name not in self.hlink_names.keys():
            emptyResponse = {
                'name': name,
                'url': None
            }
        
            return json.dumps(emptyResponse)
        else:
            response = {
                'name': name,
                'url': self.hlink_names[name]
            }
            return response

    def delete(self):
        self.hlink_names = {}

