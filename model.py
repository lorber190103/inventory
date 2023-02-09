from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, create_engine
from sqlalchemy.orm import declarative_base

metadata_obj = MetaData()
Base = declarative_base()
engine = create_engine("sqlite:///inventory.db")


class Company(Base):
    __tablename__ = "company"

    ID = Column(Integer(), primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return str(self.ID)


class Item(Base):
    __tablename__ = "item"

    ID = Column(Integer(), primary_key=True)
    company_id = Column(Integer(), ForeignKey('company.ID'))
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    location = Column(String(3), nullable=False)

    def __repr__(self) -> str:
        return str(f"\nName: {self.name} | Quantity: {self.quantity} | Location: {self.location}")


Base.metadata.create_all(engine)
