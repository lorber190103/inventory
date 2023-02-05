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
        for i in s_all:
            print(i)
    elif show_all.lower() == "no":
        category = input("Category: ")
        contents = input("Contents: ")
        s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id))&idk_dict[category.lower()].like('%'+str(contents.capitalize()+'%'))).all()
        for i in s_filtered:
            print(i)


def CREATE():
    Name = input("Name of the item: ")
    if Name.isalpha() == False and Name.isnumeric() == True:
        raise TypeError("Name must have 1 letter at least")
    Quantity = input("Quantity of the item: ")
    if Quantity.isnumeric() == False:
        raise TypeError("\nQuantity must only be numbers")
    Location = input("Location of the item: ")
    if len(Location) > 3:
        raise IndexError("\nLocation can't have more than 3 characters")
    s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id))&Item.name.is_(str(Name.capitalize()))&Item.location.is_(str(Location.capitalize()))).all()
    if len(s_filtered) < 1:
        session.add(Item(company_id=str(c_id),
            name=str(Name.capitalize()),
            quantity=(Quantity),
            location=str(Location.capitalize())))
        session.commit()
        print("Item created")
        again = session.query(Item).filter(Item.company_id.is_(str(c_id))&Item.name.is_(str(Name.capitalize()))&Item.location.is_(str(Location.capitalize()))).all()
        for i in again:
            print(i)
    else:
        question = input("This item already exists do you still want to proceed? ")
        if question != "yes" and question != "no":
            print("\nThis question must be answered with yes or no")
            pass
        if question.lower() == "yes":
            session.add(Item(company_id=str(c_id),
                name=str(Name.capitalize()),
                quantity=(Quantity),
                location=str(Location.capitalize())))
            session.commit()
            print("Item created")
            for i in s_filtered:
                print(i)
        elif question.lower() == "no":
            pass


def UPDATE():
    name_of_item = input("Name of the item: ")
    s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id))&Item.name.like('%'+str(name_of_item.capitalize()+'%'))).all()
    for i in s_filtered:
        print(i)
    if len(s_filtered) < 2: 
        question = input("Is this the item you would like to update?: ")
        if question != "yes" and question != "no":
            print("\nThis question must be answered with yes or no")
            pass
        if question.lower() == "yes":
            category = input("Category you want to change: ")
            change = input("Change Contents to: ")
            session.query(Item).filter(Item.company_id.is_(str(c_id))&Item.name.like('%'+str(name_of_item.capitalize()+'%'))).update({idk_dict[category.lower()]: str(change.capitalize())})
            session.commit()
            print("Item info updated")
        elif question.lower() == "no":
            print("Try again")
            pass
    else:
        print("\nPlease be more specific")
        pass


def DELETE():
    category = input("In what categorie is it located: ")
    contents = input("What contents do you want to delete: ")
    s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id))&idk_dict[category.lower()].like('%'+str(contents.capitalize()+'%'))).all()
    for i in s_filtered:
        print(i)
    
    if len(s_filtered) < 2: 
        question = input("Is this the item you would like to delete?: ")
        if question != "yes" and question != "no":
            print("\nThis question must be answered with yes or no")
            pass

        if question.lower() == "yes":
            for_deletion = session.query(Item).filter(Item.company_id.is_(str(c_id))&idk_dict[category.lower()].like('%'+str(contents.capitalize()+'%'))).all()[0]
            session.delete(for_deletion)
            session.commit()
            print("Item deleted")
        elif question.lower() == "no":
            print("Try again")
            pass
    else:
        print("\nPlease be more specific")
        pass

def EXIT():
    exit()

while 1:
    print("-----------------------------------")
    action = input("What would you like to do: ")
    function_dict = {
        'create':CREATE,
        'read':READ,
        'delete':DELETE,
        'update':UPDATE,
        'exit':EXIT,
    }
    if action in function_dict:
        function_dict[action.lower()]()
    else:
        print("This function does not exist.")
        pass
