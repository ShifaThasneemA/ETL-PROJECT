# 🧠 HR Data Visualization Tool

## 📋 Project Overview
This project is a **Python-based Data Visualization Tool** that connects to a **MySQL database**, retrieves data from a chosen table, and allows users to visualize it using **Matplotlib**.  
It helps analyze HR or business data interactively through different types of charts.

---

## ⚙️ Features
- ✅ Connects automatically to MySQL database (`hr`)
- ✅ Displays all data from selected table
- ✅ Lists all column names for quick selection
- ✅ Generates multiple chart types:
  - 📊 **Bar Graph**
  - 📈 **Line Graph**
  - 🥧 **Pie Chart**
  - 📉 **Histogram**
  - ⚪ **Scatter Plot**
- ✅ Includes error handling for invalid inputs

---

## 🧩 Technologies Used
- **Python 3.x**
- **pandas** – for data manipulation  
- **pymysql** – for MySQL database connectivity  
- **matplotlib** – for data visualization  

---

## 🗃️ Database Setup

### Step 1: Create Database
```sql
CREATE DATABASE hr;
USE hr;

Step 2: Create Table
CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept VARCHAR(50),
    salary INT,
    experience INT
);

Step 3: Insert Sample Data
INSERT INTO employee VALUES 
(1, 'Asha', 'IT', 60000, 4),
(2, 'Rahul', 'HR', 55000, 3),
(3, 'Meena', 'Finance', 65000, 5);

🖥️ How to Run
1️⃣ Install Required Libraries
pip install pandas pymysql matplotlib

2️⃣ Verify Database Connection

Make sure your MySQL server is running and credentials in the code match:

Username: root

Password: (leave blank or edit as needed)

Database: hr

3️⃣ Run the Program
python hr_visualizer.py

4️⃣ Choose Options

When prompted:

Enter your table name (e.g., employee)

Choose a visualization option:

1. Bar Graph
2. Line Graph
3. Pie Chart
4. Histogram
5. Scatter Plot


Select X and Y columns for plotting.

📊 Example Visualizations
Visualization	Description
📊 Bar Graph	Compare employee vs salary
📈 Line Graph	Show salary trends over experience
🥧 Pie Chart	Show department distribution
📉 Histogram	Display salary frequency
⚪ Scatter Plot	Compare salary vs experience
🛠️ Error Handling

Prints "error" for invalid column selections

Ensures valid database connection before running queries

Prevents crash during wrong user input

👩‍💻 Author

Shifa Thasneem
💻 Python Developer | Data Enthusiast | Cybersecurity Innovator
✨ Turning data into visual stories.
