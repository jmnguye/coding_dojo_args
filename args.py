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
'''

class NumberOfArgsDontMatchNumberOfFlag(Exception):
    pass

class Parser():
    
    def load(self, schema):
        number_of_args = self.get_args(schema)
        number_of_flags = len(self.get_flags(schema))
        if number_of_args != number_of_flags:
            raise NumberOfArgsDontMatchNumberOfFlag

           
    def get_args(self, schema) -> int:
        return int(schema[0])

    def get_flags(self, schema) -> List[str]:
        flags = schema.split(' ')[1]
        return flags.split(',')

@pytest.fixture
def parser():
    parser = Parser()
    return parser

def test_read_number_by(parser):
    schema = "3 l,p,d"
    assert 3 == parser.get_args(schema)

def test_miss_number_by(parser):
    schema = "l,p,d"
    with pytest.raises(ValueError):
        parser.get_args(schema)

def test_read_flags_by(parser):
    schema = "3 l,p,d"
    assert ['l', 'p', 'd'] == parser.get_flags(schema)

def test_number_of_args_match_number_of_flags(parser):
    schema = "3 l,p,d,t"
    with pytest.raises(NumberOfArgsDontMatchNumberOfFlag):
        parser.load(schema)

