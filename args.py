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

class unmanagedType(Exception):
    pass

class Parser():
    def __init__(self, schema: dict):
        self.schema = schema
        self.data_input_list = None

    def parsing(self, data: str):
        self.data_input_list = data.split()
        for data_entry in self.data_input_list:
            if self.is_a_flag(data_entry):
                if self.has_all_data_match_key_from_schema(data_entry) is False:
                    return False
                if self.data_has_double_flag(data_entry) is True:
                    return False

                value_type = self.flag_value_type(data_entry)
                flag_value = self.get_value_from(data_entry)

                if flag_value is None:
                    if not value_type is bool:
                        return False
                else:
                    if value_type is str and not flag_value.replace('/', '').isalpha():
                        return False
                    if value_type is int and not flag_value.isdigit():
                        return False
        return True

    def flag_value_type(self, data_entry):
        for _type in bool, str, int:
            if isinstance(self.schema[data_entry], _type):
                return _type
        raise unmanagedType
        

    def get_value_from(self, data_entry):
        try:
            flag_value =  self.data_input_list[ self.data_input_list.index(data_entry) + 1 ]
            return flag_value
        except IndexError as e:
            return None

    def is_a_flag(self, data_entry):
        if self.data_input_list.index(data_entry) % 2 == 0:
            return True
        return False

    def has_all_data_match_key_from_schema(self, data_entry):
        if data_entry in self.schema.keys():
            pass
        else:
            return False
        return True

    def data_has_double_flag(self, data_entry):
        if str(self.data_input_list).count(data_entry) > 1:
            return True
        return False


        
@pytest.fixture
def parser():
    schema = {
        "-l": False,
        "-p": 0,
        "-d": ""
    }
    parser = Parser(schema)
    return parser

def test_is_schema_a_dict(parser):
    assert isinstance(parser.schema, dict)

def test_data_match_key_from_schema(parser):
    assert parser.parsing("-d /tmp") == True

def test_data_one_value_dont_match_key_from_schema(parser):
    assert parser.parsing("-d toto -q") == False

def test_double_flags_are_invalid(parser):
    assert parser.parsing("-d toto -d") == False

def test_value_is_missing_for_a_flag_that_require_it(parser):
    assert parser.parsing("-d") == False

def test_value_is_missing_for_bool_flag_but_its_ok(parser):
    assert parser.parsing("-l") == True

def test_int_flag_with_int_value(parser):
    assert parser.parsing("-p 8080") == True

def test_int_flag_without_int_value(parser):
    assert parser.parsing("-p /tmp") == False

def test_one_of_flag_has_wrong_parameter_type(parser):
    assert parser.parsing("-d /totot -p /tmp") == False

def test_two_ok_parameters(parser):
    assert parser.parsing("-d /totot -p 809") == True

def test_three_ok_parameters(parser):
    assert parser.parsing("-d /totot -p 809 -l") == True

def test_three_nok_parameters(parser):
    assert parser.parsing("-d 80 -p 809 -l") == False

def test_unknown_flag(parser):
    assert parser.parsing("-k jige") == False

def test_with_explicit_bool_false_value(parser):
    assert parser.parsing("-l False") == True

def test_with_explicit_bool_true_value(parser):
    assert parser.parsing("-l True") == True

def test_empty(parser):
    assert parser.parsing("") == True