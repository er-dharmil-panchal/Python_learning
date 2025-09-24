"""
📌 Matplotlib - Step 2 (Essential Plot Types)
    - Real-world data rarely needs just a line,
    - We often need different plot types to represent distributions, comparisons, and relationships.

   This file covers:
    - Different plot types for real-world data visualization
    - How to compare categories, show relationships, and distributions
    - Bar plots, scatter plots, histograms, pie plots, area plots
    - Customizations, legends, subplots, annotations

📝 Summary:
    - Bar Plot → compare quantities across categories
    - Scatter Plot → show relationship between two variables
    - Histogram → show distribution of numerical data
    - Pie Plot → show proportion of categories in a whole
    - Area Plot → show trends and cumulative data
"""

import matplotlib.pyplot as plt
import numpy as np

# =====================================================
# ===================== Bar Plot ======================
# =====================================================

"""
    - Bar plots are perfect when you want to compare quantities across categories 
    - e.g., sales by product, marks by subject.
    
    Functions :
        - plt.bar(x, height) → vertical bars
        - plt.barh(y, width) → horizontal bars
    Key Customizations:
        - color → fill color
        - edgecolor → border color
        - width → bar thickness (for vertical bars)
        - alpha → transparency (0 → invisible, 1 → solid)
        - align → "center" (default) or "edge"
"""

categories = ["A", "B", "C", "D"]
values = [23, 45, 56, 78]

