
import requests

searchparameter = "wangshang Rd"
index = "index1"
queryType = "match_phrase"

url = " http://127.0.0.1:5000/search/{}/{}/{}".format(index,queryType,searchparameter)

result = requests.get(url=url)

#print(result.json())

result_Json = result.json()
all_hits = result_Json['hits']['hits']  

print ("total hits using 'size' param:", len(result_Json["hits"]["hits"]))

# iterate the nested dictionaries inside the ["hits"]["hits"] list
for num, doc in enumerate(all_hits):
	print ("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")

    # Use 'iteritems()` instead of 'items()' if using Python 2
	for key, value in doc.items():
		print (key, "-->", value)

    # print a few spaces between each doc for readability
	print ("\n\n")



