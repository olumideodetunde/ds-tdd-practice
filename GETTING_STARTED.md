# Getting Started with DS TDD Practice

## Quick Start

### 1. Install Dependencies

```bash
# Initialize with uv (if not already done)
uv init

# Install dependencies
uv sync
```

### 2. Start Your First Challenge

```bash
# Get today's challenge (starts with Day 1)
python -m utils.challenge_manager today
```

### 3. Read the Challenge

Open `challenges/day_01_easy.md` and read through:
- The business question
- The sample data
- The expected output format
- Hints

### 4. Manual Calculation (IMPORTANT!)

**Before writing any code**, calculate the answer by hand:

Example for Day 1:
```
Customer 101: Laptop (1200) + Keyboard (75) = 1275
Customer 102: Mouse (25) + Laptop (1200) = 1225
Customer 103: Monitor (300) = 300

Sorted descending: 101 (1275), 102 (1225), 103 (300)
```

### 5. Write Tests First (TDD!)

Open `tests/test_day_01.py` and fill in the expected values:

```python
def test_calculate_total_sales_sample_data():
    # ... setup code ...

    # Fill in YOUR calculated values
    assert result.iloc[0] == 1275.0  # Customer 101
    assert result.iloc[1] == 1225.0  # Customer 102
    assert result.iloc[2] == 300.0   # Customer 103
```

### 6. Run Tests (They Should Fail)

```bash
pytest tests/test_day_01.py -v
```

Expected output: `FAILED` (because you haven't written the solution yet)

### 7. Implement the Solution

Open `solutions/day_01_solution.py` and implement:

```python
def calculate_total_sales(sales_df: pd.DataFrame) -> pd.Series:
    return (sales_df.groupby('customer_id')['amount']
            .sum()
            .sort_values(ascending=False))
```

### 8. Run Tests Again (They Should Pass!)

```bash
pytest tests/test_day_01.py -v
```

Expected output: `PASSED ✓`

### 9. Mark Complete

```bash
python -m utils.challenge_manager complete 1
```

### 10. Move to Next Challenge

```bash
python -m utils.challenge_manager today
```

## Tips for Success

### Follow the TDD Cycle

1. **Red:** Write tests that fail
2. **Green:** Write minimal code to pass tests
3. **Refactor:** Clean up your code

### Manual Calculation is Key

- Use paper, Excel, or a calculator
- Verify your logic before coding
- This builds analytical thinking

### Test Edge Cases

Always test:
- Empty DataFrames
- Single row/customer
- Null/missing values
- Boundary conditions

### Use Pandas Efficiently

Common operations:
- `groupby()` + `sum()`, `mean()`, `count()`
- `merge()` for joins
- `sort_values()` for sorting
- `.dt` accessor for dates
- `value_counts()` for counting

### Check Your Progress

```bash
python -m utils.challenge_manager stats
```

## Project Structure

```
solutions/day_XX_solution.py    # Your implementation
tests/test_day_XX.py           # Your tests
challenges/day_XX_*.md         # Challenge description
```

## Common Commands

```bash
# Get next challenge
python -m utils.challenge_manager today

# Run specific test
pytest tests/test_day_01.py -v

# Run all tests
pytest tests/ -v

# Mark challenge complete
python -m utils.challenge_manager complete 1

# View statistics
python -m utils.challenge_manager stats
```

## Troubleshooting

### Import Error

```python
ModuleNotFoundError: No module named 'solutions'
```

**Solution:** Make sure you're in the project root directory

### Test Discovery Issues

```bash
# Make sure __init__.py files exist
ls solutions/__init__.py
ls tests/__init__.py
```

### Pandas DataFrame Comparison

Use pandas testing utilities:
```python
import pandas.testing as pdt
pdt.assert_frame_equal(result, expected)
pdt.assert_series_equal(result, expected)
```

## Next Steps

Once you complete Day 1:
- Day 2: Active Users (filtering dates)
- Day 3: Average Order Value (aggregation)
- Day 4: High-Value Customers (filtering with threshold)
- Day 5: Product Sales Count (counting and ranking)
- Day 6: Employee Department Lookup (joins)

Days 7-10 are medium difficulty with more complex logic!

## Need Help?

- Review the hints in each challenge file
- Check pandas documentation: https://pandas.pydata.org/docs/
- Remember: manual calculation comes first!

---

**Ready?** Run `python -m utils.challenge_manager today` to begin!
