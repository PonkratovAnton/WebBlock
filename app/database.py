from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# engine = create_engine('postgresql://postgres:04041954-@localhost/web_block', echo=True)
engine = create_engine('postgresql://postgres:04041954-@db:5432/web_block')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

