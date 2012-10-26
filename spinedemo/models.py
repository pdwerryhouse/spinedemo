import transaction

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import ForeignKey

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)
    
class Person(Base):
    __tablename__ = 'persons'
    
    id = Column(Integer, primary_key=True)
    firstname = Column(Unicode(255), unique=True)
    surname = Column(Unicode(255), unique=True)
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship("Country", backref=backref('persons', order_by=id))

def populate():
    session = DBSession()
    model = Country()
    model.name = "Australia"
    session.add(model)
    session.flush()
    transaction.commit()

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    try:
        populate()
    except IntegrityError:
        transaction.abort()
