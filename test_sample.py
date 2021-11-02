"""
    Author: Lori White
    Purpose: Showing how to use pytest for python.
"""
import pytest

def increase_by_two(number_to_increase):
    """
     Increases a number by 2.
    """
    assert isinstance(number_to_increase, (int,float)) and \
         not isinstance(number_to_increase, bool), "Invalid input."
    return number_to_increase + 2

def test_success_of_increase_by_two():
    """
     Tests the increases_by_two function with ints and floats.
    """
    assert increase_by_two(3) == 5
    assert increase_by_two(-2) == 0
    assert increase_by_two(2.5) == 4.5

def test_failure_of_increase_by_two():
    """
     Tests the increases_by_two function with strings and booleans.
    """    
    with pytest.raises(AssertionError) as error_info:
        increase_by_two("")
    assert "Invalid input." in str(error_info)
    with pytest.raises(AssertionError) as error_info:
        increase_by_two(True)
    assert "Invalid input." in str(error_info)
