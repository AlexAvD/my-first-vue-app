import falcon
import json
from bson.objectid import ObjectId
from bson import json_util

class EditContact:
    def __init__(self, mongoClient):
        self.db = mongoClient['contacts_app']
        self.contacts = self.db['contacts']
        
    def on_post(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable('This API only supports responses encoded as JSON.')
        
        if 'application/json' not in req.content_type:
            raise falcon.HTTPUnsupportedMediaType('This API only supports requests encoded as JSON.')

        data = json.loads(req.stream.read().decode('utf-8'))
        print(data)
        action = data['action']
        result = {
            'action': action,
            'result': 0
        }

        if action == 'add':
            add_result = self.contacts.insert_one(data['data'])
            result['result'] = str(add_result.inserted_id)

        elif action == 'delete': 
            delete_result = self.contacts.delete_one({'_id': ObjectId(data['id'])})
            if (delete_result.deleted_count):
                result['result'] = data['id']

        elif action == 'update':
            update_result = self.contacts.replace_one({'_id': ObjectId(data['id'])}, data['data'])
            if (update_result.modified_count):
                result['result'] = data['id']

        resp.content_type = 'application/json'
        resp.body = json_util.dumps(result)