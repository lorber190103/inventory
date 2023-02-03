from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, Session
from model import Item, Company
engine = create_engine("sqlite:///inventory.db")
Session = sessionmaker(bind = engine)
session = Session()

print("Chang-Fisher | Sheppard-Tucker | Faulkner-Howard | Wagner LLC | Campos PLC")
company = input("Choose a company: ")

if len(company) < 4:
    raise Exception("Be more specific with your answer")

c_id = session.query(Company).filter(Company.name.like(str('%'+company+'%'))).all()[0]
idk_dict = {'name':Item.name, 'quantity':Item.quantity, 'location':Item.location}

def READ():
    show_all = input("Would you like to see all contents?:")

    if show_all.lower() != "yes" and show_all.lower() != "no":
        print("\nYou can only answer this question with yes or no")
        pass

    if show_all.lower() == "yes":
        s_all = session.query(Item).filter(Item.company_id.is_(str(c_id))).all()
        print(s_all)
    elif show_all.lower() == "no":
        category = input("Category: ")
        contents = input("Contents: ")
        s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id))&idk_dict[category.lower()].like('%'+str(contents.capitalize()+'%'))).all()
        print(s_filtered)


def CREATE():
    Name = input("Name of the item: ")
    if type(Name) != str:
        raise TypeError("\nName must be a string")

    Quantity = input("Quantity of the item: ")
    if type(Quantity) != int:
        raise TypeError("\nQuantity must be a number")

    Location = input("Location of the item: ")
    if len(Location) > 3:
        raise IndexError("\nLocation can't have more than 3 characters")

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
    category = input("In what categorie is it located: ")
    contents = input("What contents do you want to delete: ")
    s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id))&idk_dict[category.lower()].like('%'+str(contents.capitalize()+'%'))).all()
    print(s_filtered)
    if len(s_filtered) < 2: 
        question = input("\nIs this the item you would like to delete?: ")
        if question.lower == "yes":
            for_deletion = session.query(Item).filter(Item.company_id.is_(str(c_id))&idk_dict[category.lower()].is_(str(contents.capitalize()))).all()[0]
            session.delete(for_deletion)
            session.commit()
        elif question.lower == "no":
            pass
    else:
        print("\nPlease be more specific")
        pass

def EXIT():
    exit()

while 1:
    action = input("\nWhat would you like to do: ")
    function_dict = {
        'create':CREATE,
        'read':READ,
        'delete':DELETE,
        'update':UPDATE,
        'exit':EXIT,
    }
    function_dict[action.lower()]()
