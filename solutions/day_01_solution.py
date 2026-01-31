"""
Day 1 Solution: Total Sales by Customer

Your task:
1. Read the challenge in challenges/day_01_easy.md
2. Manually calculate the expected answer
3. Implement the function below
4. Write tests in tests/test_day_01.py
5. Run: pytest tests/test_day_01.py -v
"""

import pandas as pd


def calculate_total_sales(sales_df: pd.DataFrame) -> pd.Series:
    """
    Calculate total sales per customer, sorted descending.

    Args:
        sales_df: DataFrame with columns [customer_id, product, amount]

    Returns:
        Series with customer_id as index and total_sales as values,
        sorted by total_sales descending
    """
    # TODO: Implement your solution here
    pass
