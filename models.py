from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Role(Base):
    #this is the child class
    __tablename__ = 'roles'
    id = Column (Integer, primary_key = True)
    character = Column(String)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship('Actor', back_populates = 'roles')

class Actor(Base):
    __tablename__ = 'actors'
    id = Column (Integer, primary_key = True)
    name = Column(String)
    roles = relationship('Role', order_by = 'Role.id',back_populates = 'actor')


engine = create_engine('sqlite:///actors.db', echo = True)
Base.metadata.create_all(engine)
