import pandas as pd
import os 
currency = '₹'

# Function to give a quick overview of the dataset
def display_data(dataset):
    print("\n" + "="*50)
    print("SAMPLE DATA (First 5 Rows)")
    print("="*50)
    print(dataset.head(5)) # Shows the top 5 records to understand column structure
    
    print("\n" + "="*50)
    print("DATASET INFORMATION")
    print("="*50)
    print(f"Total Rows: {dataset.shape[0]}")
    print(f"Total Columns: {dataset.shape[1]}")
    
    print("\n" + "="*50)
    print("DATA TYPES & MISSING VALUES")
    print("="*50)
    # .info() is essential to check if 'Date' or 'Price' are objects (strings) or numbers
    dataset.info()
    print("="*50 + "\n")

    return dataset


# Function to fix data types and remove bad data
def clean_data(dataset):
    # Converting Date column to actual datetime objects for time-based analysis
    dataset['Date'] = pd.to_datetime(dataset['Date'], format="%Y-%m-%d", errors='coerce')
    
    # Ensuring Price is numeric; 'coerce' turns non-numeric junk into NaN
    dataset['Price'] = pd.to_numeric(dataset['Price'], errors='coerce')
    
    # Removing exact duplicate entries to avoid double-counting sales
    dataset.drop_duplicates(inplace=True)
    
    # Removing any rows that have empty (NaN) values
    dataset.dropna(inplace=True)
    
    # Filtering out negative or zero quantities which might be data entry errors
    dataset = dataset[dataset['Quantity'] > 0]

    dataset = dataset[dataset['Revenue']==(dataset['Quantity']*dataset['Price'])]
    
    print(dataset)
    return dataset

# Calculating the grand total revenue
def total_sales(dataset):
    print(f"Total Sales: {currency} {dataset['Revenue'].sum()}")
    return dataset


# Helper function to calculate the percentage share of a specific group
def add_contribution(series):
    total_sale = series.sum()
    # Logic: (Current Item Total / Grand Total) * 100
    return ((series / total_sale) * 100).round(2)


def get_monthly_summary(dataset):
    # Removing rows where Date is missing because we can't assign them to a month
    monthly_summary = dataset.dropna(subset=['Date'])

    # Extracting Month number and Name from the Date column
    monthly_summary['Month'] = monthly_summary['Date'].dt.month
    monthly_summary['Month_name'] = monthly_summary['Date'].dt.month_name()

    return monthly_summary 

# Analyzing sales trends across different months
def sales_by_month(dataset):
    
    monthly_summary = get_monthly_summary(dataset)

    # Grouping by both to keep them together, then summing revenue
    salesBy_Month = monthly_summary.groupby(["Month", "Month_name"])["Revenue"].sum().sort_index()
    salesBy_Month = salesBy_Month.reset_index()

    print("Sales by Month:\n", salesBy_Month.to_string(index=False))

    return dataset



# Finding which products are generating the most money
def top_products(dataset):
    # Grouping by Product and sorting from highest revenue to lowest
    products_set = dataset.groupby(["Product"])["Revenue"].sum().sort_values(ascending=False).reset_index()


    # Using our helper function to see how much % each product contributes
    products_set['Contribution(%)'] = add_contribution(products_set["Revenue"])
    products_set.index += 1 # Shifting index to start from 1 instead of 0
    
    top_val = 10  
    if products_set.index.max() < 10: 
        top_val = products_set.index.max()

    print("Top 5 products:\n", products_set.head(5))

    # Giving the user an option to see a longer list (Top 10)
    ans = input(f"Do you want to look into top {top_val} products?(Yes = Enter, No = n)... ").lower().strip()

    if ans == 'n':
        return dataset
    print(f"Top {top_val} products:\n", products_set.head(top_val))

    return dataset

