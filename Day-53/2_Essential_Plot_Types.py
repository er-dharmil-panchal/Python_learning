"""
📌 Seaborn - Step 2 (Categorical & Distribution Plots)
    - Seaborn is great for categorical and distribution plots because it automatically:
        - Groups data
        - Calculates summary statistics
        - Applies nice styles by default

   This file covers:
    - Categorical plots: bar plot, count plot, box plot, violin plot, strip plot, swarm plot
    - Distribution plots: histogram, KDE plot, displot, ECDF plot, rug plot, joint plot, pair plot
    - Parameter explanations: hue, style, size, ci, palette, jitter, dodge
    - Combining categorical and distribution plots for EDA

📝 Summary:
    - Categorical plots → compare categories, frequencies, and distributions
    - Distribution plots → show spread, density, and probability of data
    - hue → changes plot colors by category
    - style → changes marker shapes for categories
    - size → changes marker sizes for numerical variables
    - ci → confidence interval for statistical certainty
    - Seaborn + Matplotlib → combine for detailed customization
"""

# =====================================================
# ====================== Dataset ======================
# =====================================================

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
# Columns:
# total_bill, tip, sex, smoker, day, time, size


# =====================================================
# ================= Categorical Plots =================
# =====================================================

# Used when one axis is categorical (day, gender, smoker, etc.)
# Helpful for comparing averages, frequencies, distributions, and raw data points

# ============== Bar Plot ==================

# Compare an aggregate (mean, median, etc.) across categories.
sns.barplot(x="day", y="total_bill", data=df, hue="sex", palette="rocket", ci=95, capsize=0.1, edgecolor="black")
# sns.catplot(x="day", y="total_bill", data=df, hue="sex", palette="rocket", ci=None)
plt.title("Average Bill by Day and Gender")
plt.show()

"""
ci = Confidence Interval
-> When you measure something (like average bill), you don’t know the exact true value for everyone.
   The confidence interval tells you how sure you are about your average.
   - If the CI is small → you’re pretty sure about the average.
   - If the CI is big → you’re less sure.
   Example: average bill is 20±2 means it's between 18 to 22
capsize=0.1 -> Add caps to the error bars for cleaner visuals (for CI lines).
"""

# ============== Count Plot ==================
# Show counts of each category.

sns.countplot(x="day", hue="sex", data=df, palette="bright")
plt.title("Count of Bills by Day and Gender")
plt.show()
# Use case: Seeing frequency of categories, e.g., how many bills per day.


# ============== Box Plot ==================

# Show distribution summary (median, quartiles, outliers).
sns.boxplot(x="day", y="total_bill", hue="smoker", data=df)
plt.title("Total Bill by Day and Smoker Status")
plt.show()

# A box plot shows the spread of data using the five-number summary: min, Q1, median, Q3, and max.
# The box covers Q1 to Q3 (middle 50% of data), the line inside is the median, and whiskers extend to min and max values.
# Dots or bubbles outside whiskers are outliers — unusual values far from the rest of the data.


# ============== Violin Plot ==================

# Show distribution shape + summary statistics.
sns.violinplot(x="day", y="total_bill", data=df, hue="sex", palette="rocket", split=True)
plt.title("Violin Plot by Day and Gender")
plt.show()
# Combines box plot + KDE
# Can split violins using split=True


# ============== Strip Plot ==================
# Show individual observations with jitter to avoid overlap.

sns.stripplot(x="day", y="total_bill", hue="sex", data=df, jitter=True, dodge=True)
plt.title("Strip Plot with Hue")
plt.show()

# jitter -> When many points overlap (same x position), they stack on top of each other and you can’t see them clearly.
#           jitter=True spreads them out a little horizontally (adds random noise in x-axis) so you can actually see individual points.
#   Think: crowd of people → they step a little left and right so you see everyone.
# dodge -> When you have multiple categories (hue), by default all points/bars overlap at the same x position.
#           dodge=True separates them side by side so you can compare groups more clearly.
#   Example: Male vs Female tips shown next to each other instead of stacked.


# ============== Swarm Plot ==================
# Show individual observations, arranged to avoid overlap.
# Similar to stripplot, but intelligently arranges points to avoid overlap.
sns.swarmplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("Swarm Plot with Hue")
plt.show()

"""
These are all Categorical Plots:
    - barplot → Compare category averages (mean).
    - countplot → Frequency of categories.
    - boxplot → Distribution summary + outliers (min, Q1, median, Q3, max).
    - violinplot → Distribution + density + summary.
    - stripplot → Raw points (small datasets).
    - swarmplot → Raw points, but better arrangement (small/medium datasets).
"""


# =====================================================
# ================ Distribution Plots =================
# =====================================================

# Show how data is spread or distributed over a range of values
# Useful for understanding patterns, skewness, and density of data


