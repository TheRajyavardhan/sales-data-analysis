import load_data as ld
import analysis as an

# -------------------------------
# Safe input functions
# -------------------------------

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")  

# -------------------------------
# Menu wrapper functions
# -------------------------------

def get_data():
    file_path = input("Enter the file path to load data: ")
    print("Loading data...")
    if file_path:
        return ld.load_data(file_path)
    else:
        return ld.load_data()

def get_clean(dataset):
    print("Cleaning the data...")
    print("Converting the datatype of columns...")
    print("Drop duplicate rows...")
    print("Drop rows containing nan values...")
    print("Removing wrong values rows...")
    return an.clean_data(dataset)

# -------------------------------
# Menu dictionary
# -------------------------------

menu = {
    1:get_data,
    2:an.display_data,
    3:get_clean,
    4:an.total_sales,
    5:an.sales_by_month,
    6:an.top_products,
    7:an.sales_by_cate,
    8:an.sales_by_region,
    9:"Customer Analysis",
    10:"Best Sales Period",
    11:"Average Order Value",
    12:"Export Result",
    13:"Exit"
}

# -------------------------------
# Main program
# -------------------------------

def main():
    df = None

    while True:
        print("="*30)
        print("Sales Data Analysis Menu")
        print("="*30)
        print("1. Load Data\n" \
        "2. View Data\n" \
        "3. Clean Data\n" \
        "4. Total Sales\n" \
        "5. Sales by Month\n" \
        "6. Top Products\n" \
        "7. Sales by Category\n" \
        "8. Region-wise Sales\n" \
        "9. Customer Analysis\n" \
        "10. Best Sales Period\n" \
        "11. Average Order Value\n" \
        "12. Export Result\n" \
        "13. Exit")
        print("="*30)
        choice = get_int("Enter your choice: ")

        if choice == 1: 
            df = get_data()
        elif choice == 13:
            print("Exiting the program. Goodbye!")
            break
        
        else:
            action = menu.get(choice)
            if action:
                if df is None:
                    print("Load data first.")
                    continue
                dataset = action(df)
            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()