from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()

#Actors
tom_hanks = Actor(name = 'Tom Hanks')
gwyneth_paltrow = Actor(name = 'Gwyneth Paltrow')
tom_hardy = Actor(name = 'Tom Hardy')

#Roles
tom_hanks.roles = [Role(character = 'Forrest Gump'), Role(character = 'Jim Lovell'),\
Role(character= 'Woody'), Role(character = 'Robert Langdon')]

gwyneth_paltrow.roles = [Role(character='Pepper Potts'), Role(character='Margot Tenenbaum')]

tom_hardy.roles = [Role(character = 'Bronson'), Role(character = 'Alfie Solomons')]

session.add_all([tom_hanks,gwyneth_paltrow,tom_hardy])
session.commit()
