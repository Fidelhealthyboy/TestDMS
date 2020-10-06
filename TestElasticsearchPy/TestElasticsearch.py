from elasticsearch import Elasticsearch
import subprocess

#Run the Mapreduce 

mapProcess = subprocess.run([ 'yarn','jar','Storejsonesmr.jar', 'elasticsearch.EsDriver','ElasticsearchInput.txt', 'ElastictestOutput2'],stdout=subprocess.PIPE)

print(mapProcess.stdout)

if mapProcess.returncode == 0:
	print('Map completed')

#connect to Elasticsearch
es = Elasticsearch(HOST="http://master",PORT=9200)

#check Elasticsearch Index
print(es.indices.exists(index="index1"))

