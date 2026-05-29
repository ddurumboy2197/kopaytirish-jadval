# test_table_generator.py
import pytest
from table_generator import generate_table

def test_generate_table():
    result = generate_table(5)
    assert result == [[1, 2, 3, 4, 5],
                     [2, 4, 6, 8, 10],
                     [3, 6, 9, 12, 15],
                     [4, 8, 12, 16, 20],
                     [5, 10, 15, 20, 25]]

def test_generate_table_zero():
    result = generate_table(0)
    assert result == []

def test_generate_table_negative():
    with pytest.raises(ValueError):
        generate_table(-1)
