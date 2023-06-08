from collections import namedtuple
import pytest
import sqlite3

Person = namedtuple('Person', 'first_name last_name')  # create object to test

FIRST_NAME = "Guido"
LAST_NAME = "Von Rossum"

db_conn = sqlite3.connect('../../DATA/presidents.db')
db_cursor = db_conn.cursor()
db_cursor.row_factory = sqlite3.Row  # set the row factory to be a Row object

@pytest.fixture
def presidents():
    db_cursor.execute('select * from presidents')
    return db_cursor.fetchall()

@pytest.fixture  # mark person as a fixture
def person():
    """
    Return a 'Person' named tuple with fields 'first_name' and 'last_name'
    """
    return Person(FIRST_NAME, LAST_NAME)  # return value of fixture

def test_first_name(person):  # pass fixture as test parameter
    assert person.first_name == FIRST_NAME

def test_last_name(person):  # pass fixture as test parameter
    assert person.last_name == LAST_NAME

def test_john_tyler_is_from_virginia(presidents):
    assert presidents[9]['birthstate'] == 'Virginia'  # John Tyler is 10th president

if __name__ == "__main__":
    pytest.main(['-v', __file__])