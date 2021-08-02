from sqlalchemy import Column, Integer, Text, DateTime, func
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    rubrics = Column(Text(length=1024))  # Рубрики через запятую
    text = Column(Text(length=65535))
    created_at = Column(DateTime(), server_default=func.now())
