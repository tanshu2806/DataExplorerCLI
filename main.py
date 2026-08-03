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
            explorer
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            exit
        case _:
            print("Invalid Choice")