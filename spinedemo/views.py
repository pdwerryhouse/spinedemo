import transaction

from spinedemo.models import DBSession
from spinedemo.models import Country
from spinedemo.models import Person

from cornice import Service

from datetime import datetime

def root(request):
    return { }

countries = Service(name='countries', path='/api/countries', description="Countries")
country = Service(name='country', path='/api/countries/{id}', description="Country")

@countries.get()
def get_countries(request):
    session = DBSession()

    countries = session.query(Country).order_by(Country.name)
    entries = []
    for country in countries:
        entry = { }
        entry['id'] = country.id    
        entry['name'] = country.name
        entries.append(entry)

    return entries

@country.put()
def update_country(request):
    session = DBSession()

    id = request.json_body['id']

    country = session.query(Country).get(id)
    country.name = request.json_body['name']

    session.add(country)
    session.flush()
    try:
        transaction.commit()
    except IntegrityError:
        transaction.abort()

    return { }

@countries.post()
def create_country(request):
    session = DBSession()

    country = Country()
    country.name = request.json_body['name']

    session.add(country)
    session.flush()
    newid = country.id;

    try:
        transaction.commit()
    except IntegrityError:
        transaction.abort()

    return { "id": newid }

persons = Service(name='persons', path='/api/persons', description="Persons")
person = Service(name='person', path='/api/persons/{id}', description="Person")

@persons.get()
def get_persons(request):
    session = DBSession()

    persons = session.query(Person).order_by(Person.firstname)
    entries = []
    for person in persons:
        entry = { }
        entry['id'] = person.id    
        entry['firstname'] = person.firstname
        entry['surname'] = person.surname
        entry['country_id'] = person.country_id
        entries.append(entry)

    return entries

@person.put()
def update_person(request):
    session = DBSession()

    id = request.json_body['id']

    person = session.query(Person).get(id)
    person.firstname = request.json_body['firstname']
    person.surname = request.json_body['surname']
    person.country_id = request.json_body['country_id']

    session.add(person)
    session.add(country)
    session.flush()
    try:
        transaction.commit()
    except IntegrityError:
        transaction.abort()

    return { }

@persons.post()
def create_person(request):
    session = DBSession()

    person = Person()
    person.firstname = request.json_body['firstname']
    person.surname = request.json_body['surname']
    person.country_id = request.json_body['country_id']

    session.add(person)
    session.flush()
    newid = person.id;

    try:
        transaction.commit()
    except IntegrityError:
        transaction.abort()

    return { "id": newid }

