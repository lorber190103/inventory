from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, Session
from model import Item, Company
engine = create_engine("sqlite:///inventory.db")
Session = sessionmaker(bind = engine)
session = Session()

def create():
    t = input("Do it: ")
    filtered = session.query(Company).filter(Company.name.is_(str(t))).all()[0]
    session.add(Item(company_id=int(filtered),
                     name="Ches",
                     quantity=1,
                     location="A32"))
    session.commit()

create()
