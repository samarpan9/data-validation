from pickle import TRUE
from cerberus import Validator

schema = {'name': {'type': 'string','maxlength': 10, 'minlength' : 2}, 'age': {'type': 'integer', 'min': 18, 'max' : 60}}
document = {'name': "hello", 'age': 20}

def validate_func(schema,document):
    v = Validator()
    a = v.validate(document, schema)
    if a == True:
        print("There are no errors.")
    else:
        print("you've got error:", v.errors)

validate_func(schema,document)

