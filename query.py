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
db.session.query(Model.year).filter((Model.name=="Corvette") & (Model.brand_name=="Chevrolet")).all()

# Get all models that are older than 1960.
db.session.query(Model.name).filter(Model.year > 1960).group_by(Model.name).all()

# Get all brands that were founded after 1920.

db.session.query(Brand.name).filter(Brand.founded > 1920).group_by(Brand.name).all()

# Get all models with names that begin with "Cor".
db.session.query(Model.name).filter(Model.name.like('Cor%')).group_by(Model.name).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
db.session.query(Brand.name).filter((Brand.founded==1903) & (Brand.discontinued !=None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
db.session.query(Brand.name).filter((Brand.discontinued==None) | (Brand.founded < 1950)).group_by(Brand.name).all()

# Get all models whose brand_name is not Chevrolet.
db.session.query(Model.brand_name).filter(Model.brand_name != 'Chevrolet').group_by(Model.brand_name).all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    
    model_info = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year==year).group_by(Model.name, Model.brand_name, Brand.headquarters).all()
    
    for model in model_info:
        print model.name +": " + model.brand_name + "; " + model.headquarters + "\n"



def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
   
    model_info = db.session.query(Model.brand_name, Model.name).group_by(Model.brand_name, Model.name).all()

    for model in model_info:
        print model.brand_name + ": " + model.name + "\n"
   

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
#ANS: a BasQuery object with the memory location of that object this object holds all the Brand class instances with a name attribue Ford but in order to access the informaton of this object we need to call the method .all() which will give us a list of tupules of all the instances of the the class Brand that have name attribute Ford.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
#And association table is a middle table that creates a connection btween two tables that have a many to many relationship. This association table has fields that are usally just keeping id or code values so the feilds have little meaningful data. But these id feilds create a bridge between two tables that have strong association through these foriegn keys. 

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    
    part_name = "%" + mystr + "%"
    
    model_info = db.session.query(Model.brand_name).filter(Model.brand_name.like(part_name)).group_by(Model.brand_name).all()

    for model in model_info:
        print model.brand_name

def get_models_between(start_year, end_year):
    model_info = db.session.query(Model.name).filter((Model.year >= start_year) & (Model.year < end_year)).group_by(Model.name).order_by(Model.name).all()

    for model in model_info:
        print model.name
