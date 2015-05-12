import requests
from elasticsearch import Elasticsearch


URI = "http://localhost:9200/" 
es = Elasticsearch(URI)


def get_all_indexes():
    indexes = list()
    result = requests.get(URI+"_cat/indices?v")
    infos = result.content.rstrip().split('\n')
    # Except the first row(titles)
    infos = infos[1:]
    for info in infos:
        # Yield the index
        yield info.split(' ')[4]


def get_all_rows(index, doc_type, offset=0, limit=500):
    info = { "query": { "match_all": {} } }
    while True: 
        info["from"] = offset
        info["size"] = limit

        result = es.search(index=index, doc_type=doc_type, body=info)
        rows = [doc["_source"] for doc in result['hits']['hits']]
        if len(rows) == 0: break

        yield rows
        offset += limit


if __name__ == "__main__":
    for index in get_all_indexes():
        rows = get_all_rows(index=index, doc_type="logs")
        print rows[0]
