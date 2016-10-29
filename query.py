"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

# Get the brand with the **id** of 8.
db.session.query(Brand.name).filter_by(id=8).one()
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
db.session.query(Model.name).filter_by(name="Corvette").all()

# Get all models that are older than 1960.
db.session.query(Model.name).filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.

db.session.query(Brand.name).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
db.session.query(Model.name).filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
db.session.query(Brand.name).filter((Brand.founded==1903) & (Brand.discontinued !=None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
db.session.query(Brand.name).filter((Brand.discontinued==None) | (Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.
db.session.query(Model.brand_name).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    pass

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
