import pandas as pd

def calculate_total_sales(sales_df: pd.DataFrame) -> pd.Series:
    total = (sales_df
             .groupby('customer_id')['amount']
             .sum()
             .sort_values(ascending=False)
             )
    return total
