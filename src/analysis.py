import pandas as pd

def display_data(dataset):
    print("\n" + "="*50)
    print("SAMPLE DATA (First 5 Rows)")
    print("="*50)
    print(dataset.head(5))
    
    print("\n" + "="*50)
    print("DATASET INFORMATION")
    print("="*50)
    print(f"Total Rows: {dataset.shape[0]}")
    print(f"Total Columns: {dataset.shape[1]}")
    print(f"\nColumn Names: {dataset.columns.tolist()}")
    
    print("\n" + "="*50)
    print("DATA TYPES & MISSING VALUES")
    print("="*50)
    dataset.info()
    print("="*50 + "\n")


