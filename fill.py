from faker import Faker
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from model import Company, Item

engine = create_engine("sqlite:///inventory.db", echo=True)
fake = Faker()
Session = sessionmaker(bind = engine)
session = Session()

Faker.seed(0)

for _ in range(5):
    session.add(Company(name=fake.company()))

for _ in range(250):
    session.add(Item(company_id=fake.random_int(min=1, max=5) ,
                     name= None,
                     quantity=fake.random_int(min=1, max=100),
                     location=fake.bothify('?##',letters='ABCDE')))

session.commit()