# ============== Histogram ==================
# Show distribution of a numeric variable.

# Without KDE
sns.histplot(df["total_bill"], bins=20, kde=False)
plt.title("Histogram of Total Bill")
plt.show()

# With KDE
sns.histplot(df["total_bill"], bins=20, kde=True)
plt.title("Histogram of Total Bill with KDE")
plt.show()

# bins='auto' or bins='fd' (Freedman–Diaconis) often works well
# KDE = Kernel Density Estimate.
# Use histogram to see counts and discrete bin-based view.
# Use KDE to see a smooth estimate of the distribution shape.
# Often best to show both: histogram (bars) with KDE overlay (smooth curve).


# ============== KDE Plot ==================
# Smooth estimate of distribution.
sns.kdeplot(df["total_bill"], shade=True)
plt.title("KDE Plot of Total Bill")
plt.show()

sns.kdeplot(df[df["sex"] == "Male"]["total_bill"], label="Male", shade=True)
sns.kdeplot(df[df["sex"] == "Female"]["total_bill"], label="Female", shade=True)
plt.title("KDE by Gender")
plt.legend()
plt.show()

# If KDE is flat, data is spread evenly.
# If KDE has multiple peaks → multimodal distribution (separate subgroups).


# ============== Displot ==================
# Combine histogram + KDE, supports faceting.
sns.displot(df["total_bill"], kde=True, bins=20)
plt.title("Distribution of Total Bill")
plt.show()

sns.displot(df, x="total_bill", hue="sex", kind="kde", fill=True)
plt.show()

# Practice Example — Combining Categorical & Distribution Plots
sns.boxplot(x="day", y="total_bill", hue="smoker", data=df)
sns.stripplot(x="day", y="total_bill", hue="smoker", data=df, dodge=True, jitter=True, alpha=0.5)
plt.title("Box + Strip Plot Combination")
plt.show()

# Histogram = bars,
# KDE = smooth curve,
# Displot = wrapper that can do both (and more, like ECDF + faceting).

# 👉 Some other Distribution plots

# 1) Empirical Cumulative Distribution Function (ECDF)
#    Shows cumulative probability up to x.
# Use: To see medians/percentiles.
plt.figure(figsize=(6, 4))
sns.ecdfplot(df["total_bill"], color="red")
plt.title("ECDF of Total Bill")
plt.show()
# If line at $20 = 70%, means 70% of bills ≤ $20.

# 2) Rug Plot
#    Tiny lines at each data point.
# Use: To show raw data distribution.
#      Retail: Spot days with high sales (scan barcode).
plt.figure(figsize=(6, 4))
sns.rugplot(df["total_bill"], height=0.1, color="black")
plt.title("Rug Plot of Total Bill")
plt.show()
# Each little tick mark in a rug plot represents one data point.
# Rug plots work best with small datasets.

# 3) Joint Plot
#    Shows relationship between 2 variables + marginals.
# Use: To study correlation and distributions together.
sns.jointplot(data=df, x="total_bill", y="tip", kind="scatter", color="purple")
plt.suptitle("Joint Plot of Total Bill vs Tip", y=1.02)
plt.show()

# 4) Pair Plot (IMP)
#    Grid of plots for every pair of numeric columns.
# Use: Quick dataset overview (EDA).
sns.pairplot(df, hue="sex")
plt.suptitle("Pairplot of Tips Dataset", y=1.02)
plt.show()

# Diagonal = histograms, off-diagonal = scatter plots.
# Helps detect correlation patterns.

"""
Distribution Plots:
    - Histogram -> counts per range
    - KDE -> smooth probability curve
    - ECDF -> cumulative percentage
    - Rugplot -> raw values
    - Displot -> grouped distributions
    - Jointplot -> 2D + marginals
    - Pairplot -> all pairwise plots
"""


# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick Recap:
- Categorical Plots → compare categories, frequencies, and distributions
    - barplot -> compare category averages
    - countplot -> show frequency of categories
    - boxplot -> show distribution summary + outliers
    - violinplot -> distribution shape + summary statistics
    - stripplot -> show individual observations with jitter
    - swarmplot -> show individual observations with smart arrangement
- Distribution Plots -> understand spread, density, and probability
    - histplot -> histogram ± KDE
    - kdeplot -> smooth estimate of distribution
    - displot -> combination of histogram/KDE, supports faceting
    - ecdfplot -> cumulative distribution
    - rugplot -> show raw values as ticks
    - jointplot -> bivariate relationship + marginals
    - pairplot -> pairwise relationships of variables
- Parameters:
    - hue -> changes colors by category
    - style -> changes marker shapes by category
    - size -> changes marker size by numeric variable
    - ci -> confidence interval for statistical certainty
    - palette -> color scheme
    - jitter -> adds noise to avoid overlap
    - dodge -> separates categories side-by-side
"""
