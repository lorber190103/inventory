from model import Item

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///inventory.db")
Session = sessionmaker(bind=engine)
session = Session()


def CREATE():
    session.add(Item(company_id=2,
                     name="FakeProduct",
                     quantity=1,
                     location='A11'))
    session.commit()


def READ():
    filtered = session.query(Item).filter(Item.name.is_('FakeProduct')).all()[0]
    return filtered


def UPDATE():
    session.query(Item).filter(Item.name.is_('FakeProduct')).update({Item.location: 'A12'})
    session.commit()


def DELETE():
    for_deletion = session.query(Item).filter(Item.name.is_('FakeProduct')).all()[0]
    session.delete(for_deletion)
    session.commit()
