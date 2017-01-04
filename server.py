import os
import pymongo
# import ssl

MONGODB_URL = os.environ.get('mongodb://admin:PPOETEQMMQUSMJRG@bluemix-sandbox-dal-9-portal.4.dblayer.com:21452/admin?ssl=true')
client = pymongo.MongoClient(MONGODB_URL,ssl_ca_certs="mongpyt.crt")
db = client.get_default_database()
print db.collection_names() 


# VCAP_SERVICES mapping Start
