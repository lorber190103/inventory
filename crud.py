from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, Session
from model import Item
engine = create_engine("sqlite:///inventory.db")
Session = sessionmaker(bind = engine)
session = Session()


def create():
    session.add(Item(company_id=2,
                     name="FakeProduct",
                     quantity=1,
                     location='A11'))
    session.commit()

def read():
    filtered = session.query(Item).filter(Item.name.is_('FakeProduct')).all()[0]
    return filtered

def updatee():
    session.query(Item).update({Item.location: 'A12'})
    session.commit()

def deletee():
    letsdoit = session.query(Item).filter(Item.name.is_('FakeProduct')).all()[0]
    session.delete(letsdoit)
    session.commit()
