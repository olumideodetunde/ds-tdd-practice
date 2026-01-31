# Data Science TDD Practice - 50 Day Challenge

Daily analytical challenges with Test-Driven Development to master pandas and SQL thinking.

## Progress: 0/50 Challenges Complete

## What is This?

This is a structured learning system where you:
1. Get a daily analytical question (similar to SQL interviews)
2. Manually calculate the answer from small sample data
3. Write your solution in pandas/Python
4. Write tests to verify your solution
5. Run pytest until all tests pass

## Setup

```bash
# Install dependencies with uv
uv sync

# Activate the virtual environment
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
```

## Daily Workflow

```bash
# 1. Get today's challenge
python -m utils.challenge_manager today

# 2. Read the challenge markdown file
# challenges/day_XX_*.md

# 3. Manually calculate the answer with the sample data provided

# 4. Write your solution
# solutions/day_XX_solution.py

# 5. Write tests
# tests/test_day_XX.py

# 6. Run tests
pytest tests/test_day_XX.py -v

# 7. When all tests pass, mark complete
python -m utils.challenge_manager complete XX
```

## Difficulty Progression

- **Days 1-17:** Easy (GroupBy, Filtering, Basic Joins)
- **Days 18-34:** Medium (Window Functions, Multiple Joins, Subqueries)
- **Days 35-50:** Hard (Complex Analytics, Performance, Edge Cases)

## Project Structure

```
ds-tdd-practice/
├── challenges/          # Challenge markdown files
├── solutions/           # Your solution code (you write these)
├── tests/              # Your test files (you write these)
├── utils/              # Helper scripts
├── progress.json       # Tracks your progress
├── pyproject.toml      # Project configuration
├── uv.lock            # Locked dependencies
└── README.md
```

## Tips for Success

1. **Manual Calculation First:** Always work out the answer by hand before coding
2. **Small Sample Data:** The challenges provide 5-10 rows - easy to verify
3. **Write Tests First:** Follow TDD - tests before implementation
4. **Edge Cases:** Test empty data, nulls, single rows
5. **One Challenge Per Day:** Build the habit, don't rush

## Why This Works

- **Pandas mastery** - Practice the operations used 80% of the time
- **SQL thinking** - Translatable to any database work
- **Testing discipline** - Rare skill among data scientists
- **Interview prep** - 50 solved analytical problems
- **Confidence** - You know your code works

## Stats

Run `python -m utils.challenge_manager stats` to see:
- Current streak
- Completion rate
- Difficulty breakdown
- Time invested

## Getting Help

If you get stuck:
1. Review the hints in the challenge file
2. Check pandas documentation
3. Look at the function signature
4. Remember: manual calculation comes first!

---

**Start your first challenge:** `python -m utils.challenge_manager today`
