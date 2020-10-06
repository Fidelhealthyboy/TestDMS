from elasticsearch import Elasticsearch
es = Elasticsearch(HOST="http://master",PORT=9200)
print(es.indices.exists(index="index1"))

