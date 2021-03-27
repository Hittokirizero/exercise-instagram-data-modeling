import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_user = Column(Integer, primary_key=True)
    user_mail = Column(String(250), nullable=False)
    user_birthday = Column(String(250), nullable=False)
    user_country = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'posterson'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_post = Column(Integer, primary_key=True)
    post_title = Column(String(250), nullable=False)
    post_detail = Column(String(250), nullable=False)
    post_img = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Like(Base):
    __tablename__ = 'like'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_like = Column(Integer, primary_key=True)
    like_like_dislike_detail = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_follower = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    userfollow_id = Column(Integer, ForeignKey('user.id'))
    userfollow = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')