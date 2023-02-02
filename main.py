from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, Session
from model import Item, Company
engine = create_engine("sqlite:///inventory.db")
Session = sessionmaker(bind = engine)
session = Session()

print("Chang-Fisher | Sheppard-Tucker | Faulkner-Howard | Wagner LLC | Campos PLC")
company = input("Choose a company: ")
c_id = session.query(Company).filter(Company.name.is_(str(company))).all()[0]
idk_dict = {'name':Item.name, 'quantity':Item.quantity, 'location':Item.location}

def READ():
    category = input("Category: ")
    contents = input("Contents: ")
    real = session.query(Item).filter(Item.company_id.is_(str(c_id))&idk_dict[category.lower()].is_(str(contents.capitalize()))).all()
    print(real)


def CREATE():
    Name = input("Name of the item: ")
    if type(Name) != str:
        raise TypeError("Name must be a string")

    # Raises an Exception if Name contains numbers
    # if any(str.isdigit() for str in Name):
    #   raise Exception("Name can't contain numbers")

    Quantity = input("Quantity of the item: ")
    if type(Quantity) != int:
        raise TypeError("Quantity must be a number")

    Location = input("Location of the item: ")
    if len(Location) > 3:
        raise IndexError("Location can't have more than 3 characters")

    session.add(Item(company_id=str(c_id),
                     name=str(Name.capitalize()),
                     quantity=(Quantity),
                     location=str(Location.capitalize())))
    session.commit()


def UPDATE():
    name_of_item = input("Name of the item: ")
    category = input("Category of item you want to change: ")
    change = input("Change Contents to: ")
    session.query(Item).filter(Item.company_id.is_(str(c_id))&Item.name.is_(str(name_of_item.capitalize()))).update({idk_dict[category.lower()]: str(change.capitalize())})
    session.commit()


def DELETE():
    category = input("In what categorie is it: ")
    contents = input("What contents do you want to delete: ")
    for_deletion = session.query(Item).filter(Item.company_id.is_(str(c_id))&idk_dict[category.lower()].is_(str(contents.capitalize()))).all()[0]
    session.delete(for_deletion)
    session.commit()


def EXIT():
    exit()

while 1:
    action = input("What would you like to do: ")
    function_dict = {
        'create':CREATE,
        'read':READ,
        'delete':DELETE,
        'update':UPDATE,
        'exit':EXIT,
    }

    function_dict[action.lower()]()
