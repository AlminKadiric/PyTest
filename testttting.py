import pytest

@pytest.fixture
def dbconnfixture():
    print("Connection to database")
    
@pytest.fixture
def dbdisconnfixture():
    print("Disconnecting from database")
    
    
def test_case_1(dbconnfixture,dbdisconnfixture):
    assert 1==1
    
    
