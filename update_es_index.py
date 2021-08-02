from elasticsearch import Elasticsearch
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Document

es = Elasticsearch()
engine = create_engine('sqlite:///test.db')
Session = sessionmaker(bind=engine)
session = Session()

for instance in session.query(Document).order_by(Document.id):
    res = es.index(index='text_search', id=instance.id, body={'text': instance.text})

print(es.search(index='text_search', body={"query": {"match": {'text': 'of the volcano'}}}))

