from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Document

engine = create_engine('sqlite:///test.db')

Session = sessionmaker(bind=engine)
session = Session()
documents = [Document(rubrics='Science, Tech, IT', text='A comparison of the activity of the volcano, which is now '
                                                        'partially collapsed, with sea levels over the last 360,000 '
                                                        'years reveals that when the sea level dips more than 40 '
                                                        'meters below the present-day level, it triggers a fit of '
                                                        'eruptions.'),
             Document(rubrics='Stars, Pop, Music', text='I still remember when I first heard the song by'
                                                        'Peter Gabriel, “Solsbury Hill.”')

             ]

for doc in documents:
    session.add(doc)
session.commit()