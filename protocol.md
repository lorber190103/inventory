# The Idea
- I wanted to have an website where you could choose a company.
- After you choose the company you can read, create, update and delete items from that database.

## 12.01.2023
- Created a GitHub Repository

## 18.01.2023
- Added User-Stories

## 19.01.2023
- Added an ER-Diagramm
- Added model.py
    - model.py creates two databases
- Added fill.py
    - fill.py populates the two databases with 5 companys and 250 items
- Added items.md
    - In items.md are 250 items that are used to populate the database

## 20.01.2023
- Added .gitignore

## 25.01.2023
- Added Django

## 26.01.2023
- Added crud.py
    - crud.py can read, create, update and delete items in the database
    - this uses ready-made inputs
- Tried to work on Django

## 02.02.2023
- Stopped working on Django
- Added main.py
    - In main.py i added functions where you can choose a company and read, create, update and delete items

## 04.02.2023
- Added requirements.txt
- Worked on main.py

## 09.02.2023
- Added flake8
- Added sefup.cfg
- Added setup.py
- Added whitelist.txt

## End Product? (10.02.2023)
- You can use the Commandline to choose a company
- After you chose a company you can choose between READ, CREATE, UPDATE, DELETE, EXIT
- In READ you can either have the whole database printed out to you or you can choose what you want to search for
- In CREATE you can add an item to the database.
- In UPDATE you can update an item from the database.
- In DELETE you can delete an item from the database.
- In EXIT you exit the programm.
- If an item has the same name and location of the item you want to CREATE or UPDATE, it won't let you create or update it.