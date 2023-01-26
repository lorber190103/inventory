from sqlalchemy.orm import declarative_base
from sqlalchemy import *


metadata_obj = MetaData()
Base = declarative_base()
engine = create_engine("sqlite:///inventory.db", echo=True)

class Company(Base):
    __tablename__ = "company"

    id = Column(Integer(), primary_key = True)
    name = Column(String, nullable = False)

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer(), primary_key = True)
    company_id = Column(Integer(), ForeignKey('company.id'))
    name = Column(String, nullable = False)
    quantity = Column(Integer, nullable = False)
    location = Column(String, nullable = False)

    def __repr__(self) -> str:
        return f"{self.company_id}: {self.name}"

Base.metadata.create_all(engine)
