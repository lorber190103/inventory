from model import Company, Item

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///inventory.db")
Session = sessionmaker(bind=engine)
session = Session()
company = None

while company is None:
    print("-----------------------------------")
    print("Chang-Fisher | Sheppard-Tucker | Faulkner-Howard | Wagner LLC | Campos PLC")
    company = input("Choose a company: ")
    c_dict = {'chang', 'fisher', 'chang-fisher',
              'sheppard', 'tucker', 'sheppard-tucker',
              'faulkner', 'howard', 'faulkner-howard',
              'wagner', 'llc', 'wagner llc',
              'campos', 'plc', 'campos plc'}

    if not company.lower() in c_dict:
        print('\033[1m'+'\nEither the company does not exist or you have made a mistake while writing it.'+'\033[0m')
        company = None
        pass

c_id = session.query(Company).filter(Company.name.like(str('%'+company+'%'))).all()[0]
category_dict = {'name': Item.name, 'quantity': Item.quantity, 'location': Item.location}


def READ():
    show_all = None
    while show_all is None:
        show_all = input("Would you like to see all contents?:")

        if show_all.lower() != "yes" and show_all.lower() != "no":
            print('\033[1m'+'\nYou can only answer this question with yes or no.'+'\033[0m')
            print("-----------------------------------")
            show_all = None
            pass

    if show_all.lower() == "yes":
        s_all = session.query(Item).filter(Item.company_id.is_(str(c_id))).all()
        for i in s_all:
            print(i)

    elif show_all.lower() == "no":
        category = None

        while category is None:
            category = input("Category: ")

            if category not in category_dict:
                print('\033[1m'+'\nThis category does not exist.'+'\033[0m')
                print("-----------------------------------")
                category = None
                pass

        contents = input("Contents: ")
        s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id)) &
                                                category_dict[category.lower()].like('%' +
                                                str(contents.capitalize()+'%'))).all()

        if len(s_filtered) < 1:
            print('\033[1m'+'\nThere are no contents with that name.'+'\033[0m')
            pass

        else:
            for i in s_filtered:
                print(i)


def CREATE():
    Name = None
    Quantity = None
    Location = None

    while Name is None:
        Name = input("Name of the item: ")
        if not Name.isalpha() and Name.isnumeric():

            print('\033[1m'+'\nThe Name must at least have 1 letter.'+'\033[0m')
            print("-----------------------------------")
            Name = None
            pass

        elif len(Name) > 50:
            print('\033[1m'+'\nThe Name cant have more than 50 characters.'+'\033[0m')
            print("-----------------------------------")
            Name = None
            pass

    while Quantity is None:
        Quantity = input("Quantity of the item: ")

        if not Quantity.isnumeric():
            print('\033[1m'+'\nThe Quantity must only contain numbers.'+'\033[0m')
            print("-----------------------------------")
            Quantity = None
            pass

        elif len(Quantity) > 4:
            print('\033[1m'+'\nThe Quantity cant have more than 4 characters.'+'\033[0m')
            print("-----------------------------------")
            Quantity = None
            pass

    while Location is None:
        Location = input("Location of the item: ")

        if not len(Location) == 3:
            print('\033[1m'+'\nThe Location should for example look like this: A11'+'\033[0m')
            print("-----------------------------------")
            Location = None
            pass

        elif not Location[0].isalpha() or not Location[1].isdigit() or not Location[2].isdigit():
            print('\033[1m'+'\nThe Location should for example look like this: A11'+'\033[0m')
            print("-----------------------------------")
            Location = None
            pass

    s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id)) &
                                            Item.name.is_(str(Name.capitalize())) &
                                            Item.location.is_(str(Location.capitalize()))).all()

    if len(s_filtered) < 1:
        session.add(Item(company_id=str(c_id),
                         name=str(Name.capitalize()),
                         quantity=(Quantity),
                         location=str(Location.capitalize())))

        session.commit()
        print("Item created")
        again = session.query(Item).filter(Item.company_id.is_(str(c_id)) &
                                           Item.name.is_(str(Name.capitalize())) &
                                           Item.location.is_(str(Location.capitalize()))).all()

        for i in again:
            print(i)

    else:
        print('\033[1m'+'\nAn item with the same attributes does already exist'+'\033[0m')
        pass


