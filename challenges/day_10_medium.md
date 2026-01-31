# Day 10 - User Activity Streak

**Difficulty:** Medium
**Topics:** Date Logic, Streak Calculation
**Company:** Duolingo

## Business Question

Find the longest consecutive days streak for each user based on their activity dates.

## Sample Data

**user_activity table:**

| user_id | activity_date |
|---------|---------------|
| 1       | 2024-01-01   |
| 1       | 2024-01-02   |
| 1       | 2024-01-03   |
| 1       | 2024-01-05   |
| 2       | 2024-01-10   |
| 2       | 2024-01-11   |
| 2       | 2024-01-15   |

## Your Task

1. **Manually calculate** the longest streak for each user
2. Implement `calculate_longest_streak(activity_df)` in `solutions/day_10_solution.py`
3. Write tests in `tests/test_day_10.py`
4. Run `pytest tests/test_day_10.py -v` until all tests pass

## Function Signature

```python
def calculate_longest_streak(activity_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the longest consecutive days streak for each user.

    Args:
        activity_df: DataFrame with columns [user_id, activity_date]

    Returns:
        DataFrame with columns [user_id, longest_streak]
        sorted by user_id
    """
    pass
```

## Expected Output Format

A DataFrame like:
```
   user_id  longest_streak
0        1               3
1        2               2
```

## Hints

- Convert activity_date to datetime
- Sort by user_id and activity_date
- For consecutive days: difference between consecutive dates should be 1 day
- One approach: calculate date differences, identify when streak breaks
- Group consecutive dates into streak groups
- Count days in each streak group
- Take the maximum streak per user
- Alternative: Use `.diff()` to find gaps, then count consecutive runs

## Manual Calculation

User 1: [Jan 1, 2, 3] = 3 days consecutive, then gap, then [Jan 5] = 1 day
  - Longest streak: 3

User 2: [Jan 10, 11] = 2 days consecutive, then gap, then [Jan 15] = 1 day
  - Longest streak: 2

## SQL Equivalent (Advanced)

```sql
WITH date_diffs AS (
  SELECT
    user_id,
    activity_date,
    DATE_SUB(activity_date, INTERVAL ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY activity_date) DAY) as streak_group
  FROM user_activity
),
streak_counts AS (
  SELECT
    user_id,
    streak_group,
    COUNT(*) as streak_length
  FROM date_diffs
  GROUP BY user_id, streak_group
)
SELECT
  user_id,
  MAX(streak_length) as longest_streak
FROM streak_counts
GROUP BY user_id
ORDER BY user_id;
```
