# Day 6 - Employee Department Lookup

**Difficulty:** Easy
**Topics:** Join, Merge
**Company:** LinkedIn

## Business Question

Match employees with their department names. Return employee name and department name.

## Sample Data

**employees table:**

| employee_id | name    | department_id |
|-------------|---------|---------------|
| 1           | Alice   | 10            |
| 2           | Bob     | 20            |
| 3           | Charlie | 10            |
| 4           | David   | 30            |

**departments table:**

| department_id | department_name |
|---------------|-----------------|
| 10            | Engineering     |
| 20            | Sales           |
| 30            | Marketing       |

## Your Task

1. **Manually calculate** which employee works in which department
2. Implement `match_employee_departments(employees_df, departments_df)` in `solutions/day_06_solution.py`
3. Write tests in `tests/test_day_06.py`
4. Run `pytest tests/test_day_06.py -v` until all tests pass

## Function Signature

```python
def match_employee_departments(employees_df: pd.DataFrame,
                               departments_df: pd.DataFrame) -> pd.DataFrame:
    """
    Join employees with their department names.

    Args:
        employees_df: DataFrame with columns [employee_id, name, department_id]
        departments_df: DataFrame with columns [department_id, department_name]

    Returns:
        DataFrame with columns [name, department_name]
    """
    pass
```

## Expected Output Format

A DataFrame like:
```
       name department_name
0     Alice     Engineering
1       Bob           Sales
2   Charlie     Engineering
3     David       Marketing
```

## Hints

- Use `merge()` or `join()` to combine the tables
- Merge on `department_id` (the common column)
- Select only the columns `name` and `department_name`
- This is an inner join (default)

## SQL Equivalent

```sql
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
```
