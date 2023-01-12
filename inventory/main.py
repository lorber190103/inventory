from sqlalchemy import *
engine = create_engine('sqlite:///company.db', echo = True)
meta = MetaData()

company = Table(
    'company', meta,
    Column('company_id', Integer, primary_key = True),
    Column('name', String),
)
meta.create_all(engine)