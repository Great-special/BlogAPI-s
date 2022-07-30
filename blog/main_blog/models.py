from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from main_blog.database import Base

"""
    Models Saves the data to the  a database 
    relationship('ModelName', back_populates='connetorName')
"""

class Blogs(Base):
    __tablename__ = 'Blogs'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('Users.id'))
    
    creator = relationship('User', back_populates='blog')
    
    
class User(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    email = Column(String) 
    phone = Column(Integer)
    password = Column(String)
    
    blog = relationship('Blogs', back_populates='creator')
