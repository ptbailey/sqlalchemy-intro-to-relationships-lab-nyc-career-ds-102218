from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_gwyneth_paltrows_roles():
    return session.query(Role).join(Actor).filter(Actor.name == 'Gwyneth Paltrow').all()

def return_tom_hanks_2nd_role():
    return (session.query(Role).join(Actor).filter(Actor.name == 'Tom Hanks').all())[1]
