from sqlalchemy import create_engine
from model import Document, Base
engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)
