from sqlalchemy import create_engine
from model import Document, Base
from settings import DB_URL


if __name__ == '__main__':
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
