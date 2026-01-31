# Day 9 - Top Products per Category

**Difficulty:** Medium
**Topics:** Grouping, Ranking, Window Functions
**Company:** Amazon

## Business Question

For each product category, find the top 2 products by total sales amount.

## Sample Data

**products table:**

| product_id | product_name | category    |
|------------|--------------|-------------|
| 1          | Laptop Pro   | Electronics |
| 2          | Mouse X      | Electronics |
| 3          | Desk Chair   | Furniture   |
| 4          | Keyboard Y   | Electronics |
| 5          | Standing Desk| Furniture   |

**sales table:**

| product_id | amount |
|------------|--------|
| 1          | 2000.0 |
| 1          | 1500.0 |
| 2          | 500.0  |
| 3          | 800.0  |
| 4          | 1000.0 |
| 5          | 1200.0 |

## Your Task

1. **Manually calculate** the top 2 products per category
2. Implement `get_top_products_per_category(products_df, sales_df, n=2)` in `solutions/day_09_solution.py`
3. Write tests in `tests/test_day_09.py`
4. Run `pytest tests/test_day_09.py -v` until all tests pass

## Function Signature

```python
def get_top_products_per_category(products_df: pd.DataFrame,
                                  sales_df: pd.DataFrame,
                                  n: int = 2) -> pd.DataFrame:
    """
    Get top N products by sales amount for each category.

    Args:
        products_df: DataFrame with columns [product_id, product_name, category]
        sales_df: DataFrame with columns [product_id, amount]
        n: Number of top products per category (default: 2)

    Returns:
        DataFrame with columns [category, product_name, total_sales]
        sorted by category, then by total_sales descending within each category
    """
    pass
```

## Expected Output Format

A DataFrame like:
```
      category product_name  total_sales
0  Electronics   Laptop Pro       3500.0
1  Electronics   Keyboard Y       1000.0
2    Furniture Standing Desk      1200.0
3    Furniture   Desk Chair        800.0
```

## Hints

- First, aggregate sales by product_id: group and sum
- Merge with products table to get product_name and category
- Group by category
- Within each category, sort by total_sales descending
- Use `.head(n)` within each group (`.groupby().apply()` or `.nlargest()`)
- Sort final result by category and total_sales

## SQL Equivalent

```sql
WITH product_sales AS (
  SELECT
    p.category,
    p.product_name,
    SUM(s.amount) as total_sales,
    ROW_NUMBER() OVER (PARTITION BY p.category ORDER BY SUM(s.amount) DESC) as rank
  FROM products p
  JOIN sales s ON p.product_id = s.product_id
  GROUP BY p.category, p.product_name
)
SELECT category, product_name, total_sales
FROM product_sales
WHERE rank <= 2
ORDER BY category, total_sales DESC;
```
