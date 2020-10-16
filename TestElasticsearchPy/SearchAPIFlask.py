from flask import Flask
from flask_restful import Resource, Api

from elasticsearch import Elasticsearch
import subprocess

#Run the Mapreduce
with open('output.txt','w') as f:
        mapProcess = subprocess.run([ 'yarn','jar','Storejsonesmr.jar', 'elasticsearch.EsDriver','ElasticsearchInput.txt', 'ElastictestOutput3','index1'],stdout=f)

#print(mapProcess.stdout)


app = Flask(__name__)
api = Api(app)

if mapProcess.returncode == 0:
        print('Map completed')

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
