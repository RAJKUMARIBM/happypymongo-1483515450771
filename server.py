import os
import pymongo
# import ssl
MONGODB_URL = "mongodb://admin:VSBVBFCGCIFGXQFS@bluemix-sandbox-dal-9-portal.0.dblayer.com:19651/admin?ssl=true"
client = pymongo.MongoClient(MONGODB_URL,ssl_ca_certs="Mongo.crt")
#db = client.get_default_database()
print client.database_names()