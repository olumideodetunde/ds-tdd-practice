# Day 2 - Active Users

**Difficulty:** Easy
**Topics:** Filtering, Unique Values
**Company:** Meta

## Business Question

Find all unique user IDs who made at least one purchase in January 2024.

## Sample Data

**purchases table:**

| user_id | purchase_date | amount |
|---------|---------------|--------|
| 1       | 2024-01-15   | 50.0   |
| 2       | 2023-12-20   | 30.0   |
| 1       | 2024-01-20   | 25.0   |
| 3       | 2024-01-05   | 100.0  |
| 2       | 2024-02-10   | 75.0   |

## Your Task

1. **Manually calculate** which users made purchases in January 2024
2. Implement `get_active_users(purchases_df)` in `solutions/day_02_solution.py`
3. Write tests in `tests/test_day_02.py`
4. Run `pytest tests/test_day_02.py -v` until all tests pass

## Function Signature

```python
def get_active_users(purchases_df: pd.DataFrame) -> list:
    """
    Get unique user IDs who made purchases in January 2024.

    Args:
        purchases_df: DataFrame with columns [user_id, purchase_date, amount]

    Returns:
        Sorted list of unique user_ids
    """
    pass
```

## Expected Output Format

A sorted list:
```python
[1, 3]
```

## Hints

- Convert `purchase_date` to datetime using `pd.to_datetime()`
- Filter for dates where year is 2024 AND month is 1
- Use `.dt.year` and `.dt.month` accessors
- Get unique values with `.unique()` or `.tolist()`
- Don't forget to sort the result!

## SQL Equivalent

```sql
SELECT DISTINCT user_id
FROM purchases
WHERE YEAR(purchase_date) = 2024
  AND MONTH(purchase_date) = 1
ORDER BY user_id;
```
