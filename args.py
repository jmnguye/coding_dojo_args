import pytest
'''
https://codingdojo.org/kata/Args/
write a parser that takes a schema as input detailing:
    how many args
    what types
    what are the requested values

Once schema defined, the programe should send the list to the parser

The parser will check
'''
schema_definition = "3"

def get_args(schema_definition) -> int:
    return int(schema_definition[0])


def test_get_schema_definition():
    assert schema_definition is not None

def test_request_3_args():
    schema_definition = "3"
    assert 3 == get_args(schema_definition)

def test_get_flags():
    assert 3 == len(get_flags())