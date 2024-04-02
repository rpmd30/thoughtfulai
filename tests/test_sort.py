import pytest
from main import sort

def test_sort_rejected():
    # Test case: bulky and heavy package
    assert sort(500, 500, 500, 30) == "REJECTED"
    
def test_sort_special_bulky():
    # Test case: only bulky package
    assert sort(500, 500, 500, 10) == "SPECIAL"

def test_sort_special_heavy():
    # Test case: only heavy package
    assert sort(50, 50, 50, 30) == "SPECIAL"

def test_sort_standard():    
    # Test case: standard package
    assert sort(50, 50, 50, 10) == "STANDARD"