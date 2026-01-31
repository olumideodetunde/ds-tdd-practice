# Day 7 - Monthly Revenue Growth

**Difficulty:** Medium
**Topics:** Date Manipulation, Window Functions
**Company:** Uber

## Business Question

Calculate the month-over-month revenue growth percentage for each month in 2024.

## Sample Data

**sales table:**

| sale_date  | amount |
|------------|--------|
| 2024-01-15 | 1000.0 |
| 2024-01-20 | 1500.0 |
| 2024-02-10 | 3000.0 |
| 2024-02-25 | 2000.0 |
| 2024-03-05 | 4000.0 |
| 2024-03-15 | 5000.0 |

## Your Task

1. **Manually calculate** the month-over-month growth percentage
2. Implement `calculate_revenue_growth(sales_df)` in `solutions/day_07_solution.py`
3. Write tests in `tests/test_day_07.py`
4. Run `pytest tests/test_day_07.py -v` until all tests pass

## Function Signature

```python
def calculate_revenue_growth(sales_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate month-over-month revenue growth percentage.

    Args:
        sales_df: DataFrame with columns [sale_date, amount]

    Returns:
        DataFrame with columns [month, revenue, growth_pct]
        where month is in 'YYYY-MM' format and growth_pct is percentage change
        from previous month (NaN for first month)
    """
    pass
```

## Expected Output Format

A DataFrame like:
```
    month  revenue  growth_pct
0  2024-01   2500.0         NaN
1  2024-02   5000.0      100.0
2  2024-03   9000.0       80.0
```

## Hints

- Convert sale_date to datetime
- Extract year-month using `.dt.to_period('M')` or format with `.dt.strftime('%Y-%m')`
- Group by month and sum revenue
- Use `.pct_change()` to calculate percentage change
- Multiply by 100 to get percentage
- Round to reasonable decimal places

## SQL Equivalent

```sql
WITH monthly_revenue AS (
  SELECT
    DATE_FORMAT(sale_date, '%Y-%m') as month,
    SUM(amount) as revenue
  FROM sales
  GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
)
SELECT
  month,
  revenue,
  (revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month) * 100 as growth_pct
FROM monthly_revenue
ORDER BY month;
```
