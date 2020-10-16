from flask import Flask
from flask_restful import Resource, Api

from elasticsearch import Elasticsearch

app = Flask(__name__)
api = Api(app)

#connect to Elasticsearch
es = Elasticsearch(HOST="http://master",PORT=9200)

#check Elasticsearch Index
index_exists = es.indices.exists(index="index1")
print(index_exists)



class ElasticSearchQueries(Resource):
	def __init__(self):
		pass

	def get(self,Index,query):
		if query == "match_all":
			return es.search(index=Index, body={"query": {"match_all": {}}})
		
	
api.add_resource(ElasticSearchQueries,"/search/<string:Index>/<string:query>")

if __name__ == "__main__":
	app.run(debug=True)
