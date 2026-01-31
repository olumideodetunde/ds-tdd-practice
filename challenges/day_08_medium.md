# Day 8 - Customer Retention Rate

**Difficulty:** Medium
**Topics:** Set Operations, Date Logic
**Company:** Netflix

## Business Question

Calculate the customer retention rate: what percentage of customers who made a purchase in January 2024 also made a purchase in February 2024?

## Sample Data

**purchases table:**

| customer_id | purchase_date |
|-------------|---------------|
| 1           | 2024-01-10   |
| 2           | 2024-01-15   |
| 3           | 2024-01-20   |
| 1           | 2024-02-05   |
| 2           | 2024-02-10   |
| 4           | 2024-02-15   |

## Your Task

1. **Manually calculate** the retention rate
2. Implement `calculate_retention_rate(purchases_df, month1='2024-01', month2='2024-02')` in `solutions/day_08_solution.py`
3. Write tests in `tests/test_day_08.py`
4. Run `pytest tests/test_day_08.py -v` until all tests pass

## Function Signature

```python
def calculate_retention_rate(purchases_df: pd.DataFrame,
                             month1: str = '2024-01',
                             month2: str = '2024-02') -> float:
    """
    Calculate customer retention rate between two months.

    Args:
        purchases_df: DataFrame with columns [customer_id, purchase_date]
        month1: First month in 'YYYY-MM' format
        month2: Second month in 'YYYY-MM' format

    Returns:
        Retention rate as percentage (0-100)
    """
    pass
```

## Expected Output Format

A float like:
```python
66.67  # means 66.67% retention
```

## Hints

- Convert purchase_date to datetime
- Extract month in 'YYYY-MM' format
- Get unique customers for each month (use `set()` or `.unique()`)
- Find intersection: customers in both months
- Retention rate = (customers in both / customers in month1) * 100
- Return 0 if no customers in month1

## Calculation Example

From sample data:
- January customers: {1, 2, 3}
- February customers: {1, 2, 4}
- Retained (in both): {1, 2}
- Retention rate: 2/3 * 100 = 66.67%

## SQL Equivalent

```sql
WITH jan_customers AS (
  SELECT DISTINCT customer_id
  FROM purchases
  WHERE DATE_FORMAT(purchase_date, '%Y-%m') = '2024-01'
),
feb_customers AS (
  SELECT DISTINCT customer_id
  FROM purchases
  WHERE DATE_FORMAT(purchase_date, '%Y-%m') = '2024-02'
)
SELECT
  COUNT(DISTINCT f.customer_id) * 100.0 / COUNT(DISTINCT j.customer_id) as retention_rate
FROM jan_customers j
LEFT JOIN feb_customers f ON j.customer_id = f.customer_id;
```
