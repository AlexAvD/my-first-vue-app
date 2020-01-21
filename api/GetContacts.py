import falcon
from bson import json_util

class GetContacts:
    def __init__(self, mongoClient):
        self.db = mongoClient['contacts_app']
        self.contacts = self.db['contacts']

        # self.db = mongoClient['sample_mflix']
        # self.contacts = self.db['users']

    def on_get(self, req, resp):
        data = self.contacts.find()

        data = [
            {   
                'id': str(contact['_id']),
                'name': contact['name'],
                'email': contact['email'],
                'phone': contact['phone'],
                'image': contact['image'] if ('image' in contact) else '',
                'desc': contact['desc'] if ('desc' in contact) else '',
            } for contact in self.contacts.find()
        ]

        resp.content_type = 'application/json'
        resp.body = json_util.dumps(data)
