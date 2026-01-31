# Day 5 - Product Sales Count

**Difficulty:** Easy
**Topics:** Counting, Sorting
**Company:** Walmart

## Business Question

Count how many times each product was sold and return the top 3 most sold products.

## Sample Data

**sales table:**

| sale_id | product     |
|---------|-------------|
| 1       | Laptop      |
| 2       | Mouse       |
| 3       | Laptop      |
| 4       | Keyboard    |
| 5       | Laptop      |
| 6       | Mouse       |
| 7       | Monitor     |

## Your Task

1. **Manually calculate** which products were sold most frequently (top 3)
2. Implement `get_top_products(sales_df, n=3)` in `solutions/day_05_solution.py`
3. Write tests in `tests/test_day_05.py`
4. Run `pytest tests/test_day_05.py -v` until all tests pass

## Function Signature

```python
def get_top_products(sales_df: pd.DataFrame, n: int = 3) -> pd.Series:
    """
    Get top N most sold products by count.

    Args:
        sales_df: DataFrame with columns [sale_id, product]
        n: Number of top products to return (default: 3)

    Returns:
        Series with product as index and count as values,
        sorted by count descending, limited to top n
    """
    pass
```

## Expected Output Format

A pandas Series like:
```
product
Laptop      3
Mouse       2
Keyboard    1
Name: count, dtype: int64
```

## Hints

- Use `value_counts()` on the product column
- This automatically counts and sorts descending
- Use `.head(n)` to get top n results
- Alternative: `groupby().size()` then sort

## SQL Equivalent

```sql
SELECT product, COUNT(*) as sale_count
FROM sales
GROUP BY product
ORDER BY sale_count DESC
LIMIT 3;
```
