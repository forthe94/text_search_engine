from elasticsearch import Elasticsearch
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Document
from settings import DB_URL


def update_es_index(es, session):
    """
    Updates ElasticSearch index from database.
    """
    es.indices.delete(index='text_search', ignore=[400, 404])

    for instance in session.query(Document).order_by(Document.id):
        es.index(index='text_search', id=instance.id, body={'text': instance.text})


if __name__ == '__main__':
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    ses = Session()
    update_es_index(Elasticsearch(), ses)
