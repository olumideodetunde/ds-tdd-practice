"""
Tests for Day 1: Total Sales by Customer

Your task:
1. Manually calculate the expected answer from the sample data
2. Write tests to verify your solution
3. Run: pytest tests/test_day_01.py -v
"""

import pytest
import pandas as pd
from solutions.day_01_solution import calculate_total_sales


def test_calculate_total_sales_sample_data():
    """Test with the sample data from the challenge."""
    # Arrange - Create the sample data
    sample_data = pd.DataFrame({
        'customer_id': [101, 102, 101, 103, 102],
        'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop'],
        'amount': [1200.0, 25.0, 75.0, 300.0, 1200.0]
    })

    # Act - Run your solution
    result = calculate_total_sales(sample_data)

    # Assert - Check against YOUR manual calculation
    # TODO: Fill in the expected values based on your manual calculation
    # Customer 101: ??? (calculate yourself!)
    # Customer 102: ??? (calculate yourself!)
    # Customer 103: ??? (calculate yourself!)

    assert result.iloc[0] == ???  # Highest total sales
    assert result.iloc[1] == ???  # Second highest
    assert result.iloc[2] == ???  # Third highest
    assert len(result) == 3


def test_calculate_total_sales_single_customer():
    """Test with only one customer."""
    test_data = pd.DataFrame({
        'customer_id': [1, 1, 1],
        'product': ['A', 'B', 'C'],
        'amount': [100.0, 200.0, 300.0]
    })

    result = calculate_total_sales(test_data)

    assert len(result) == 1
    assert result[1] == 600.0


def test_calculate_total_sales_empty_dataframe():
    """Test with empty DataFrame."""
    empty_df = pd.DataFrame(columns=['customer_id', 'product', 'amount'])

    result = calculate_total_sales(empty_df)

    assert len(result) == 0


def test_calculate_total_sales_sorting():
    """Test that results are sorted by amount descending."""
    test_data = pd.DataFrame({
        'customer_id': [1, 2, 3],
        'product': ['A', 'B', 'C'],
        'amount': [100.0, 500.0, 300.0]
    })

    result = calculate_total_sales(test_data)

    # Verify descending order
    assert result.index[0] == 2  # Customer 2 has highest (500)
    assert result.index[1] == 3  # Customer 3 is second (300)
    assert result.index[2] == 1  # Customer 1 is third (100)
