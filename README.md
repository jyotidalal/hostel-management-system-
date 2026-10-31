# hostel-management-system-
# 🏨 Hostel Management System
### Using Singly Linked List in Python

## 📌 Project Overview

The **Hostel Management System** is a Python-based application developed to simplify hostel administration and record management.

The project uses a **Singly Linked List** as its primary data structure to manage student, room, staff, fee, and complaint records. It also uses CSV files for storing data permanently.

The system provides basic operations such as insertion, searching, updating, deletion, room allocation, and report generation.

## 🎯 Project Objectives

- To computerize hostel management activities.
- To implement Linked List concepts using Python.
- To reduce manual record-keeping and errors.
- To provide efficient searching and record management.
- To maintain hostel information using CSV file handling.
- To generate reports for different hostel management modules.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Singly Linked List | Data Structure |
| CSV | Data Storage |
| OOP | Object-Oriented Programming |
| VS Code | Development Environment |

## ✨ Features

### 1. Student Management
- Add student records.
- Display student information.
- Search student records.
- Update student details.
- Delete student records.

### 2. Room Management
- Add room details.
- Store room capacity.
- Track room occupancy.
- Allocate rooms to students.
- Check room availability.

### 3. Staff Management
- Add staff information.
- Store staff names, roles, and contact details.
- Display and manage staff records.

### 4. Fee Management
- Record student fee payments.
- Store fee amount and payment date.
- Maintain payment status.

### 5. Complaint Management
- Register student complaints.
- Store complaint descriptions and status.
- Maintain complaint records.

### 6. Searching and Updating
- Search records using unique IDs.
- Update existing information.
- Delete unwanted records.

### 7. Report Generation
- Generate CSV reports for:
  - Student Records
  - Room Records
  - Staff Records
  - Fee Records
  - Complaint Records

## 🧠 Data Structures Implemented

### Singly Linked List

A Singly Linked List is a linear data structure consisting of nodes. Each node contains:

- **Data:** Stores the record information.
- **Next:** Stores the reference to the next node.

The project implements the following linked list operations:

- Insertion
- Traversal
- Searching
- Deletion
- Counting records

### Node Structure

Each node stores a dictionary containing the record details and a reference to the next node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## 📂 Project Structure

```text
HostelManagementSystem/
│
├── hostel_management.py
│
├── hostel_data/
│   ├── students.csv
│   ├── rooms.csv
│   ├── staff.csv
│   ├── fees.csv
│   └── complaints.csv
│
└── reports/
    ├── students_report.csv
    ├── rooms_report.csv
    ├── staff_report.csv
    ├── fees_report.csv
    └── complaints_report.csv
```

**Note:** The `hostel_data` and `reports` folders and their CSV files are automatically created by the program when required.

## ⚙️ Installation and Execution

### Prerequisites

- Python 3.8 or above
- Visual Studio Code
- Python extension for VS Code (recommended)

### Steps to Run

**Step 1:** Clone the repository.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2:** Open the project folder in VS Code.

**Step 3:** Open the terminal.

**Step 4:** Run the Python program.

```bash
python hostel_management.py
```

No external Python libraries are required.

## 📋 Main Menu

The application provides the following menu:

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

## 📊 Time Complexity Analysis

| Operation | Time Complexity |
|---|---|
| Insertion at End | O(n) |
| Searching | O(n) |
| Deletion | O(n) |
| Traversal | O(n) |
| Counting | O(n) |

Here, **n** represents the total number of nodes in the linked list.

## 💾 Data Storage

The project uses CSV (Comma-Separated Values) files to store records.

The program loads existing CSV records into linked lists when it starts and saves changes back to the respective CSV files.

This allows records to remain available even after the application is
