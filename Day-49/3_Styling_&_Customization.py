"""
📌 Matplotlib - Step 3 (Styling & Customization)
    - Styling makes plots readable, presentation-ready, and visually consistent.
    - Customizing plots improves clarity, highlights key points, and creates professional visualizations.

   This file covers:
    - Controlling axis limits and aspect ratios
    - Customizing ticks (major & minor)
    - Using locators and formatters
    - Adding and styling legends
    - Applying colors, linestyles, markers, and style sheets
    - Adding text and annotations
    - Understanding Axis vs Axes

📝 Summary:
    - Axis → control visible range and aspect ratio
    - Ticks → improve readability with custom positions, labels, and formatting
    - Legends → label and distinguish plot elements
    - Styling → enhance aesthetics via colors, linewidths, linestyles, markers
    - Style Sheets → apply predefined visual themes
    - Text/Annotations → highlight points and add descriptions
    - Axis vs Axes → understand the difference for better plotting control
"""

import matplotlib.pyplot as plt
import numpy as np

# =====================================================
# ======================= Axis ========================
# =====================================================

x = np.linspace(0, 10, 200)
y = np.sin(x)
plt.plot(x, y, label="sin(x)")
plt.title("Axis limits example")
plt.xlabel("x")
plt.ylabel("sin(x)")

# Set limits for x and y,
plt.xlim(2, 8)  # show 2 ≤ x ≤ 8
plt.ylim(-1.2, 1.2)  # set y-range
plt.legend()
plt.grid(True)
plt.show()

# Alternative: plt.axis([xmin, xmax, ymin, ymax])
plt.plot(x, y)
plt.axis([0, 10, -0.8, 0.8])
plt.title("plt.axis([xmin,xmax,ymin,ymax])")
plt.show()

# Shortcuts: 'tight' and 'equal'
plt.plot(x, np.cos(x))
plt.axis('tight')  # fit axis tightly to data
plt.title("Tight")
plt.show()

plt.plot(x, np.sin(x))
plt.axis('equal')  # equal scaling on x & y
plt.title("Equal")
plt.show()

# =====================================================
# ====================== Ticks ========================
# =====================================================
import matplotlib.ticker as tck

# positions, rotation, locators & formatters
# Improve readability; avoid overlapping ticks; format numbers (percent/currency).
x = np.linspace(0, 2 * np.pi, 9)
y = np.sin(x)
plt.plot(x, y, marker='o')
plt.title("Custom ticks + rotation")
# custom tick positions and labels
plt.xticks(x, [f"{val:.2f}" for val in x], rotation=45)
plt.yticks([-1, 0, 1])
plt.show()

# set ticks
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xticks([0, 2, 4, 6, 8, 10])  # major ticks
ax.minorticks_on()  # enable minor ticks
plt.title("setting ticks")
plt.show()

# Major ticks: 0, 2, 4, 6, 8, 10 (with labels)
# Minor ticks: small unlabeled marks in between major ticks

# Percent formatting:
vals = np.random.rand(6)  # between 0 and 1
x = np.arange(len(vals))
fig, ax = plt.subplots()
ax.bar(x, vals)
ax.yaxis.set_major_formatter(tck.PercentFormatter(xmax=1.0))
ax.set_title("Percent formatted y-axis")
plt.show()

# FuncFormatter example (thousands):
sales = [1500, 3000, 4500, 7000]
months = ["Jan", "Feb", "Mar", "Apr"]


def thousands(x, pos):
    if x >= 1000:
        return f'{int(x / 1000)}k'
    return f'{int(x)}'


fig, ax = plt.subplots()
ax.bar(months, sales)
ax.yaxis.set_major_formatter(tck.FuncFormatter(thousands))
ax.set_title("Sales (k)")
plt.show()

# Tick locators (set spacing):
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.xaxis.set_major_locator(tck.MultipleLocator(2))  # ticks every 2 units
# plt.xticks(x[::2])
ax.xaxis.set_minor_locator(tck.MultipleLocator(0.5))  # minor ticks
ax.grid(which='major', color='red', linestyle='-', linewidth=2)
ax.grid(which='minor', color='blue', linestyle='--', linewidth=0.5)
ax.minorticks_on()
plt.show()

# =====================================================
# ======================= LEGENDS =====================
# =====================================================
# Legends identify plots. Use plt.legend() with labels and position arguments.
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)", color="blue")
plt.plot(x, y2, label="cos(x)", color="green")
plt.title("Legends Example")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right", fontsize=10, shadow=True)
plt.grid(True)
plt.show()

# =====================================================
# ==================== STYLING ========================
# =====================================================
# Styling improves visual appeal.
# Controls include colors, linewidth, linestyle, markers, and style sheets.

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, color="purple", linewidth=2, linestyle="--", marker="o", markersize=6)
plt.title("Line Styling")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()

# Built-in style sheets for consistent styling
plt.style.use("ggplot")
plt.plot(x, y)
plt.title("ggplot Style")
plt.show()

plt.style.use("seaborn-darkgrid")
plt.plot(x, y)
plt.title("Seaborn Darkgrid Style")
plt.show()

# =====================================================
# ================= TEXT & ANNOTATIONS ================
# =====================================================
# Text and annotations help highlight points or explain features on a plot.
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Text & Annotation Example")
plt.text(2, 0.5, "Local Max", fontsize=12, color="red")
plt.annotate("Peak", xy=(1.57, 1), xytext=(3, 1.2),
             arrowprops=dict(facecolor="black", shrink=0.05))
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()

# =====================================================
# ================= AXIS VS AXES ======================
# =====================================================
# Axis = single dimension scale (x-axis or y-axis)
# Axes = entire plot area containing x-axis and y-axis
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Axis vs Axes")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.grid(True)
plt.show()

# =====================================================
# =================== QUICK RECAP =====================
# =====================================================
"""
Quick recap:
- Axis: control limits and aspect ratio
- Ticks: major & minor ticks, locators, formatters
- Legends: labels, location, fontsize, shadow
- Styling: color, linewidth, linestyle, markers
- Stylesheets: plt.style.use
- Text/Annotations: plt.text, plt.annotate
- Axis vs Axes distinction
"""
