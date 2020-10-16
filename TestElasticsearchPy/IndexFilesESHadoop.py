import subprocess

#Run the Mapreduce
with open('output.txt','w') as f:
        mapProcess = subprocess.run([ 'yarn','jar','Storejsonesmr.jar', 'elasticsearch.EsDriver','ElasticsearchInput.txt', 'ElastictestOutput3','index1'],stdout=f)

#print(mapProcess.stdout)

if mapProcess.returncode == 0:
        print('Map completed')
