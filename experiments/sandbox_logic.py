import pandas as pd

# --- 1. SETUP ---
def load_test_data():
    """Load the dataset for experimentation."""
    return pd.read_csv("data/raw/sales_1.csv")

# --- 2. UTILITY FUNCTIONS ---
def add_contribution(series):
    """Calculates percentage contribution of a series."""
    total_sale = series.sum()
    return ((series / total_sale) * 100).round(2)

# --- 3. FEATURE PROOFS (The 'Lab' area) ---

def proof_cleaning(dataset):
    # print("\n--- Testing Data Cleaning ---")
    critical_cols = ['Order_ID', 'Date', 'Product', 'Category', 'Region', 'Customer_Name']
    
    # Apply cleaning logic
    dataset['Date'] = pd.to_datetime(dataset['Date'], errors='coerce')
    dataset['Price'] = pd.to_numeric(dataset['Price'], errors='coerce')
    dataset.dropna(subset=critical_cols, inplace=True)
    
    # print("Cleaning Complete. Info:")
    # print(dataset.info())
    return dataset

def proof_top_products(dataset):
    print("\n--- Testing Top Products ---")
    products_set = dataset.groupby("Product")["Revenue"].sum().sort_values(ascending=False).reset_index()
    products_set['Contribution(%)'] = add_contribution(products_set["Revenue"])
    products_set.index += 1
    
    print(products_set.head(5))

def avg_oder_val(Total_spent,Order_count):
    try:
        return Total_spent/Order_count
    except ZeroDivisionError:
        return 0.0

def proof_customer_analysis(dataset):
    print("\n--- Testing Customer Analysis (Option 9) ---")
    
    # Strategy: Combine Spend and Frequency into one clear table
    customer_stats = dataset.groupby("Customer_Name").agg(
        Total_Spend=('Revenue', 'sum'),
        Order_Count=('Order_ID', 'count'),
        Order_count= ('Order_ID','count')
    ).sort_values(by='Total_Spend', ascending=False).reset_index()
    
    customer_stats.index += 1

    customer_stats["Average_order_value"] = avg_oder_val(customer_stats['Total_Spend'],customer_stats['Order_count'])
    
    print("Top 5 Customers by Spend:")
    print(customer_stats.head(5))
    
    ans = input("\nView top 5 by Frequency? [y/n]: ").lower().strip()
    if ans == 'y':
        print(customer_stats.sort_values(by='Order_Count', ascending=False).head(5))

def test_agg_func(dataset):
    # Pass a list of strings
    stats = dataset.groupby('Category')['Price'].agg(['min', 'max', 'mean'])
    print(stats)

    summary = dataset.groupby('Region').agg({
    'Revenue': 'sum',      # Total money per region
    'Order_ID': 'count',   # Number of transactions
    'Quantity': 'mean'  })   # Average items per sale
    print("\n\n",summary)
    
    # Named Aggregation: New_Column_Name = (Original_Column, Function)
    customer_report = dataset.groupby('Customer_Name').agg(
    Total_Spent = ('Revenue', 'sum'),
    Visit_Frequency = ('Order_ID', 'count'),
    Avg_Items_Per_Order = ('Quantity', 'mean'))
    print(customer_report)



def get_monthly_summary(dataset):
    # Removing rows where Date is missing because we can't assign them to a month
    monthly_summary = dataset.dropna(subset=['Date'])

    # Extracting Month number and Name from the Date column
    monthly_summary['Month'] = monthly_summary['Date'].dt.month
    monthly_summary['Month_name'] = monthly_summary['Date'].dt.month_name()

    return monthly_summary

def best_sales_period(dataset):
    
    monthly_summary =  get_monthly_summary(dataset)
    
    best_period = monthly_summary.groupby(["Month_name"])['Revenue'].sum().sort_values(ascending=False)

    # best_period['Contribution'] = add_contribution(best_period['Revenue'])

    # print(f"Best sales period is {best_period.iloc[0]["Month_name"]} by having ₹{best_period.iloc[0]['Revenue']} as revenue with contribution of {best_period.iloc[0]['Contribution']}% in annual revenue.")

    best_month = best_period.idxmax()
    worst_month = best_period.idxmin()
    max_revenue = best_period.max()
    min_revenue = best_period.min()
    total_revenue = best_period.sum()
    contribution = (max_revenue/total_revenue)*100

    print(f"Best sales period is {best_month} by having ₹{max_revenue:,.2f} as revenue with contribution of {contribution:.2f}% in annual revenue.")
    print(f"The most challenging period was {worst_month} with only ₹{min_revenue:.2f} in sales.")

import os

def export_data(dataset):
    # 1. Get the directory where analysis.py is located
    current_dir = os.path.dirname(__file__) 
    
    # 2. Go one level up to reach the root project folder
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    
    # # 3. Define the target folder outside the source folder
    export_folder = os.path.join(parent_dir, "data/processed")

    # # 4. Create the folder if it doesn't exist
    if not os.path.exists(export_folder):
        os.makedirs(export_folder)
        print(f"Created external directory: {export_folder}")

    filename = input("Enter filename to save: ").strip()
    if not filename.lower().endswith(".csv"):
        filename += ".csv"

    # 5. Full path for saving
    save_path = os.path.join(export_folder, filename)

    try:
        dataset.to_csv(save_path, index=False)
        print(f"File successfully saved at: {save_path}")
    except Exception as e:
        print(f"Error: {e}")

    return dataset

def check_revenue(dataset):
    dataset = dataset[dataset['Revenue']==(dataset['Quantity']*dataset
    ['Price'])]
    print(dataset)

# --- 4. EXECUTION CONTROL ---
if __name__ == "__main__":
    # Load data once
    df = load_test_data()
    
    # STEP 1: Always clean before analyzing
    df = proof_cleaning(df)
    
# STEP 2: Uncomment the specific feature you want to test right now
# proof_top_products(df)
# proof_customer_analysis(df)
# test_agg_func(df)
# get_monthly_summary(df)
# best_sales_period(df)
# export_data(df)
check_revenue(df)
