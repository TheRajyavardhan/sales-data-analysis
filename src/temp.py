import pandas as pd 
dataset = pd.read_csv("data/raw/sales.csv")
# critical_cols = ['Order_ID','Date','Product','Category','Region'] # these columns must not have nan values
# numeric_cols = ['Price','Quantity','Revenue'] # Can replace nan values with numeric values
# df.dropna(inplace=True)
# df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
# print(df[df.isna().any(axis=1)])
# df.dropna(subset=critical_cols,inplace=True) 

# print(df.groupby("Product")["Price"].mean())
# df['Date'] = pd.to_datetime(df['Date'],format="%Y-%m-%d",errors='coerce')
# df.info()
# df['Month'] = df['Date'].dt.month
# df['Month_name'] = df['Date'].dt.month_name()
# saleBy_Month = df.groupby(["Month","Month_name"])['Revenue'].sum()
# # saleBy_Month.sort_values(inplace=True)
# # print(df.groupby(["Month","Region"])['Revenue'].sum())
# print(saleBy_Month)
# print(df)
# products_set = df.groupby(["Product"])["Revenue"].sum().sort_values(ascending=False).reset_index()
# products_set.index = products_set.index + 1
# print(products_set)
# print(products_set.index.max())
# category_sales = dataset.groupby("Category",as_index=False)["Revenue"].sum().sort_values(by='Revenue',ascending=False)
# category_sales.index += 1
# print("Sales by category:\n\n",category_sales.to_string())
# print(f"\nTop performing category: {category_sales.loc[1,"Category"]}")
# print(category_sales.iloc[1]["Category"])
# print(category_sales)
# def add_contribution(series):
#     total_sale = series.sum()
#     return ((series/total_sale)*100).round(2)

products_set = dataset.groupby(["Product"],as_index=False)["Revenue"].sum().sort_values(by="Revenue",ascending=False)
print(products_set)

# products_set['Contribution(%)'] = add_contribution(products_set["Revenue"])
# products_set.index += 1
# top_val = 10  
# if products_set.index.max()<10: 
#     top_val = products_set.index.max()

# print("Top 5 products:\n",products_set.head(5))

# print(f"Top {top_val} products:\n",products_set.head(top_val))