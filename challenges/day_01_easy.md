# Day 1 - Total Sales by Customer

**Difficulty:** Easy
**Topics:** GroupBy, Aggregation
**Company:** Amazon

## Business Question

Calculate the total sales amount for each customer and return them sorted by total sales (highest first).

## Sample Data

**sales table:**

| customer_id | product  | amount |
|-------------|----------|--------|
| 101         | Laptop   | 1200.0 |
| 102         | Mouse    | 25.0   |
| 101         | Keyboard | 75.0   |
| 103         | Monitor  | 300.0  |
| 102         | Laptop   | 1200.0 |

## Your Task

1. **Manually calculate** the expected answer using the sample data above
2. Implement `calculate_total_sales(sales_df)` in `solutions/day_01_solution.py`
3. Write tests in `tests/test_day_01.py`
4. Run `pytest tests/test_day_01.py -v` until all tests pass

## Function Signature

```python
def calculate_total_sales(sales_df: pd.DataFrame) -> pd.Series:
    """
    Calculate total sales per customer, sorted descending.

    Args:
        sales_df: DataFrame with columns [customer_id, product, amount]

    Returns:
        Series with customer_id as index and total_sales as values,
        sorted by total_sales descending
    """
    pass
```

## Expected Output Format

A pandas Series like:
```
customer_id
102    1225.0
101    1275.0
103     300.0
Name: amount, dtype: float64
```

## Hints

- Use `groupby()` to group by customer_id
- Use `sum()` to aggregate amounts
- Use `sort_values()` with `ascending=False` to sort
- Remember: highest sales first!

## SQL Equivalent

```sql
SELECT customer_id, SUM(amount) as total_sales
FROM sales
GROUP BY customer_id
ORDER BY total_sales DESC;
```
