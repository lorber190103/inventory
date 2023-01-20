from faker import Faker
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from model import Company, Item

engine = create_engine("sqlite:///inventory.db", echo=True)
fake = Faker()
Session = sessionmaker(bind = engine)
session = Session()
items = open("items.md", "r")
item = items.read()
item_into = item.split("\n")
Faker.seed(0)
i = 0

for _ in range(5):
    session.add(Company(name=fake.company()))

for _ in range(250):
    session.add(Item(company_id=fake.random_int(min=1, max=5) ,
                     name=item_into[i],
                     quantity=fake.random_int(min=1, max=100),
                     location=fake.bothify('?##',letters='ABCDE')))
    i = i+1

session.commit()
