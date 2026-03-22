import pandas as pd

def load_data(file_path="data/raw/sales_1.csv"):
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print("No records found.")
            return None
        
        required_cols = ['Date', 'Quantity', 'Price', 'Revenue']
        missing = set(required_cols)-set(df.columns)
        if missing:
            print(f"Missing columns: {missing}")
            return None
        
        print("File is successfully loaded.")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")
        return df
    
    except FileNotFoundError:
        print("File not found.")
        return None

    except pd.errors.EmptyDataError:
        print("File is empty.")
        return None