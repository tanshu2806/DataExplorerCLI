from explorer import DataExplorer

explorer = DataExplorer()

def get_row_count():
    while True:
        try:
            value = input("How many rows? (Press Enter for default)").strip()
            if value =="":
                return 5
            rows = int(value)
            
            if rows <= 0:
                print("Please enter a number greater than 0.")
                continue
            else:
                return rows
        except ValueError:
            print("Please enter a valid number.")
            
        

while True:
    print('''========== DATA EXPLORER CLI ==========

    1. Load CSV
    2. Dataset Information
    3. Show Dataset Shape
    4. Show Column Names
    5. Show Data Types
    6. Show Top Rows
    7. Show Bottom Rows
    8. Missing Values
    9. Statistical Summary
    10. Correlation Matrix
    11. Remove Missing Values
    12. Export Cleaned CSV

    0. Exit


    Enter choice:''')
    try:
        choice = int(input("Enter the choice: "))
    except ValueError:
        print("Please enter a valid number.")

    match choice:
        case 1:
            # Load CSV
            path = input("Enter file path: ")
            explorer.load_csv(path)

        case 2:
            # Dataset Information
            explorer.dataset_info()

        case 3:
            # Dataset Shape
            explorer.show_shape()

        case 4:
            # Column Names
            explorer.show_columns()

        case 5:
            # Data Types
            explorer.show_dtypes()

        case 6:
            # Top rows
            rows = get_row_count()
            explorer.head(rows)

        case 7:
            # Bottom Rows
            rows = get_row_count()
            explorer.tail(rows)

        case 8:
            # Missing Values
            explorer.missing_values()

        case 9:
            # Statistical Summary
            explorer.statistics()

        case 10:
            # Correlation Matrix
            explorer.correlation_matrix()

        case 11:
            # Remove Missing Values
            explorer.remove_missing_values()

        case 12:
            # Export CSV
            name = input("Enter filename: ")
            if not name.endswith(".csv"):
                name = name + ".csv"
            explorer.export_csv(name)

        case _:
            print("Invalid Choice")
