# Day 3 - Average Order Value

**Difficulty:** Easy
**Topics:** Aggregation, Grouping
**Company:** Shopify

## Business Question

Calculate the average order value (total amount per order) for each customer.

## Sample Data

**orders table:**

| order_id | customer_id | amount |
|----------|-------------|--------|
| 1        | 101         | 50.0   |
| 2        | 102         | 100.0  |
| 3        | 101         | 150.0  |
| 4        | 102         | 200.0  |
| 5        | 101         | 100.0  |

## Your Task

1. **Manually calculate** the average order value for each customer
2. Implement `calculate_avg_order_value(orders_df)` in `solutions/day_03_solution.py`
3. Write tests in `tests/test_day_03.py`
4. Run `pytest tests/test_day_03.py -v` until all tests pass

## Function Signature

```python
def calculate_avg_order_value(orders_df: pd.DataFrame) -> pd.Series:
    """
    Calculate average order value per customer.

    Args:
        orders_df: DataFrame with columns [order_id, customer_id, amount]

    Returns:
        Series with customer_id as index and avg_order_value as values
    """
    pass
```

## Expected Output Format

A pandas Series like:
```
customer_id
101    100.0
102    150.0
Name: amount, dtype: float64
```

## Hints

- Use `groupby('customer_id')` to group by customer
- Use `mean()` to calculate average
- The result will naturally have customer_id as the index

## SQL Equivalent

```sql
SELECT customer_id, AVG(amount) as avg_order_value
FROM orders
GROUP BY customer_id;
```