# ============== VERTICAL BAR PLOT ====================
plt.bar(categories, values, color="pink", edgecolor="black", alpha=0.8, align="center")
plt.title("Vertical Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# ============== HORIZONTAL BAR PLOT ==================
plt.barh(categories, values, color="blue", alpha=0.8, align="center", edgecolor="black")
plt.title("Horizontal Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

categories = ["A", "B", "C", "D"]
values1 = [23, 45, 56, 78]
values2 = [18, 40, 60, 70]

# ============== Multiple Bar Plots ==================
# Compare two datasets side by side.

x = np.arange(len(categories))  # positions
width = 0.35  # bar width

plt.bar(x - width / 2, values1, width, label="Set 1", color="skyblue")
plt.bar(x + width / 2, values2, width, label="Set 2", color="orange")

plt.xticks(x, categories)  # replace numbers with category names
plt.title("Grouped Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()  # Display legend for plots that have a 'label' defined
plt.show()

# ============== Stacked Bar Plots ==================
values1 = [23, 45, 56, 78]
values2 = [18, 40, 60, 70]

plt.bar(categories, values1, color="lightblue", label="Set 1")
plt.bar(categories, values2, bottom=values1, label="Set 2", color="lightgreen")
plt.title("Stacked Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()
plt.show()

# 👉🏻 Bar Labels (Annotating Bars)
bars = plt.bar(categories, values, color="lightcoral")
plt.title("Bar Plot with Labels")

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(height),
             ha="center", va="bottom", fontsize=10)

plt.show()

# =====================================================
# ================== Scatter Plots ====================
# =====================================================
"""
    - Scatter plots are used to show the relationship between two variables.
"""

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y, color="red")
plt.title("Basic Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()

# 👉🏻 Customizing Scatter Points
plt.scatter(x, y,
            color="green",  # Point color
            s=100,  # Size of points
            marker="o",  # Shape ('o','s','^','x','*')
            edgecolor="blue",  # Outline color
            alpha=0.7, )  # Transparency
plt.title("Customized Scatter Plot")
plt.show()

# ============== Multiple Scatter Sets (with legend) ==================
x1 = [5, 7, 8, 7, 2, 17]
y1 = [99, 86, 87, 88, 100, 86]

x2 = [2, 9, 4, 11, 12, 9, 6]
y2 = [103, 87, 94, 78, 77, 85, 86]

plt.scatter(x1, y1, color="red", edgecolors="blue", s=80, label="Set 1")
plt.scatter(x2, y2, color="green", edgecolors="blue", s=80, label="Set 2")
plt.title("2 Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)
plt.show()

# =====================================================
# ==================== Histograms =====================
# =====================================================
"""
NOTE :- Sequence will change (order doesn’t matter)
    - Histograms are used to show the distribution of numerical data by dividing data into bins (intervals)
        and counting how many values fall into each bin.
        
   Example use cases:     
    - Exam scores distribution
    - Age distribution in a population
    - Sales per price range
   
   How it works:
    - It looks at your data’s min and max values.
    - Then it splits that range into equal-sized bins (unless you manually set bins or range)
    
    eg -> If your data ranges from 2 to 17 (data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]) and bins=5, it will create 5 bins: 
            [2–5), [5–8), [8–11), [11–14), [14–17]
            min = 2, max = 17
            -> 17-2 = 15 / 5 = 3(So each bin covers 3 units from min to max)
    - Count how many data points fall in each bin
        Bin [2–5) → 3 points  (2,2,4) 
        Bin [5–8) → 4 points  (5,7,7,6)
        Bin [8–11) → 3 points  (8,9,9)
        Bin [11–14) → 2 points  (11,12)
        Bin [14–17] → 1 point   (17)

Note :- More bins → more granular distribution
"""

data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
plt.hist(data, bins=5)  # bins = number of intervals
plt.title("Basic Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

counts, bins = np.histogram(data, bins=5)
print("Bin edges:", bins)
print("Counts:", counts)

# 5 → Bin 2, 7 → Bin 2, 8 → Bin 3,  7 → Bin 2....

# 👉🏻 Customizing Histograms
plt.hist(
    data,
    bins=7,  # More bins → more detail
    color="skyblue",  # Fill color
    edgecolor="black",  # Border color of bars
    alpha=0.7  # Transparency
)
plt.title("Customized Histogram")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# 👉🏻 Histogram with Density
# Shows relative distribution (percentages rather than counts)
# Useful for statistical analysis
plt.hist(
    data,
    bins=7,
    density=True,  # Normalize to area=1
    color="lightgreen",
    edgecolor="black"
)
plt.title("Histogram with Density")
plt.xlabel("Value Range")
plt.ylabel("Density")
plt.show()

# 👉🏻 Multiple Histograms in One Plot
data1 = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
data2 = [6, 9, 11, 7, 5, 14, 3, 8, 10, 12, 15]

plt.hist(data1, bins=7, alpha=0.7, label="Dataset 1", color="skyblue")
plt.hist(data2, bins=7, alpha=0.5, label="Dataset 2", color="orange")

plt.title("Multiple Histograms")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# 👉🏻Bar Labels in Histogram
counts, bins, patches = plt.hist(data, bins=5, color="lightcoral", edgecolor="black")
plt.title("Histogram with Labels")
for count, patch in zip(counts, patches):
    plt.text(patch.get_x() + patch.get_width() / 2, count + 0.5, str(int(count)), ha="center", va="bottom", fontsize=10)
plt.show()

# =====================================================
# ============ Bar vs Scatter vs Histogram ============
# =====================================================
"""
| Feature               | Bar Plot                 | Scatter Plot             | Histogram              |
| --------------------- | ------------------------ | ------------------------ | ---------------------- |
| Data Type             | Categorical/Numerical    | Numerical                | Numerical              |
| Shows                 | Comparison of categories | Relationship/correlation | Distribution of values |
| X-axis meaning        | Categories               | Variable values          | Bin ranges             |
| Y-axis meaning        | Values per category      | Values per variable      | Frequency/count        |
| Sequence matters?     | No                       | Yes                      | No                     |

"""

# =====================================================
# ==================== Pie Plots ======================
# =====================================================
"""
    A pie plot is used to show proportions of a whole.
    Each slice represents a category’s proportion relative to the total.
    They’re best for categorical data where we want to visually compare parts to a whole.
    
   Key Points:
    - Each slice = one category
    - Size of slice = proportion of category in total
    - Useful for percentage comparisons
    - Avoid too many slices — best for ≤ 6 categorie
    
    Syntax :- plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        - sizes → list of values
        - labels → list of category labels
        - autopct → format string for percentage labels (e.g., "%.1f%%")
        - startangle → rotates starting position of first slice
        - colors → custom slice colors
        - explode → separate slices for emphasis
"""

labels = ["Apples", "Bananas", "Cherries", "Dates"]
sizes = [25, 30, 20, 25]
plt.figure(figsize=(8, 8))  # Bigger square figure
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=-45, colors=["red", "pink", "yellow", "lime"],
        explode=(0, 0.1, 0, 0))
plt.title("Fruit Distribution")
plt.legend(labels, loc="best")
plt.axis("equal")
plt.show()

"""
plt.axis("equal")  # Forces pie chart to be a perfect circle
plt.figure(figsize=(8, 8))  # Bigger square figure
plt.tight_layout()  # Adjust layout
"""

# =====================================================
# ==================== Area Plots =====================
# =====================================================

# An area plot is like a line plot but with the area below the line filled with color.
# It’s useful for showing trends over time and visualizing cumulative values.

x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 8, 7]

plt.plot(x, y, color="blue")  # Line plot
plt.fill_between(x, y, color="skyblue", alpha=0.4)  # Fill area under line
plt.title("Basic Area Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()

# 👉🏻 Area Plot with Multiple Areas

y2 = [1, 2, 4, 6, 5]

plt.fill_between(x, y, color="lightblue", alpha=0.5, label="Series 1")
plt.fill_between(x, y2, color="lightgreen", alpha=0.5, label="Series 2")

plt.plot(x, y, color="blue")
plt.plot(x, y2, color="green")
plt.title("Stacked Area Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)
plt.show()

# 👉🏻 Area Plot with Baseline

baseline = 2
plt.fill_between(x, y1, baseline, color="orange", alpha=0.3)
plt.plot(x, y1, color="red")
plt.title("Area Plot with Baseline")
plt.show()

# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick Recap:
- Bar Plot → plt.bar(), plt.barh(), grouped & stacked bars
- Scatter Plot → plt.scatter(), customize color, size, marker
- Histogram → plt.hist(), bins, density, multiple datasets
- Pie Plot → plt.pie(), autopct, explode, labels
- Area Plot → plt.fill_between(), trends & baselines
- Legends → plt.legend()
- Annotations → plt.text()
"""