from sqlalchemy import *

engine = create_engine('sqlite:///test.db')
metadata = MetaData()

document = Table('document', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('rubrics', Text(length=1024)),  # Рубрики через запятую
                 Column('text', Text(length=65535)),
                 Column('created_at', DateTime(), server_default=func.now())
)

metadata.create_all(engine)
