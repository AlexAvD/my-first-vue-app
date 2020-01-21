import falcon
from falcon_cors import CORS
from pprint import pprint 
from waitress import serve
from pymongo import MongoClient


from api.GetContacts import GetContacts
from api.EditContact import EditContact

client = MongoClient('mongodb+srv://alex-av-d:alex-av-d@mycluster-panv4.mongodb.net/test?retryWrites=true&w=majority')

cors = CORS(allow_origins_list=['http://localhost:8080'], allow_all_headers=True, allow_all_methods=True)
api = falcon.API(middleware=[cors.middleware])

api.add_route('/api/contacts', GetContacts(client))
api.add_route('/api/contacts/edit', EditContact(client))

serve(api, host = '127.0.0.1', port = '3000') 