from elasticsearch import Elasticsearch

URI = "http://localhost:9200/" 
es = Elasticsearch(URI)


def get_all_rows(index, doc_type):
    #res = es.search(index="test", doc_type="articles", body={"query": {"match": {"content": "fox"}}})
    res = es.search(index=index, doc_type=doc_type, body={"query": {"match_all":{}}})
    print("%d documents found" % res['hits']['total'])
    #print("%s) %s" % (doc['_id'], doc['_source']['content']))
    return [doc["_source"] for doc in res['hits']['hits']]


if __name__ == "__main__":
    rows = get_all_rows(index="logstash-3611.01.10", doc_type="logs")
    print rows[0]
