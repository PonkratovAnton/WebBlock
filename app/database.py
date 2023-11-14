from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from config import password_db, localhost, name_db, postgres_user, port_db

engine = create_engine(f'postgresql://{postgres_user}:{password_db}@{localhost}:{port_db}/{name_db}')
Session = sessionmaker(bind=engine)
session = Session()

