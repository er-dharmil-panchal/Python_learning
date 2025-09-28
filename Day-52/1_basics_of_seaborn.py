"""
📌 Seaborn - Step 1 (Basics + Relational Plots)
    - Seaborn is a Python visualization library built on top of Matplotlib.
    - Seaborn makes plots pretty and high-level, but Matplotlib still controls low-level things
        (like figure size, titles, saving).
    - Seaborn directly works with Pandas DataFrames.

   This file covers:
    - Installing & importing Seaborn
    - Loading datasets
    - How Seaborn integrates with Pandas and Matplotlib
    - Relational plots: scatter plot, line plot
    - Enhancements using hue, style, and size
    - Customizing plots with Matplotlib functions

📝 Summary:
    - Seaborn → simplifies statistical plotting and works directly with DataFrames
    - hue → changes point colors based on a variable
    - style → changes marker shape based on a variable
    - size → changes marker size based on a variable
    - Seaborn + Matplotlib → combine for powerful customization
"""

import seaborn as sns
import matplotlib.pyplot as plt

# =====================================================
# =================== basic Plots =====================
# =====================================================

# --- with Matplotlib ---
x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y)
plt.title("Plot with Matplotlib")
plt.show()

# --- with Seaborn ---
sns.lineplot(x=[1, 2, 3], y=[4, 5, 6])
plt.title("Plot with Seaborn")
plt.show()
# Seaborn needs fewer lines for a clean plot.


# =====================================================
# ====================== Dataset ======================
# =====================================================

# 👉🏻 Seaborn has built-in datasets for practice.
df = sns.load_dataset("tips")  # Restaurant bills dataset
print(df.head())

# Columns:
# total_bill: Bill amount in USD
# tip: Tip given
# sex: Customer gender
# smoker: Yes/No
# day: Day of week
# time: Lunch/Dinner
# size: Table size

# =====================================================
# ================= Relational Plots ==================
# =====================================================

# ============== Scatter Plot ==================
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()
# Notice we don’t need df['total_bill'], just pass column names.

# Enhancements with Seaborn:
sns.scatterplot(x="total_bill", y="tip", hue="time", style="sex", size="size", data=df)
plt.show()

# Explanation:
# hue :-    hue changes the color of the points/lines based on a categorical or numerical variable.
#            It’s useful when you want to visually separate groups.
# style :-  style changes the marker shapes (circle, triangle, square, etc.) based on a categorical variable.
#            Useful for distinguishing groups visually without relying on color.
#            Legend will show marker shapes.
# size :-   size changes the marker size based on a numerical variable.
#            Useful to add a third quantitative dimension to your plot.


# ============== Line Plot ==================
sns.lineplot(x="total_bill", y="tip", data=df, hue="time", style="sex")
plt.show()

# --- Practice Example ---
sns.scatterplot(x="total_bill", y="tip", hue="time", data=df)
plt.title("Bill vs Tips wrt Time")
plt.xlabel("Total Bill")
plt.ylabel("Tips")
plt.show()

# =====================================================
# ======= Notes on Pandas, Seaborn, Matplotlib =======
# =====================================================

"""
Pandas group support:
    - Reads the "time" column
    - Automatically assigns colors to each group
    - Adds a legend
Seaborn + Matplotlib
    - sns.scatterplot() → creates the plot
    - plt.title(), plt.xlabel() → Matplotlib functions that customize the plot
    - You can combine Seaborn plots + Matplotlib customization seamlessly.

Pandas → data handling
Seaborn → statistical visualization
Matplotlib → customization & control
"""

# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick Recap:
- Seaborn → built on Matplotlib, works directly with Pandas DataFrames
- sns.scatterplot() → scatter plots, supports hue, style, size
- sns.lineplot() → line plots, supports grouping with hue/style
- hue → changes point/line color by category or numeric variable
- style → changes marker shapes by category
- size → changes marker size by numeric variable
- Integration → use Matplotlib functions (plt.title(), plt.xlabel(), plt.savefig()) to customize Seaborn plots
"""
