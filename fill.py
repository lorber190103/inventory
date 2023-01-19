from faker import Faker
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from model import Company

engine = create_engine("sqlite:///inventory.db", echo=True)
fake = Faker()
Session = sessionmaker(bind = engine)
session = Session()


Faker.seed(0)

for _ in range(5):
    session.add(Company(name=fake.company()))

session.commit()
