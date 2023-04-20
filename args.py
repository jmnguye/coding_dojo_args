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

class Parser():
    
    def load(self, schema):
        self.get_args(schema)
           
    def get_args(self, schema) -> int:
        return int(schema[0])

    def get_flags(self, schema) -> List[str]:
        flags = schema.split(' ')[1]
        return flags.split(',')

@pytest.fixture
def parser():
    parser = Parser()
    return parser

def test_parser_read_number_args(parser):
    schema = "3 l,p,d"
    parser.load(schema)
    assert 3 == parser.get_args(schema)

def test_parser_miss_number_args(parser):
    schema = "l,p,d"
    with pytest.raises(ValueError):
        parser.get_args(schema)