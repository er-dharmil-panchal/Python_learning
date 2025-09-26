"""
📌 Matplotlib - Step 4 (Multiple Plots & Subplots)

This file covers:
- Multiple lines in one figure
- Subplots using plt.subplot()
- Subplots using plt.subplots()
- Looping through subplots
- Sharing axes
- Subplot adjustments
- Advanced subplot controls

📝 Summary:
- Multiple lines → overlay plots in one figure
- plt.subplot() → manual subplot control
- plt.subplots() → cleaner API with fig & ax
- Loops → efficient for multiple subplots
- sharex/sharey → sync axes
- Layout adjustments → tight_layout(), subplots_adjust()
- Advanced controls → common titles, labels, spacing, legends
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tck

# =====================================================
# =========== Multiple Lines in One Figure ============
# =====================================================

# Just call plt.plot() multiple times before plt.show().
# Each call adds a new line to the same figure.
# Use labels, legends, colors, line styles to differentiate.

# Example :- Quadratic vs Cubic
x = np.linspace(-3, 3, 500)
y1 = x ** 2
y2 = x ** 3

plt.figure(figsize=(10, 6))
plt.title("Quadratic vs Cubic", fontsize=16, fontweight="bold")
plt.plot(x, y1, color="blue", label="Quadratic", linestyle="-", linewidth=2)
plt.plot(x, y2, color="red", label="Cubic", linestyle="-", linewidth=2)
plt.fill_between(x, y1, y2, color="skyblue", alpha=0.4)
plt.xlabel("Values", fontsize=12)
plt.ylabel("Output", fontsize=12)
plt.axis([-3, 3, -30, 30])
plt.grid(True, linestyle="--", color="gray")
plt.legend(loc="best")
plt.show()

# Key Points:
# Always add legend (plt.legend()).
# Keep grid for clarity.

# =====================================================
# =========== Subplots using plt.subplot() ============
# =====================================================

# Instead of drawing all lines on one graph,
# we can split the figure into smaller sections and draw one plot per section.

# Multiple calls to plt.subplot() create independent plots in one figure.
# Each subplot can have its own title, labels, grid.
# plt.subplot(2, 2, 1) → 2×2 grid, first subplot.

# >> Example 1: 2×1 (Two Functions, One Column)
x = np.linspace(0, 2 * np.pi, 500)
plt.figure(figsize=(10, 6))

# Top subplot → sin(x)
plt.subplot(2, 1, 1)  # (rows=2, cols=1, index=1)
plt.plot(x, np.sin(x), color="blue")
plt.xlim(0, 2 * np.pi)
plt.xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi], labels=["0", "π/2", "π", "3π/2", "2π"], fontsize=10)
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.title("sin(x)")
plt.grid(True)

# Bottom subplot → sin(x)
plt.subplot(2, 1, 2)  # (rows=2, cols=1, index=2)
plt.plot(x, np.cos(x), color="red")
plt.xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi], labels=["0", "π/2", "π", "3π/2", "2π"], fontsize=10)
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.xlim(0, 2 * np.pi)
plt.title("cos(x)")
plt.grid(True)
plt.tight_layout()
plt.show()

# >> Example 2: 2×2 Grid (4 Functions)
x = np.linspace(-3, 3, 500)
plt.figure(figsize=(10, 8))

# Quadratic
plt.subplot(2, 2, 1)
plt.plot(x, x ** 2, color="blue")
plt.title("y = x²")
plt.grid(True)

# Cubic
plt.subplot(2, 2, 2)
plt.plot(x, x ** 3, color="green")
plt.title("y = x³")
plt.grid(True)

# Exponential
plt.subplot(2, 2, 3)
plt.plot(x, np.exp(x), color="red")
plt.title("y = exp(x)")
plt.grid(True)

# Sigmoid
plt.subplot(2, 2, 4)
plt.plot(x, 1 / (1 + np.exp(-x)), color="purple")
plt.title("Sigmoid")
plt.grid(True)

plt.tight_layout()
plt.show()

#  >> Example 3: 1×3 Row of Subplots
x = np.linspace(0, 2 * np.pi, 500)
plt.figure(figsize=(12, 4))

# sin(x)
plt.subplot(1, 3, 1)
plt.plot(x, np.sin(x), color="blue")
plt.title("sin(x)")

# cos(x)
plt.subplot(1, 3, 2)
plt.plot(x, np.cos(x), color="red")
plt.title("cos(x)")

# tan(x)
plt.subplot(1, 3, 3)
plt.plot(x, np.tan(x), color="green")
plt.title("tan(x)")
plt.ylim(-5, 5)  # keep graph readable

plt.tight_layout()
plt.show()

# Good For small projects or learning — but becomes messy for bigger figures.
# For professional use -> plt.subplots() (Next topic)


# =====================================================
# =========== Subplots with plt.subplots() ============
# =====================================================

# Gives explicit access to fig (figure) and ax (axes) objects.
# Easier to control each subplot individually.
# Cleaner syntax for large subplot grids.
# Better for shared axes and advanced customization.

"""
Syntax:
    fig, ax = plt.subplots(nrows, ncols, figsize=(width, height), sharex=False, sharey=False)
        - nrows, ncols → grid size
        - figsize → size of figure
        - ax → NumPy array of axes if more than one subplot
        - sharex, sharey → share axis scale between plots
    
    fig → the figure object (the whole plotting window)
    ax → the axes object(s) (the individual plots inside the figure)
    
    sharex=True → all subplots share the same x-axis range and ticks.
    sharey=True → all subplots share the same y-axis range and ticks.
    
    When there are multiple subplots:
        - ax becomes a 2D NumPy array containing each subplot’s axes:
            ax = [[ax[0,0], ax[0,1]], [ax[1,0], ax[1,1]]]
        - You access individual subplots by index:
            ax[0,0].plot(...)
            ax[1,1].set_title(...)

