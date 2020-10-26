from flask import Flask
from flask_restful import Resource, Api

from elasticsearch import Elasticsearch

app = Flask(__name__)
api = Api(app)

#connect to Elasticsearch
es = Elasticsearch(HOST="http://master",PORT=9200)


class ElasticSearchQueries(Resource):
	def __init__(self):
		pass

	def get(self,Index,queryType,queryParameter):
		if queryType == "match_all":
			return es.search(index=Index, body={"query": {"match_all": {}}})
		elif queryType == "exists":
			return es.exists(index=Index)
		elif queryType == "match":
			return es.search(index=Index, body={"query":{"match":{"addr":queryParameter}}})
		elif queryType == "match_phrase":
			return es.search(index=Index, body={"query":{"match_phrase":{"addr":queryParameter}}})		
		elif queryType == "term":
                        return es.search(index=Index, body={"query":{"term":{"addr":queryParameter}}})
		
	def delete(self,Index):
		return es.delete(index=Index)
		
	
api.add_resource(ElasticSearchQueries,"/search/<string:Index>/<string:queryType>/<string:queryParameter>")

if __name__ == "__main__":
	app.run(debug=True)
