from explorer import DataExplorer

explorer = DataExplorer()

while True:
    print('''========== DATA EXPLORER ==========

    1. Load CSV
    2. Dataset Info
    3. Top Rows
    4. Bottom Rows
    5. Exit

    Enter choice:''')

    choice = int(input("Enter the choice: "))

    match choice:
        case 1:
            path = input("Enter file path: ")
            explorer.load_csv(path)
        case 2:
            explorer.dataset_info()
        case 3:
            explorer.head()
        case 4:
            explorer.tail()
        case 5:
            break
        case _:
            print("Invalid Choice")