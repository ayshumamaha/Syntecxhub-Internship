# Expense Tracker CLI

## Overview

Expense Tracker CLI is a simple Python command-line application that helps users record and manage their daily income and expenses. The application stores transaction data in a CSV file, provides monthly and category-wise summaries, exports reports to CSV and Excel formats, and generates a pie chart to visualize expense distribution.

This project demonstrates Python file handling, data analysis using Pandas, data visualization with Matplotlib, and command-line interface (CLI) development.

---

## Features

* Add income transactions
* Add expense transactions
* Store transaction data in a CSV file
* View all recorded transactions
* Generate monthly income and expense summaries
* Display category-wise expense reports
* Export transaction data to CSV
* Export transaction data to Excel
* Generate and save an expense distribution pie chart
* Simple and user-friendly command-line interface

---

## Technologies Used

* Python 3
* Pandas
* Matplotlib
* OpenPyXL

---

## Project Structure

```
Expense_Tracker_CLI/
│
├── expense_tracker.py
├── expenses.csv
├── expense_report.csv
├── expense_report.xlsx
├── expense_chart.png
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Expense_Tracker_CLI.git
```

Move into the project directory:

```bash
cd Expense_Tracker_CLI
```

Install the required libraries:

```bash
pip install pandas matplotlib openpyxl
```

---

## Running the Project

Execute the Python file:

```bash
python expense_tracker.py
```

The application will display a menu with the available options.

---

## Menu Options

```
1. Add Income
2. Add Expense
3. View Transactions
4. Monthly Summary
5. Category Summary
6. Export CSV
7. Export Excel
8. Generate Expense Chart
9. Exit
```

---

## Sample Transaction

| Date       | Type    | Category  | Amount |
| ---------- | ------- | --------- | -----: |
| 2026-07-01 | Income  | Salary    |  50000 |
| 2026-07-02 | Expense | Food      |    350 |
| 2026-07-03 | Expense | Transport |    120 |

---

## Generated Output Files

* **expenses.csv** – Stores all transaction records.
* **expense_report.csv** – Exported CSV report.
* **expense_report.xlsx** – Excel report.
* **expense_chart.png** – Pie chart showing expense distribution by category.

---

## Skills Demonstrated

* Python Programming
* Command-Line Interface (CLI)
* File Handling
* CSV Processing
* Data Analysis with Pandas
* Data Visualization with Matplotlib
* Excel File Generation
* Data Aggregation and Reporting

---

## Future Improvements

* User authentication
* SQLite database support
* Budget planning and alerts
* Search and filter transactions
* Delete or edit existing transactions
* Interactive charts and dashboard
* Graphical User Interface (GUI)

---

## License

This project is developed for educational and learning purposes.

Author
M. Ayshwarya
