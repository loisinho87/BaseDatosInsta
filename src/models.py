import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base) :
    __tablename__ = 'user'
    id = Column (Integer, primary_key=True)
    username = Column (String (200), nullable = False)
    first_name = Column (String (250), nullable=False)
    last_name = Column (String (250), nullable=False)
    email = Column (String(200), nullable=False, unique=True)

class Post (Base) :
    __tablename__ = 'post'
    id = Column (Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('user.id'))
    user = relationship (User)      


class Media (Base):
    __tablename__ = 'media'
    id = Column (Integer, primary_key=True)
    type = Column (Enum ('foto''video'))
    url = Column (String(300), nullable=False)
    post_id = Column (Integer, ForeignKey('post.id'))
    post = relationship (Post) 

class Comment (Base):
    __tablename__ = 'comment'
    id = Column (Integer, primary_key=True)
    comment_text = Column (String(2000))
    author_id = Column (Integer, ForeignKey ('user.id'))
    post_id = Column (Integer, ForeignKey ('post.id' ))
    post = relationship (Post)
    user = relationship (User)

class Follower (Base):
    __tablename__ = 'follower'
    user_from_id = Column (Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column (Integer, ForeignKey('user.id'), primary_key= True)
    user = relationship (User)
    
    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