def UPDATE():
    name_of_item = None
    location_of_item = None

    while name_of_item is None:
        name_of_item = input("Full Name of the item: ")
        if not name_of_item.isalpha() and name_of_item.isnumeric():
            print('\033[1m'+'\nThe Name must at least have 1 letter.'+'\033[0m')
            print("-----------------------------------")
            name_of_item = None
            pass

        elif len(name_of_item) > 50:
            print('\033[1m'+'\nThere are no items with a name longer than 50 characters.'+'\033[0m')
            print("-----------------------------------")
            name_of_item = None
            pass

    while location_of_item is None:
        location_of_item = input("Location of item: ")

        if not len(location_of_item) == 3:
            print('\033[1m'+'\nThe Location should for example look like this: A11.'+'\033[0m')
            print("-----------------------------------")
            location_of_item = None
            pass

        elif not location_of_item[0].isalpha() or not location_of_item[1].isdigit() or not location_of_item[2].isdigit():
            print('\033[1m'+'\nThe Location should for example look like this: A11.'+'\033[0m')
            print("-----------------------------------")
            location_of_item = None
            pass

    s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id)) &
                                            Item.location.like(str(location_of_item.capitalize())) &
                                            Item.name.is_(str(name_of_item.capitalize()))).all()

    if len(s_filtered) < 1:
        print('\033[1m'+'\nThere are no contents with that name and location.'+'\033[0m')
        pass

    else:
        for i in s_filtered:
            print(i)

        if len(s_filtered) < 2:
            question = None

            while question is None:
                print("-----------------------------------")
                question = input("Is this the item you would like to update?: ")

                if question != "yes" and question != "no":
                    print('\033[1m'+'\nThis question must be answered with yes or no.'+'\033[0m')
                    print("-----------------------------------")
                    question = None
                    pass

            if question.lower() == "yes":
                category = None

                while category is None:
                    category = input("Category you want to change: ")

                    if category not in category_dict:
                        print('\033[1m'+'\nThis category does not exist.'+'\033[0m')
                        print("-----------------------------------")
                        category = None
                        pass

                if category.lower() == "name":
                    change = None

                    while change is None:
                        change = input("Change Contents to: ")

                        if not change.isalpha() and change.isnumeric():
                            print('\033[1m'+'\nThe Name must at least contain 1 letter.'+'\033[0m')
                            print("-----------------------------------")
                            change = None
                            pass

                        elif len(change) > 50:
                            print('\033[1m'+'\nThe Name cant have more than 50 characters.'+'\033[0m')
                            print("-----------------------------------")
                            change = None
                            pass

                elif category.lower() == "location":
                    change = None

                    while change is None:
                        change = input("Change Contents to: ")
                        if not len(change) == 3:
                            print('\033[1m'+'\nThe Location should for example look like this: A11.'+'\033[0m')
                            print("-----------------------------------")
                            change = None
                            pass

                        elif not change[0].isalpha() or not change[1].isdigit() or not change[2].isdigit():
                            print('\033[1m'+'\nThe Location should for example look like this: A11.'+'\033[0m')
                            print("-----------------------------------")
                            change = None
                            pass

                elif category.lower() == "quantity":
                    change = None

                    while change is None:
                        change = input("Change contents to: ")

                        if not change.isnumeric():
                            print('\033[1m'+'\nThe Quantity must only contain numbers.'+'\033[0m')
                            print("-----------------------------------")
                            change = None
                            pass

                        elif len(change) > 4:
                            print('\033[1m'+'\nThe Quantity cant have more than 4 characters.'+'\033[0m')
                            print("-----------------------------------")
                            change = None
                            pass

                session.query(Item).filter(Item.company_id.is_(str(c_id)) &
                                           Item.location.is_(str(location_of_item.capitalize())) &
                                           Item.name.is_(str(name_of_item.capitalize()))
                                           ).update({category_dict[category.lower()]: str(change.capitalize())})

                check = session.query(Item).filter(Item.company_id.is_(str(c_id)) &
                                                   category_dict[category.lower()].is_(str(change.capitalize())) &
                                                   Item.name.is_(str(name_of_item.capitalize()))).all()

                if len(check) > 1:
                    print('\033[1m'+'\nAn item with the same attributes does already exist.'+'\033[0m')
                    pass

                else:
                    print("Item info updated.")

                session.commit()
            elif question.lower() == "no":
                print('\033[1m'+'\nTry again.'+'\033[0m')
                pass

        else:
            print('\033[1m'+'\nPlease be more specific.'+'\033[0m')
            pass


