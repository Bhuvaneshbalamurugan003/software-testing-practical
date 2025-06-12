# Step 1: Create a dictionary to store defects
defect_database = {}
defect_id_counter = 1  # Auto-incrementing defect ID

# Step 2: Function to add a new defect
def add_defect(title, description, severity):
    global defect_id_counter
    defect_database[defect_id_counter] = {
        "Title": title,
        "Description": description,
        "Severity": severity,
        "Status": "Open"
    }
    print(f"\nDefect {defect_id_counter} added successfully!")
    defect_id_counter += 1

# Step 3: Function to view all defects empty
def view_defects():
    if not defect_database:
        print("\nNo defects recorded yet.")
    else:
        print("\n--- Current Defect List ---")
        for defect_id, details in defect_database.items():
            print(f"ID: {defect_id} | Title: {details['Title']} | Severity: {details['Severity']} | Status: {details['Status']}")

# Step 4: Function to update a defect's status
def close_defect(defect_id):
    if defect_id in defect_database:
        if defect_database[defect_id]["Status"] == "Closed":
            print(f"\nDefect {defect_id} is already closed.")
        else:
            defect_database[defect_id]["Status"] = "Closed"
            print(f"\nDefect {defect_id} has been closed.")
    else:
        print("\nInvalid Defect ID!")

# Step 5: Function to generate a defect report
def generate_report():
    total = len(defect_database)
    open_defects = sum(1 for defect in defect_database.values() if defect["Status"] == "Open")
    closed_defects = total - open_defects

    print("\n--- Defect Report ---")
    print(f"Total Defects : {total}")
    print(f"Open Defects  : {open_defects}")
    print(f"Closed Defects: {closed_defects}")

# Step 6: Main menu-driven interface
def main():
    while True:
        print("\n--- Defect Tracking System ---")
        print("1. Add Defect")
        print("2. View Defects")
        print("3. Close Defect")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
       #accepts user inpiut
       #keeps look untill user select exit

        if choice == '1':
            title = input("Enter defect title: ")
            description = input("Enter defect description: ")
            severity = input("Enter severity (Low/Medium/High): ")
            add_defect(title, description, severity)
        elif choice == '2':
            view_defects()
        elif choice == '3':
            try:
                defect_id = int(input("Enter Defect ID to close: "))
                close_defect(defect_id)
            except ValueError:
                print("\nInvalid input! Please enter a numeric Defect ID.")
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("\nExiting Defect Tracking System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select between 1 to 5.")


if __name__ == "__main__":
    main()