# Analyzing which category (Electronics, Clothing, etc.) is performing best
def sales_by_cate(dataset):
    category_sales = dataset.groupby("Category")["Revenue"].sum().sort_values(ascending=False).reset_index()

    category_sales["Contribution(%)"] = add_contribution(category_sales["Revenue"])
    category_sales.index += 1

    print("\nSales by category:\n", category_sales.to_string())
    # iloc[0] gives the first row (Top) and iloc[-1] gives the last row (Lowest)
    print(f"\nTop performing category: {category_sales.iloc[0]['Category']}")
    print(f"Lowest performing category: {category_sales.iloc[-1]['Category']}")
    return dataset

# Analyzing sales distribution across geographical regions
def sales_by_region(dataset):
    region_sales = dataset.groupby("Region")["Revenue"].sum().sort_values(ascending=False).reset_index()
    
    region_sales["Contribution(%)"] = add_contribution(region_sales["Revenue"])
    region_sales.index += 1

    print("\nSales by region:\n", region_sales.to_string())
    print(f"\nTop performing region: {region_sales.iloc[0]['Region']}")
    print(f"Lowest performing region: {region_sales.iloc[-1]['Region']}")
    
    return dataset


def avg_order_val(Total_spent,Item_frequecy):
    try:
        return (Total_spent/Item_frequecy).round(2)
    except ZeroDivisionError:
        return 0.0
    

def customer_analysis(dataset):
    customer_stats = dataset.groupby("Customer_Name").agg(
    Total_spent=('Revenue', 'sum'),
    Visit_frequency=('Order_ID', 'nunique'), # How many times they shopped
    Item_frequency=('Order_ID', 'count')     # How many items they bought total
    ).sort_values(by='Total_spent',ascending=False).reset_index()
     
    customer_stats.index += 1

    customer_stats["Average_order_value"] = avg_order_val(customer_stats['Total_spent'],customer_stats['Item_frequency'])
    
    # Show Top 5 by Spend by default (Sorted)
    print("\n" + "="*30)
    print("TOP 5 CUSTOMERS BY SPEND")
    print("="*30)
    print(customer_stats.sort_values(by='Total_spent', ascending=False).head(5))
    
    # Sub-menu for frequency views
    print("\nView more insights:")
    print("V: Top 5 by Visit Frequency (Loyalty)")
    print("I: Top 5 by Item Frequency (Volume)")
    print("N: Back to Main Menu")
    
    choice = input("Enter your choice (V/I/N): ").strip().upper()
    
    if choice == 'V':
        print("\n--- TOP 5 BY VISIT FREQUENCY ---")
        print(customer_stats.sort_values(by='Visit_frequency', ascending=False).head(5))
    elif choice == 'I':
        print("\n--- TOP 5 BY ITEM FREQUENCY ---")
        print(customer_stats.sort_values(by='Item_frequency', ascending=False).head(5))
    
    return dataset

def best_sales_period(dataset):
    
    monthly_summary =  get_monthly_summary(dataset)
    
    best_period = monthly_summary.groupby(["Month_name"])['Revenue'].sum().sort_values(ascending=False)

    best_month = best_period.idxmax()
    worst_month = best_period.idxmin()
    max_revenue = best_period.max()
    min_revenue = best_period.min()
    total_revenue = best_period.sum()
    contribution = (max_revenue/total_revenue)*100

    print(f"Best sales period is {best_month} by having ₹{max_revenue:,.2f} as revenue with contribution of {contribution:.2f}% in annual revenue.")
    print(f"The most challenging period was {worst_month} with only ₹{min_revenue:.2f} in sales.")
    
    return dataset

def export_result(dataset):

    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current_dir,".."))
    export_dir = os.path.join(parent_dir,"data\processed")
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
        print(f"Created external directory: {export_dir}")
    
    filename = input("Enter the filename: ").lower().strip()

    if not filename.endswith(".csv"):
        filename += ".csv"
    
    save_path = os.path.join(export_dir,filename)

    try:
        dataset.to_csv(save_path,index=False)
        print(f"File successfully saved at: {save_path}")

    except Exception as e:
        print(f"Error: {e}")
    
    return dataset
