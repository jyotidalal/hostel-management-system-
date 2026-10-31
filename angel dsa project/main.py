
import csv
import os
from datetime import datetime

# ==========================================
# HOSTEL MANAGEMENT SYSTEM
# Using Singly Linked List in Python
# ==========================================

DATA_FOLDER = "hostel_data"
REPORT_FOLDER = "reports"

FILES = {
    "students": {
        "file": "students.csv",
        "fields": ["student_id", "name", "course", "phone", "room_id"]
    },
    "rooms": {
        "file": "rooms.csv",
        "fields": ["room_id", "block", "capacity", "occupied"]
    },
    "staff": {
        "file": "staff.csv",
        "fields": ["staff_id", "name", "role", "phone"]
    },
    "fees": {
        "file": "fees.csv",
        "fields": ["fee_id", "student_id", "amount", "status", "date"]
    },
    "complaints": {
        "file": "complaints.csv",
        "fields": ["complaint_id", "student_id", "description", "status"]
    }
}


# ==========================================
# NODE CLASS
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ==========================================
# SINGLY LINKED LIST
# ==========================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        if current is None:
            print("No records found.")
            return

        while current:
            print(current.data)
            current = current.next

    def search(self, key, value):
        current = self.head

        while current:
            if str(current.data.get(key, "")).lower() == str(value).lower():
                return current

            current = current.next

        return None

    def delete(self, key, value):
        current = self.head
        previous = None

        while current:
            if str(current.data.get(key, "")).lower() == str(value).lower():

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                return True

            previous = current
            current = current.next

        return False

    def count(self):
        total = 0
        current = self.head

        while current:
            total += 1
            current = current.next

        return total

    def to_list(self):
        records = []
        current = self.head

        while current:
            records.append(current.data)
            current = current.next

        return records


# ==========================================
# HOSTEL MANAGEMENT CLASS
# ==========================================

