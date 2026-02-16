import pytest
import pandas as pd
from solutions.day_01_solution import calculate_total_sales

def test_calculate_total_sales_sample_data():
    sample_data = pd.DataFrame({
        'customer_id': [101, 102, 101, 103, 102],
        'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop'],
        'amount': [1200.0, 25.0, 75.0, 300.0, 1200.0]
    })

    result = calculate_total_sales(sample_data)

    assert result.iloc[0] == 1275
    assert result.iloc[1] == 1225
    assert result.iloc[2] == 300
    assert len(result) == 3


def test_calculate_total_sales_single_customer():
    test_data = pd.DataFrame({
        'customer_id': [1, 1, 1],
        'product': ['A', 'B', 'C'],
        'amount': [100.0, 200.0, 300.0]
    })
    result = calculate_total_sales(test_data)
    print(result.iloc[0])
    assert len(result) == 1
    assert result.iloc[0] == 600.0

def test_calculate_total_sales_sorting():
    test_data = pd.DataFrame({
        'customer_id': [1, 2, 3],
        'product': ['A', 'B', 'C'],
        'amount': [100.0, 500.0, 300.0]
    })
    result = calculate_total_sales(test_data)
    assert result.index[0] == 2
    assert result.index[1] == 3
    assert result.index[2] == 1
