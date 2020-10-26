import requests

searchparameter = ""

url = " http://127.0.0.1:5000/search/index1/match/{}".format(searchparameter)

result = requests.get(url=url)
 
print ("total hits using 'size' param:", len(result["hits"]["hits"]))

# iterate the nested dictionaries inside the ["hits"]["hits"] list
for num, doc in enumerate(all_hits):
    print ("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")

    # Use 'iteritems()` instead of 'items()' if using Python 2
    for key, value in doc.items():
        print (key, "-->", value)

    # print a few spaces between each doc for readability
    print ("\n\n")



