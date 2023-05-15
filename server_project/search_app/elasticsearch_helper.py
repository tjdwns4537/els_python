from elasticsearch import Elasticsearch
from django.conf import settings

def connect_elasticsearch():
    es = Elasticsearch('http://localhost:9200')
    return es

def test_elasticsearch_connection():
    es = connect_elasticsearch()

    # Index a document
    index_name = 'my_index'
    document = {
        'title': 'Test Document',
        'content': 'This is a test document.'
    }

    response = es.index(index=index_name, body=document)
    print(f"Document indexed. Response: {response}")

    # Retrieve the indexed document
    response = es.get(index=index_name, id=response['_id'])
    print(f"Retrieved document. Response: {response}")

if __name__ == '__main__':
    test_elasticsearch_connection()