def DELETE():
    name_of_item = None
    location_of_item = None

    while name_of_item is None:
        name_of_item = input("Full Name of the item: ")

        if not name_of_item.isalpha() and name_of_item.isnumeric():
            print('\033[1m'+'\nThe Name must at least have 1 letter.'+'\033[0m')
            print("-----------------------------------")
            name_of_item = None
            pass

        elif len(name_of_item) > 50:
            print('\033[1m'+'\nThere are no items longer than 50 characters.'+'\033[0m')
            print("-----------------------------------")
            name_of_item = None
            pass

    while location_of_item is None:
        location_of_item = input("Location of item: ")

        if not len(location_of_item) == 3:
            print('\033[1m'+'\nThe Location should for example look like this: A11.'+'\033[0m')
            print("-----------------------------------")
            location_of_item = None
            pass

        elif not location_of_item[0].isalpha() or not location_of_item[1].isdigit() or not location_of_item[2].isdigit():
            print('\033[1m'+'\nThe Location should for example look like this: A11'+'\033[0m')
            print("-----------------------------------")
            location_of_item = None
            pass

    s_filtered = session.query(Item).filter(Item.company_id.is_(str(c_id)) &
                                            Item.location.is_(str(location_of_item.capitalize())) &
                                            Item.name.is_(str(name_of_item.capitalize()))).all()

    if len(s_filtered) < 1:
        print('\033[1m'+'\nThere are no contents with that name and location.'+'\033[0m')
        pass

    else:
        for i in s_filtered:
            print(i)

        if len(s_filtered) < 2:
            question = None
            while question is None:
                print("-----------------------------------")
                question = input("Is this the item you would like to delete?: ")
                if question != "yes" and question != "no":
                    print('\033[1m'+'\nThis question must be answered with yes or no.'+'\033[0m')
                    print("-----------------------------------")
                    question = None
                    pass

            if question.lower() == "yes":
                for_deletion = session.query(Item).filter(Item.company_id.is_(str(c_id)) &
                                                          Item.location.is_(str(location_of_item.capitalize())) &
                                                          Item.name.is_(str(name_of_item.capitalize()))).all()[0]

                session.delete(for_deletion)
                session.commit()
                print("Item deleted.")

            elif question.lower() == "no":
                print('\033[1m'+'Try again.'+'\033[0m')
                pass

        else:
            print('\033[1m'+'\nPlease be more specific.'+'\033[0m')
            pass


def EXIT():
    exit()


while 1:
    print("-----------------------------------")
    action = input("What would you like to do: ")
    function_dict = {
        'create': CREATE,
        'read': READ,
        'delete': DELETE,
        'update': UPDATE,
        'exit': EXIT,
    }
    if action in function_dict:
        function_dict[action.lower()]()
    else:
        print('\033[1m'+'\nThis function does not exist.'+'\033[0m')
        pass
