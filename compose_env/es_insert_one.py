from elasticsearch import Elasticsearch

es = Elasticsearch(host="localhost", port=9200)
es = Elasticsearch()

data = {
        "author": "Chestermo",
        "gender": "male",
        "age": "24",
        "body_fat": "15%",
        "interest": ["couch potato", "eat and sleep"]
    }
#index oluşturma işlemi
def create_index(index):
    es.indices.create(index=index, ignore=400)
#tek bir veri yükleme işlemi
def insert_one_data(_index, data):
    res = es.index(index=_index, doc_type='authors', id=5, body=data)
    # index oluşturulabilirse True
    print(res)
    """
    {'_index': 'test-index', '_type': 'authors', '_id': '5', '_version': 1, 'result': 'created', '_shards': {'total': 2, 's
uccessful': 1, 'failed': 0}, '_seq_no': 4, '_primary_term': 1}
    """

index = "test-index"
create_index(index)
insert_one_data(index, data)