"""

# >> Example 1: Sin & Cos (2 Subplots)
x = np.linspace(0, 2 * np.pi, 500)

fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
# plt.figure(figsize=(10, 6))
ax[0].plot(x, np.sin(x), color="blue")
ax[0].set_title("sin(x)")
ax[0].set_xlim(0, 2 * np.pi)
ax[0].set_ylim(-1, 1)
ax[0].set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax[0].set_yticks([-1, -0.5, 0, 0.5, 1])
ax[0].set_xticklabels(["0", "π/2", "π", "3π/2", "2π"], fontsize=10)
ax[0].grid(True, linestyle="--", color="gray")
ax[0].xaxis.set_minor_locator(tck.MultipleLocator(np.pi / 8))
ax[0].yaxis.set_minor_locator(tck.MultipleLocator(0.1))
ax[0].minorticks_on()

ax[1].plot(x, np.cos(x), color="red")
ax[1].set_title("cos(x)")
ax[1].set_xlim(0, 2 * np.pi)
ax[1].set_ylim(-1, 1)
ax[1].set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax[1].set_yticks([-1, -0.5, 0, 0.5, 1])
ax[1].set_xticklabels(["0", "π/2", "π", "3π/2", "2π"], fontsize=10)
ax[1].grid(True, linestyle="--", color="gray")
ax[1].xaxis.set_minor_locator(tck.MultipleLocator(np.pi / 8))
ax[0].yaxis.set_minor_locator(tck.MultipleLocator(0.1))
ax[1].minorticks_on()

plt.tight_layout()
plt.show()

# 👉🏻 Why to use loop ? and how ?
# For this example, we have to do like ax[0,0] ax[0,1].... that is too lengthy
fig, ax = plt.subplots(2, 2, figsize=(8, 6))

x = np.linspace(0, 2 * np.pi, 100)
functions = [np.sin, np.cos, np.tan, np.exp]

for a, func in zip(ax.flat, functions):
    a.plot(x, func(x))
    a.set_title(func.__name__)
    a.grid(True)

plt.tight_layout()
plt.show()

# Using .ravel() -> .ravel() returns a NumPy array, .flat returns an iterator. Both work for this purpose.
fig, ax = plt.subplots(2, 2, figsize=(8, 6))
for a, func in zip(ax.ravel(), functions):
    a.plot(x, func(x))
    a.set_title(func.__name__)
    a.grid(True)

fig.suptitle("Multiple Subplots Example", fontsize=16, fontweight="bold")
# Adds one title for the whole figure, not individual subplots.
fig.text(0.5, 0.04, "Common X-axis Label", ha="center", fontsize=12)
fig.text(0.04, 0.5, "Common Y-axis Label", va="center", rotation="vertical", fontsize=12)
# Common x/y labels
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.4, wspace=0.4)
# left, right, top, bottom → control figure margins
# hspace → vertical space between subplots
# wspace → horizontal space between subplots
# plt.tight_layout()

fig.legend(["sin", "cos", "tan"], loc="upper right")
# Adding a legend for all subplots
plt.show()

# 👉🏻 Why this is better than plt.subplot()?
# Clear separation → fig and ax[i] instead of relying on index positions.
# Easy to loop → For many subplots, can loop over ax.flat.
# More control → Can set titles, labels, grids individually without calling plt.subplot() multiple times.


# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick recap:
- Multiple lines in one figure: use repeated plt.plot() calls with labels, colors, linestyles.
- plt.subplot(): create subplot grids, set titles, labels, limits individually.
- plt.subplots(): modern approach, returns fig and ax objects for more control.
- sharex/sharey: share axis limits/ticks across subplots.
- Looping with ax.flat or ax.ravel(): efficiently customize many subplots.
- plt.tight_layout(): automatically adjust subplot spacing.
- plt.subplots_adjust(): manually control subplot margins and spacing.
- fig.suptitle(), fig.text(): add global titles and axis labels.
- fig.legend(): add a legend for all subplots.
"""