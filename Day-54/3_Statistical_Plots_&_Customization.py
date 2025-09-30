"""
📌 Seaborn - Step 3 (Statistical Plots & Customization)
    - Step 1 & 2 are great for exploring the data (EDA).
    - Step 3 is about finding patterns + making plots look professional.
    - Includes:
        - Regression plots
        - Heatmaps & correlations
        - Clustermaps
        - Matrix plots
        - Statistical relationship plots
        - Themes & customization

   This file covers:
    - Regression plots: regplot, lmplot (with faceting & polynomial fit)
    - Heatmaps & correlations: heatmap, clustermap
    - Matrix plots: pivot table heatmaps
    - Statistical relationship plots: residplot, kdeplot, jointplot, pairplot
    - Themes & palettes: customizing style & colors
    - Parameter explanations: order, ci, hue, scatter_kws, line_kws, cmap, center, linewidths, linecolor

📝 Summary:
    - Regression plots → check relationship + trends between numeric variables
    - Heatmaps → visualize correlations and patterns
    - Clustermaps → correlation clustering
    - Matrix plots → pivot table visualization
    - Statistical relationship plots → explore deeper relationships
    - Themes & palettes → improve style and aesthetics
"""

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
# =====================================================
# ================= Regression Plots ==================
# =====================================================

"""
A regression plot = scatter plot + best-fit line.
It shows:
    - How two numeric variables are related.
    - Whether the relationship is positive, negative, or none.
    - The strength of that relationship.
    - The uncertainty in the trend (confidence interval).
Example: In the tips dataset – as total_bill increases, does tip also increase?
"""

# 👉🏻 Basic Regression Plot.
sns.regplot(x="total_bill", y="tip", data=df, order=1, scatter_kws={"color": "red", "alpha": 0.5, "s": 20},
            line_kws={"color": "blue", "lw": 2})
plt.title("Regression: Total Bill vs Tip (order-1)")
plt.show()
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
sns.regplot(x="total_bill", y="tip", data=df, order=2, scatter_kws={"color": "red", "alpha": 0.5, "s": 20},
            line_kws={"color": "blue", "lw": 2}, ax=axes[0, 0])
axes[0, 0].set_title("Order=2")
sns.regplot(x="total_bill", y="tip", data=df, order=3, scatter_kws={"color": "red", "alpha": 0.5, "s": 20},
            line_kws={"color": "blue", "lw": 2}, ax=axes[0, 1])
axes[0, 1].set_title("Order=3")
sns.regplot(x="total_bill", y="tip", data=df, order=5, scatter_kws={"color": "red", "alpha": 0.5, "s": 20},
            line_kws={"color": "blue", "lw": 2}, ax=axes[1, 0])
axes[1, 0].set_title("Order=5")
sns.regplot(x="total_bill", y="tip", data=df, order=7, scatter_kws={"color": "red", "alpha": 0.5, "s": 20},
            line_kws={"color": "blue", "lw": 2}, ax=axes[1, 1])
axes[1, 1].set_title("Order=7")
plt.tight_layout()
plt.show()

# ci: Confidence interval for regression line.
#   - ci=95 → 95% confidence band
#   - ci=None → remove band
# order: Degree of polynomial fit.
#   - order=1 → straight line (default)
#   - order=2 → curve (quadratic)
# scatter_kws: Customize scatter points.
#   - Example: scatter_kws={"alpha":0.5, "s":50}  (s = size)
# line_kws: Customize regression line.
#   - Example: line_kws={"color":"red", "lw":2}   (lw = line width)


# 👉🏻 lmplot = regplot + extra powers.
"""
    - It is a figure-level function, so:
    - Can create multiple subplots (facets).
    - Supports hue, col, row for grouping.
"""

# Regression by gender
sns.lmplot(x="total_bill", y="tip", hue="sex", data=df)
plt.suptitle("Regression: Male vs Female")
plt.show()

# 👉🏻 IMPORTANT:- Split plots by smoker status (row) and time (col)
# Creates multiple small plots → easy to compare across groups.
sns.lmplot(x="total_bill", y="tip", data=df,
           row="smoker", col="time", hue="sex",
           height=4, aspect=1)
plt.suptitle("Regression with Faceting", x=0.7, y=0.9)
plt.show()

