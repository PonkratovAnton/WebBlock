from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database import Base, engine




class Author(Base):
    __tablename__ = "authors"
    author_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Theme(Base):
    __tablename__ = "themes"
    theme_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Post(Base):
    __tablename__ = "posts"
    post_id = Column(Integer, primary_key=True, index=True)
    theme_id = Column(Integer, ForeignKey("themes.theme_id"))
    content = Column(String)
    likes = Column(Integer, default=0)
    author_id = Column(Integer, ForeignKey("authors.author_id"))
    pub_date = Column(DateTime, default=datetime.utcnow)
    author = relationship("Author")
    theme = relationship("Theme")


Base.metadata.create_all(bind=engine)
