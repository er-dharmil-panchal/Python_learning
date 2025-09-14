import numpy as np
import time

from matplotlib import pyplot as plt


# ==================== Load Dataset ====================
def load_dataset():
    path = input("Enter CSV file path (or press Enter for default): ").strip()
    if path == "":
        path = "student_data_dirty.csv"  # default file
    data = np.genfromtxt(path, delimiter=",", skip_header=1, dtype=str)
    print("\\n✅ Dataset Loaded Successfully!")
    print(data)
    return data


def clean_dataset(data):
    print("Dataset Cleaning....")

    # Remove Duplicates
    unique = np.unique(data, return_counts=False, axis=0)
    print("Unique Values: ", unique)
    cleaned = unique.astype(object)
    cleaned[cleaned == ""] = np.nan
    print("Cleaned Values: ", cleaned)
    print(type(cleaned))
    return cleaned


# ==================== Convert to Numeric ====================
def convert_to_numeric(data):
    # RollNo, Name, Math, Science, English, Attendance, ExtraCredit
    roll = data[:, 0].astype(int)
    names = data[:, 1]  # keep names separate
    numeric_data = data[:, 2:].astype(float)
    return roll, names, numeric_data


# ==================== Manipulation ====================
def manipulate_data(numeric_data):
    numeric_data[:, 0] = numeric_data[:, 0] + 5  # add bonus 5 mark in maths
    print("Numeric Data: ", numeric_data)
    attendance = numeric_data[:, 3:4].astype(float)
    attendance_norm = attendance / 100
    numeric_data[:, 3:4] = attendance_norm
    print("Attendance: ", numeric_data)
    return numeric_data

# ====================  Statistics ====================
def statistics(numeric_data):
    math, sci, eng = numeric_data[:, 0], numeric_data[:, 1], numeric_data[:, 2]
    print("\n📈 Statistics:")
    print(f"Mean: Math={np.nanmean(math):.2f}, Sci={np.nanmean(sci):.2f}, Eng={np.nanmean(eng):.2f}")
    print(f"Std Dev: Math={np.nanstd(math):.2f}, Sci={np.nanstd(sci):.2f}, Eng={np.nanstd(eng):.2f}")
    total = np.nansum(numeric_data[:, 0:3], axis=1)
    print(f"Top Student Total Marks: {np.nanmax(total)}")
    return total

# ==================== Filtering ====================
def filtering(numeric_data,data):
    math, sci, eng = numeric_data[:, 0], numeric_data[:, 1], numeric_data[:, 2]
    mask = (math > 80) & (sci > 80) & (eng > 80)
    print(f"There are {np.sum(mask)} students who have 80+ in all subjects")
    print("List of students with their full data:\n")
    sorted_data = sorted(data[mask], key=lambda x: (x[0] + x[1] +x[2]), reverse=True)
    for student in sorted_data:
        print(f"Roll no. {student[0]} Name: {student[1]}, Maths: {student[2]}, Sciences: {student[3]}, English: {student[4]}, total: {float( student[2])+float(student[3])+float(student[4])}")

# ==================== Sorting ====================
def sorting(total, data):
    pair = zip(total, data)
    sorted_data = sorted(pair, key=lambda x: x[0], reverse=True)
    print(f"Top 5 Students: ")
    for total_score, student_row in sorted_data[:5]:
        print(f"{student_row[0]} | Name: {student_row[1]} | Total: {total_score}")

# ====================  Weighted Average & Correlation ====================
def linear_algebra(numeric_data):
    weights = np.array([0.4, 0.3, 0.3])
    marks = numeric_data[:, 0:3]
    clean_marks = marks[~np.isnan(marks).any(axis=1)]
    weighted_scores = clean_marks @ weights
    corr = np.corrcoef(clean_marks.T)
    print("\n📐 Correlation Matrix:\n", corr)
    return weighted_scores

# ==================== Main ====================
def main():
    data = load_dataset()
    data = clean_dataset(data)
    roll, names, numeric_data = convert_to_numeric(data)
    numeric_data = manipulate_data(numeric_data)
    total = statistics(numeric_data)
    filtering(numeric_data,data)
    sorting(total, data)
    linear_algebra(numeric_data)


if __name__ == "__main__":
    main()