"""
When to Use Regression Plots?
    - To check if two numeric variables are correlated.
    - To quickly see positive/negative relationships.
    - To spot outliers (points far from line).
    - To compare trends across categories (lmplot).
When not !
    - Categorical-only data (use bar/box/violin).
    - Very noisy or non-linear data → regression might mislead.
Recap :
    - regplot: Simple scatter + regression line, customizable.
    - lmplot: Extended version with faceting (hue, row, col).
    - Important parameters: ci, order, hue, scatter_kws, line_kws.
    - Useful for: finding relationships & trends between numeric variables.
"""

# =====================================================
# ============== Heatmaps & Correlations ==============
# =====================================================
"""
- A heatmap is a colored grid that represents data values with colors.
- It’s extremely useful for visualizing correlation matrices — a compact way to see how numeric variables relate to each other.

- Correlation values range from -1 to +1:
    -> +1 → perfect positive correlation (both variables move together)
    -> -1 → perfect negative correlation (one increases, the other decreases)
    ->  0 → no correlation
- Heatmaps are widely used in Exploratory Data Analysis (EDA) to quickly understand patterns.
"""
# 👉🏻 Correlation Matrix
# Before making a heatmap, we need a correlation matrix.

df = sns.load_dataset("tips")
corr = df.select_dtypes(include="number").corr()  # Correlation for all numeric columns
print(corr)

# 👉🏻 Basic Heatmap
# Each cell color shows the correlation between two numeric variables.
# The diagonal is always 1.0 because each variable is perfectly correlated with itself.
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
# annot=True -> shows numbers inside each cell
# cmap="coolwarm" -> diverging colors for positive/negative correlation

# 👉🏻 Heatmap Customizations
# We can adjust color palettes, add gridlines, center the colors, etc.
sns.heatmap(corr, annot=True, cmap="viridis", center=0, linewidths=10, linecolor="Black")
plt.title("Correlation Heatmap")
plt.show()

# center=0 → highlights zero correlation
# linewidths & linecolor → create a grid


# =====================================================
# =================== Clustermap ======================
# =====================================================
sns.clustermap(corr, annot=True, cmap="coolwarm", center=0,
               linewidths=1, figsize=(8, 6))
plt.suptitle("Clustermap of Correlations", y=1.05)
plt.show()

# =====================================================
# ============= Matrix Plots (Example) ================
# =====================================================

flights = sns.load_dataset("flights")
pivot = flights.pivot("month", "year", "passengers")
sns.heatmap(pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Flights Heatmap (Pivot Table)")
plt.show()

# =====================
# 3.5
# =====================

# =====================================================
# ======== Statistical Relationship Plots =============
# =====================================================

sns.residplot(x="total_bill", y="tip", data=df,
              scatter_kws={"color": "green", "alpha": 0.4},
              line_kws={"color": "red", "lw": 2})
plt.title("Residual Plot: Total Bill vs Tip")
plt.show()

sns.kdeplot(x=df["total_bill"], y=df["tip"],
            cmap="Reds", fill=True)
plt.title("2D KDE Plot")
plt.show()

sns.jointplot(x="total_bill", y="tip", data=df,
              kind="hex", cmap="coolwarm")
plt.suptitle("Joint Plot: Hexbin", y=1.02)
plt.show()

sns.pairplot(df, hue="sex")
plt.suptitle("Pairplot of Tips Dataset", y=1.02)
plt.show()

# =====================
# Customization (Themes & Palettes)
# =====================
sns.set_theme(style="whitegrid")
sns.set_palette("Set2")
sns.catplot(x="day", y="total_bill", hue="sex",
            kind="bar", data=df)
plt.title("Categorical Plot with Custom Theme & Palette")
plt.show()

# Palplot to visualize palette
sns.palplot(sns.color_palette("Set2"))
plt.title("Custom Color Palette")
plt.show()

# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick Recap:
- Regression plots → sns.regplot(), sns.lmplot() for trends and relationships
- order → polynomial degree, ci → confidence interval
- Heatmaps → sns.heatmap() for correlations, annot=True for values
- center → highlight zero correlation, cmap → color palette
- Clustermaps → sns.clustermap() for grouped similarity
- Themes & Palettes → sns.set_theme(), sns.set_palette()
- Figure-level plots → sns.catplot(), sns.relplot() for faceting
"""
