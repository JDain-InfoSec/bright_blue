import pickle
import sqlalchemy
from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy import Table, Column, Integer, Date, String, Float
import os


# checking to see if there is a saved pickle file.
if os.path.isfile('save.p'):
    # if it finds a saved variable file it will apply them at the start of the
    # programs
    with open('save.p','rb') as file:
        b = pickle.load(file)
else:
    #default setting for the application
    # add new variables here when adding a new feature
    b = 15
# This function is going to be used to save the configuration of the user
def save_settings():
    pass

def get_price_per_square(price, x, y):
    area = x * y
    ppi = price / area
    # Rounds to four decimal points due to how small the price point is
    return round(ppi, 4)
# Function to add
def add_new_mat(price, x, y, color, company):
    pass

def get_remaining_amount(id):
    pass

def convert_foot_to_inch(foot):
    inch = foot * 12
    return inch

def table_check(name):
    if not inspector.has_table(name):  # If table don't exist, Create.
        metadata = MetaData(engine)
        if name == 'vinyl':
            Table('vinyl', metadata,
                  Column('Id', Integer, primary_key=True, nullable=False),
                  Column('Date', Date), Column('Country', String),
                  Column('Brand', String), Column('Price', Float),)
            # Implement the creation
            metadata.create_all()
        if name == 'products':
            Table('products', metadata,
                  Column('Id', Integer, primary_key=True, nullable=False),
                  Column('Date', Date), Column('Name', String),
                  Column('Amount', Integer), Column('Costs', Float),
                  Column('Sale Price', Float), Column('Number Sold', Integer),
                  Column('Materials', Integer), Column('Product Image', String))
            # Implement the creation
            metadata.create_all()


pickle.dump(a, open('save.p', 'wb'))


print(b)


#SQL Table Section
engine = create_engine("sqlite:///cutcal.db")  # Access the DB Engine
inspector = inspect(engine)
#Checking for Vinyal Table
table_check('vinyl')
table_check('products')
