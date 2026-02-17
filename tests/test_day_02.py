import pandas as pd
from solutions.day_02_solution import get_active_users

def test_active_users_obtained():
    data = pd.DataFrame ({
        "user_id": [1, 2, 1, 3, 2],
        "purchase_date": ["2024-01-15", "2023-12-20", "2024-01-20", "2024-01-05", "2024-02-10"],
        "amount": [50.0, 30.0, 25.0, 100.0, 75.0]})
    result = get_active_users(data)
    assert result[0] == 1
    assert result[1] == 3

def test_active_users_not_obtained():
    data = pd.DataFrame ({})
    result = get_active_users(data)
    assert result[0] == 0
    assert result[1] == 0