class HostelManagement:

    def __init__(self):
        self.data = {
            category: LinkedList()
            for category in FILES
        }

        os.makedirs(DATA_FOLDER, exist_ok=True)
        os.makedirs(REPORT_FOLDER, exist_ok=True)

        self.initialize_files()
        self.load_all_data()

    # Create CSV files automatically
    def initialize_files(self):

        for category, details in FILES.items():

            path = os.path.join(DATA_FOLDER, details["file"])

            if not os.path.exists(path):
                with open(path, "w", newline="") as file:
                    writer = csv.DictWriter(
                        file, fieldnames=details["fields"]
                    )
                    writer.writeheader()

    # Load CSV data into linked lists
    def load_all_data(self):

        for category, details in FILES.items():

            path = os.path.join(DATA_FOLDER, details["file"])

            with open(path, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    self.data[category].insert(row)

    # Save linked list data into CSV
    def save_data(self, category):

        details = FILES[category]
        path = os.path.join(DATA_FOLDER, details["file"])

        with open(path, "w", newline="") as file:

            writer = csv.DictWriter(
                file, fieldnames=details["fields"]
            )

            writer.writeheader()
            writer.writerows(self.data[category].to_list())

    # Add a record
    def add_record(self, category, record):

        id_field = FILES[category]["fields"][0]

        if self.data[category].search(id_field, record[id_field]):
            print("This ID already exists!")
            return False

        self.data[category].insert(record)
        self.save_data(category)

        print("Record added successfully!")
        return True

    # Display records
    def display_records(self, category):

        print("\n==========", category.upper(), "RECORDS ==========")
        self.data[category].display()

    # Search records
    def search_record(self, category):

        key = FILES[category]["fields"][0]
        value = input(f"Enter {key}: ")

        result = self.data[category].search(key, value)

        if result:
            print("Record found:")
            print(result.data)
        else:
            print("Record not found.")

    # Delete records
    def delete_record(self, category):

        key = FILES[category]["fields"][0]
        value = input(f"Enter {key} to delete: ")

        if self.data[category].delete(key, value):
            self.save_data(category)
            print("Record deleted successfully!")
        else:
            print("Record not found.")

    # Update records
    def update_record(self, category):

        key = FILES[category]["fields"][0]
        value = input(f"Enter {key} to update: ")

        node = self.data[category].search(key, value)

        if node is None:
            print("Record not found.")
            return

        print("Current record:", node.data)

        print("Fields:", ", ".join(FILES[category]["fields"]))

        field = input("Enter field to update: ")

        if field not in FILES[category]["fields"] or field == key:
            print("Invalid field.")
            return

        new_value = input("Enter new value: ")
        node.data[field] = new_value

        self.save_data(category)
        print("Record updated successfully!")

    # Room allocation
    def allocate_room(self):

        student_id = input("Enter Student ID: ")
        room_id = input("Enter Room ID: ")

        student = self.data["students"].search(
            "student_id", student_id
        )

        room = self.data["rooms"].search(
            "room_id", room_id
        )

        if not student:
            print("Student not found.")
            return

        if not room:
            print("Room not found.")
            return

        if student.data["room_id"]:
            print("Student already has a room.")
            return

        try:
            capacity = int(room.data["capacity"])
            occupied = int(room.data["occupied"])
        except ValueError:
            print("Invalid room capacity data.")
            return

        if occupied >= capacity:
            print("Room is full.")
            return

        student.data["room_id"] = room_id
        room.data["occupied"] = str(occupied + 1)

        self.save_data("students")
        self.save_data("rooms")

        print("Room allocated successfully!")

    # Fee collection
    def collect_fee(self):

        fee_id = input("Enter Fee ID: ")
        student_id = input("Enter Student ID: ")
        amount = input("Enter Fee Amount: ")

        if not self.data["students"].search("student_id", student_id):
            print("Student not found.")
            return

        try:
            if float(amount) <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Enter a valid amount.")
            return

        record = {
            "fee_id": fee_id,
            "student_id": student_id,
            "amount": amount,
            "status": "Paid",
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        self.add_record("fees", record)

    # Generate reports
    def generate_reports(self):

        print("\n========== HOSTEL REPORTS ==========")

        for category in FILES:

            records = self.data[category].to_list()
            path = os.path.join(
                REPORT_FOLDER, category + "_report.csv"
            )

            with open(path, "w", newline="") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=FILES[category]["fields"]
                )

                writer.writeheader()
                writer.writerows(records)

            print(f"{category.title()}: {len(records)} records")

        print("\nAll reports generated successfully!")


# ==========================================
# INPUT HELPER
# ==========================================

def get_record(category):

    record = {}

    print("\nEnter the following details:")

    for field in FILES[category]["fields"]:
        record[field] = input(field.replace("_", " ").title() + ": ")

    return record


# ==========================================
# MAIN MENU
# ==========================================

def main():

    hostel = HostelManagement()

    while True:

        print("\n" + "=" * 48)
        print("       HOSTEL MANAGEMENT SYSTEM")
        print("       USING LINKED LIST IN PYTHON")
        print("=" * 48)

        print("""
1. Student Management
2. Room Management
3. Staff Management
4. Fee Management
5. Complaint Management
6. Room Allocation
7. Display All Records
8. Search Record
9. Update Record
10. Delete Record
11. Generate Reports
12. Exit
""")

        try:
            choice = int(input("Enter your choice: "))

            if choice in [1, 2, 3, 4, 5]:

                category = {
                    1: "students",
                    2: "rooms",
                    3: "staff",
                    4: "fees",
                    5: "complaints"
                }[choice]

                print(f"\n--- {category.upper()} MANAGEMENT ---")
                print("1. Add Record")
                print("2. Display Records")

                action = input("Enter choice: ")

                if action == "1":
                    hostel.add_record(
                        category, get_record(category)
                    )
                elif action == "2":
                    hostel.display_records(category)
                else:
                    print("Invalid choice.")

            elif choice == 6:
                hostel.allocate_room()

            elif choice == 7:
                for category in FILES:
                    hostel.display_records(category)

            elif choice == 8:
                print("Select category:", ", ".join(FILES))
                category = input("Enter category: ").lower()

                if category in FILES:
                    hostel.search_record(category)
                else:
                    print("Invalid category.")

            elif choice == 9:
                print("Select category:", ", ".join(FILES))
                category = input("Enter category: ").lower()

                if category in FILES:
                    hostel.update_record(category)
                else:
                    print("Invalid category.")

            elif choice == 10:
                print("Select category:", ", ".join(FILES))
                category = input("Enter category: ").lower()

                if category in FILES:
                    hostel.delete_record(category)
                else:
                    print("Invalid category.")

            elif choice == 11:
                hostel.generate_reports()

            elif choice == 12:
                print("Thank you for using Hostel Management System!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Please enter a valid number.")

        except Exception as error:
            print("An error occurred:", error)


# ==========================================
# PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":
    main()
