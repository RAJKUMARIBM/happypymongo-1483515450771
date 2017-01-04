import os
import pymongo
# import ssl
import json
from pymongo import MongoClient

try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server

print("hai   1")
print("----------------------------------")
# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')
print("hai   2")
print("----------------------------------")

# VCAP_SERVICES mapping Start

services = os.getenv('VCAP_SERVICES')
services_json = json.loads(services)
mongodb_url = services_json['compose-for-mongodb'][0]['credentials']['uri']

print("hai   3")
print("----------------------------------")
# connect:
client = MongoClient(mongodb_url)
print("hai   4")
print("----------------------------------")
# get the default database:
db = client.get_default_database()
print('connected to mongodb!, welcome to mongodb connection, have a fun')
print db
print("----------------------------------")
print('############# CCODE RUN FROM HERE ################')
db = client['test-database']
db = client.test_database
post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"]}
resa=db.insert(post)
sse=db.collection_names()
print sse
#posts = db.posts
#posts.insert(post)
#cc=posts.find_one({"author": "Mike"})
#for reget in cc:
#	print reget
print('############# CCODE completed HERE ################')	


httpd = Server(("", PORT), Handler)
try:
    print("Start serving at port %i" % PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()

print("hai   5")
print("----------------------------------")