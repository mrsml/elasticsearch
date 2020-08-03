from elasticsearch import Elasticsearch
from elasticsearch import helpers
from const import (
    ES_HOST,
    ES_PORT
)

es = Elasticsearch(host= ES_HOST, port= ES_PORT)
es = Elasticsearch()

#toplu silme işlemi
def delete_data_by_bulk(_index, _doc_type, _id):
    action = [
        {
            '_op_type': 'delete',
            '_index': _index,
            '_type': _doc_type,
            '_id': _id,
        }
    ]
    res = helpers.bulk(es, action)
    return res
  
#index ile silme işlemi
def delete_index(_index):
    res = es.indices.delete(index=_index, ignore=[400, 404])
    return res

#dizgi ile silme işlemi
def delete_by_query(_index, query):
    res = es.delete_by_query(
        index=_index,
        body={"query": {"match": query}},
        _source=True
    )
    return res

#tek veri silme işlemi
def delete_one(_index, _id):
    res = es.delete(index=_index, id=_id)
    return res


if __name__ == "__main__":
    _index = "test-index"
    query = {"author": "Ken"}
    res = delete_by_query(_index, query)
    _id = "1"
    res = delete_one(_index, _id)
