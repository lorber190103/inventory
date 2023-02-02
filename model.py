from sqlalchemy.orm import declarative_base
from sqlalchemy import *


metadata_obj = MetaData()
Base = declarative_base()
engine = create_engine("sqlite:///inventory.db")

class Company(Base):
    __tablename__ = "company"

    id = Column(Integer(), primary_key = True)
    name = Column(String, nullable = False)
    
    def __repr__(self) -> str:
        return str(self.id)

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer(), primary_key = True)
    company_id = Column(Integer(), ForeignKey('company.id'))
    name = Column(String, nullable = False)
    quantity = Column(Integer, nullable = False)
    location = Column(String(3), nullable = False)

    def __repr__(self) -> str:
        return f"Company ID:{self.company_id} | Name:{self.name} | Quantity:{self.quantity} | Location:{self.location} \n"

Base.metadata.create_all(engine)
