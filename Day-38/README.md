# Student Performance Analysis System 📝

## Overview
This project is a **Student Performance Analysis System** built entirely using **NumPy**.  
It allows loading, cleaning, manipulating, analyzing, and visualizing student data without using pandas.  

The system works on a CSV file containing student details and scores in multiple subjects.

---

## Features

1. **Load Dataset**
   - Load CSV from user input or default file.
   
2. **Clean Dataset**
   - Remove duplicate rows.
   - Handle missing values (`NaN`).

3. **Convert to Numeric**
   - Convert scores and attendance to numeric format for calculations.

4. **Data Manipulation**
   - Add bonus marks to students.
   - Normalize attendance to 0–1 scale.

5. **Statistics**
   - Calculate mean and standard deviation for each subject.
   - Compute total scores for each student.
   - Identify top scoring students.

6. **Filtering**
   - List students scoring 80+ in all subjects.

7. **Sorting**
   - Display **Top 5 students** based on total scores.

8. **Linear Algebra Operations**
   - Compute **weighted average scores**.
   - Generate **correlation matrix** between subjects.

---

## How to Run

1. Clone or download the repository.
2. Ensure `numpy` and `matplotlib` are installed:

```bash
pip install numpy matplotlib
