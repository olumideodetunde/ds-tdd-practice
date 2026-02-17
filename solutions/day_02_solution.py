import pandas as pd

def get_active_users(purchase_df: pd.DataFrame):
    filtered_df = (purchase_df
                   .copy()
                   .query('"2024-01-01" < purchase_date < "2024-01-31"')['user_id']
                   .unique()
                   .tolist()
                   )
    return filtered_df