import pytest
from typing import List
'''
https://codingdojo.org/kata/Args/
write a parser that takes a schema as input detailing:
    how many args
    what types
    what are the requested values

Once schema defined, the programe should send the list to the parser

The parser will check

define types of parameters :
boolean : if the param is there , true, else false
number : param should be followed by a number
string : param should be followed by some string

if values are not filled, default value are applied '''

class Parser():
    def __init__(self, schema: dict):
        self.schema = schema

    def check(self, data: str): 
        if data is None:
            return " ".join([ f"-{key} {self.schema.get(key)}" for key in self.schema.keys() ])
            
        for entry in data.split():
            if entry in [ f"-{key}" for key in self.schema.keys() ]:
                value = next()


        
@pytest.fixture
def parser():
    schema = {
        "l": False,
        "p": 0,
        "d": ""
    }
    parser = Parser(schema)
    return parser

def test_is_schema_a_dict(parser):
    assert isinstance(parser.schema, dict)

def test_get_params_without_data(parser):
    assert "-l" in parser.check("")

def test_get_params_value_without_data(parser):
    assert "-p 0" in parser.check("")

def test_get_custom_params_from_data(parser):
    assert "-d /tmp" in parser.check("-d /tmp")