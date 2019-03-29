import pytest
import sys

# test will fail
'''def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
'''

# test will pass
def sum(num1, num2):
    return num1 + num2

def add(x, y=2):
    return x + y

def product(x, y=2):
    return x * y

# pytest fixtures is to set the baseline as in which test can reliably and repeatedly execute
'''
@pytest.fixture
def get_sum_test_data():
    return [(3, 5, 8),(-2, -2, -5), (-1, 5, 4), (3, -5, -2), (0, 5, 5)]
    
def test_sum(get_sum_test_data):
    for data in get_sum_test_data:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]
        assert sum(num1, num2) == expected
'''

# create a function to set the variables for the test function (makes the codes more neat)
def get_sum_test_data():
    return [(3, 5, 8),(-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)]

#pytest.mark.parametrize decorator enables parametrization of arguments for a test function.
@pytest.mark.parametrize('num1, num2, expected', get_sum_test_data())
def test_sum(num1, num2, expected):
    assert sum(num1, num2) == expected

@pytest.mark.skipif(sys.version_info > (3, 3),reason="do not run test")
def test_sum_output_type():
    assert type(sum(1, 2)) is int

@pytest.mark.number
def test_product():
    assert product(5, 5) == 25
    assert product(5) == 10
    print(product(5, 5), '---------------------------')

@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('Hello ', 'World', 'Hello World'),
                             (10.5, 25.5, 36)
                         ]
                         )
def test_add(num1, num2, result):
    assert add(num1, num2) == result

@pytest.mark.string
def test_add_string():
    result = add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result

@pytest.mark.string
def test_product_string():
    assert product('Hello ', 3) == 'Hello Hello Hello '
    result = product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
