from pymongo import MongoClient
client=MongoClient("mongodb://pythmongo:12345@ds155718.mlab.com:55718/mongopy")
# MongoClient('ds155718.mlab.com', 55718)
db=client.get_default_database()
print db
#db=client['web_craw']
#print db
db.web_cont.insert_one({"content": "", "f_flag": "y", "relevent_url_flag": "y", "base_url_flag": "y","ilock":"y"})