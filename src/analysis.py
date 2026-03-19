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
    
    print("\n" + "="*50)
    print("DATA TYPES & MISSING VALUES")
    print("="*50)
    dataset.info()
    print("="*50 + "\n")


def clean_data(dataset):
    dataset['Date'] = pd.to_datetime(dataset['Date'],format="%Y-%m-%d",errors='coerce')
    dataset['Price'] = pd.to_numeric(dataset['Price'], errors='coerce')
    dataset.drop_duplicates(inplace=True)
    dataset.dropna()
    dataset=dataset[dataset['Quantity']>0]
    print(dataset)
    return dataset

def total_sales(dataset):
    print("Total Sales:",dataset['Revenue'].sum())
    return dataset

def add_contribution(series):
    total_sale = series.sum()
    return ((series/total_sale)*100).round(2)

def sales_by_month(dataset):
    dataset = dataset.dropna(subset=['Date'])

    dataset['Month'] = dataset['Date'].dt.month
    dataset['Month Name'] = dataset['Date'].dt.month_name()

    salesBy_Month = dataset.groupby(["Month","Month Name"])["Revenue"].sum().sort_index()
    salesBy_Month = salesBy_Month.reset_index()

    print("Sales by Month:\n",salesBy_Month.to_string(index=False))

    return dataset

def top_products(dataset):
    products_set = dataset.groupby(["Product"])["Revenue"].sum().sort_values(ascending=False).reset_index()

    products_set['Contribution(%)'] = add_contribution(products_set["Revenue"])
    products_set.index += 1
    top_val = 10  
    if products_set.index.max()<10: 
        top_val = products_set.index.max()

    print("Top 5 products:\n",products_set.head(5))

    ans = input(f"Do you want to look into top {top_val} products?(Yes = Enter, No = n)... ").lower().strip()

    if ans == 'n':
        return dataset
    print(f"Top {top_val} products:\n",products_set.head(top_val))

    return dataset

def sales_by_cate(dataset):
    category_sales = dataset.groupby("Category")["Revenue"].sum().sort_values(ascending=False).reset_index()

    category_sales["Contribution(%)"] = add_contribution(category_sales["Revenue"])
    category_sales.index += 1

    print("\nSales by category:\n",category_sales.to_string())
    print(f"\nTop performing category: {category_sales.iloc[0]["Category"]}")
    print(f"Lowest performing category: {category_sales.iloc[-1]["Category"]}")
    return dataset

def sales_by_region(dataset):
    region_sales = dataset.groupby("Region")["Revenue"].sum().sort_values(ascending=False).reset_index()
    
    region_sales["Contribution(%)"] = add_contribution(region_sales["Revenue"])
    region_sales.index += 1

    print("\nSales by region:\n",region_sales.to_string())
    print(f"\nTop performing region: {region_sales.iloc[0]["Region"]}")
    print(f"Lowest performing region: {region_sales.iloc[-1]["Region"]}")
