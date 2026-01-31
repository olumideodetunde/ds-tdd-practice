# Day 4 - High-Value Customers

**Difficulty:** Easy
**Topics:** Filtering, Aggregation
**Company:** Stripe

## Business Question

Find customers whose total purchases exceed $500. Return their customer IDs sorted.

## Sample Data

**purchases table:**

| customer_id | amount |
|-------------|--------|
| 1           | 300.0  |
| 2           | 150.0  |
| 1           | 250.0  |
| 3           | 600.0  |
| 2           | 400.0  |

## Your Task

1. **Manually calculate** which customers have total purchases > $500
2. Implement `find_high_value_customers(purchases_df, threshold=500)` in `solutions/day_04_solution.py`
3. Write tests in `tests/test_day_04.py`
4. Run `pytest tests/test_day_04.py -v` until all tests pass

## Function Signature

```python
def find_high_value_customers(purchases_df: pd.DataFrame, threshold: float = 500) -> list:
    """
    Find customers whose total purchases exceed the threshold.

    Args:
        purchases_df: DataFrame with columns [customer_id, amount]
        threshold: Minimum total purchase amount (default: 500)

    Returns:
        Sorted list of customer_ids
    """
    pass
```

## Expected Output Format

A sorted list:
```python
[1, 2, 3]
```

## Hints

- First group by customer_id and sum the amounts
- Then filter for totals > threshold
- Extract the index (customer_ids) and convert to a sorted list
- Make sure threshold is a parameter!

## SQL Equivalent

```sql
SELECT customer_id
FROM purchases
GROUP BY customer_id
HAVING SUM(amount) > 500
ORDER BY customer_id;
```
