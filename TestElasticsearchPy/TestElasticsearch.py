from elasticsearch import Elasticsearch
import subprocess

#Run the Mapreduce 
with open('output.txt','w') as f:
	mapProcess = subprocess.run([ 'yarn','jar','Storejsonesmr.jar', 'elasticsearch.EsDriver','ElasticsearchInput.txt', 'ElastictestOutput3','index1'],stdout=f)

#print(mapProcess.stdout)

if mapProcess.returncode == 0:
	print('Map completed')

#connect to Elasticsearch
es = Elasticsearch(HOST="http://master",PORT=9200)

#check Elasticsearch Index
index_exists = es.indices.exists(index="index1")
print(index_exists)

if index_exists:
	result_search = es.search(index="index1",body={"from":0,"size":3,"query":{"match":{"addr":"wenyixi"}}})
	print(result_search) 

