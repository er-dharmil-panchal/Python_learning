"""
📌 Matplotlib - Advanced Plots & Exporting

This file covers:
- Grouping data & plotting aggregated results
- Stack plots
- 3D plots
- Contour plots
- Polar plots
- Quiver plots
- Colormaps
- Saving figures to file
- File formats
- DPI & quality
- Exporting to vector formats
- Exporting data

📝 Summary:
- Grouping → summarising data with groupby()
- Stack plots → visualise cumulative datasets
- 3D plots → visualise relationships between three variables
- Contour plots → 2D representation of surface levels
- Polar plots → radial representation for cyclic data
- Quiver plots → vector field visualisation
- Colormaps → add clarity and style to plots
- plt.savefig() → saves figure in multiple formats
- DPI → control image quality
- bbox_inches → tight layout saving
- Exporting data → CSV or JSON
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# =====================================================
# =========== GROUPING & AGGREGATED PLOTTING =========
# =====================================================
# Useful when you want to summarise data before plotting.

np.random.seed(0)
categories = np.random.choice(["A", "B", "C"], size=100)
values = np.random.randn(100)
df = pd.DataFrame({"Category": categories, "Value": values})

grouped = df.groupby("Category").mean()

plt.figure(figsize=(6, 4))
grouped.plot(kind="bar", legend=False, color=["blue", "green", "red"])
plt.title("Mean Value by Category")
plt.ylabel("Mean Value")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

# =====================================================
# =========== STACK PLOTS ============================
# =====================================================
# Great for showing contributions of parts over a range.

x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = np.sin(x) + 0.5
y3 = np.sin(x) + 1

plt.figure(figsize=(8, 4))
plt.stackplot(x, y1, y2, y3, labels=["y1", "y2", "y3"], alpha=0.6)
plt.legend(loc="upper left")
plt.title("Stack Plot Example")
plt.xlabel("X-axis values")
plt.ylabel("Stacked values")
plt.show()

# =====================================================
# =========== 3D PLOTS ================================
# =====================================================
# For visualising relationships between three variables.

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
# can also do like this
# fig, ax = plt.subplots(1, 1, figsize=(8, 6), subplot_kw={"projection": "3d"})

X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)
# Before:
# x is 1D → shape (5,)
# y is 1D → shape (7,)
X, Y = np.meshgrid(X, Y)
# After:
# X.shape == (7, 5)
# Y.shape == (7, 5)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_title("3D Surface Plot")
plt.show()

# =====================================================
# =========== CONTOUR PLOTS ==========================
# =====================================================
# Top-down representation of 3D surfaces.

plt.figure(figsize=(6, 5))
cont = plt.contour(X, Y, Z, levels=20, cmap="coolwarm")
plt.colorbar(cont)
plt.title("Contour Plot Example")
plt.show()

# =====================================================
# =========== POLAR PLOTS ============================
# =====================================================
# Useful for cyclic or radial data.

theta = np.linspace(0, 2 * np.pi, 100)
r = np.abs(np.sin(2 * theta) * np.cos(2 * theta))

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)
ax.plot(theta, r, color="purple")
ax.set_title("Polar Plot Example")
plt.show()

# =====================================================
# =========== QUIVER PLOTS ===========================
# =====================================================
# Vector field visualisation.

x = np.arange(0, 2, 0.2)
y = np.arange(0, 2, 0.2)
X, Y = np.meshgrid(x, y)
U = np.cos(X) * Y
V = np.sin(Y) * X
# Defines the vector components at each grid point:
# U = horizontal (x-direction) component.
# V = vertical (y-direction) component.

plt.figure(figsize=(6, 6))
plt.quiver(X, Y, U, V, color="teal")
plt.title("Quiver Plot Example")
plt.show()
# plt.quiver(X, Y, U, V) draws arrows:
# Base of arrow = (X, Y) grid points.
# Direction & length = (U, V) values.

# =====================================================
# =========== COLORMAPS ==============================
# =====================================================
# Add clarity and style without extra labels.

plt.figure(figsize=(6, 4))
for i, cmap in enumerate(["viridis", "plasma", "inferno"]):
    plt.plot(x, np.sin(x + i), label=cmap, color=plt.get_cmap(cmap)(0.6))
plt.legend()
plt.title("Colormap Examples")
plt.show()
"""
| Colormap    | Color Shade Description                 |
| ----------- | --------------------------------------- |
| viridis     | Dark purple → blue → green → yellow     |
| plasma      | Dark purple → magenta → orange → yellow |
| inferno     | Black → dark red → orange → yellow      |
| magma       | Black → deep purple → red → orange      |
| cividis     | Dark blue → turquoise → light yellow    |
"""

# =====================================================
# ============== SAVING & EXPORTING ===================
# =====================================================


# =====================================================
# =========== SIMPLE FIGURE SAVING ===================
# =====================================================
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label="sin(x)")
plt.title("Simple Figure")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

# Save figure
plt.savefig("simple_figure.png")  # PNG format
plt.savefig("simple_figure.jpg", quality=95)  # JPG format
plt.savefig("simple_figure.svg")  # Vector format
plt.savefig("simple_figure.pdf")  # PDF format
plt.show()

# =====================================================
# =========== DPI & QUALITY CONTROL =================
# =====================================================
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="sin(x)")
plt.title("High DPI Figure")
plt.legend()
plt.grid(True)

plt.savefig("high_dpi_figure.png", dpi=300)  # High resolution
plt.show()

# =====================================================
# =========== EXPORTING WITH TIGHT LAYOUT ===========
# =====================================================
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="sin(x)")
plt.title("Tight Layout Export")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("tight_layout_figure.png", bbox_inches="tight")
plt.show()

# =====================================================
# =========== EXPORTING DATA =========================
# =====================================================
data = pd.DataFrame({"X": x, "Y": y})
data.to_csv("plot_data.csv", index=False)  # Save data as CSV
data.to_json("plot_data.json", orient="records")  # Save as JSON

print("Export complete: figure images and data files saved.")

# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

"""
Quick recap:
- Grouping & aggregated plotting: summarise data with groupby(), use bar plots for categories.
- Stack plots: visualise cumulative contributions over a range.
- 3D plots: visualise relationships between three variables using surface plots.
- Contour plots: top-down representation of 3D surfaces.
- Polar plots: radial representation for cyclic data.
- Quiver plots: visualise vector fields.
- Colormaps: add clarity & style to plots with different colour schemes.
- plt.savefig(): save figures in PNG, JPG, SVG, PDF formats.
- DPI: control figure resolution and quality.
- bbox_inches='tight': save figures without extra margins.
- Exporting data: save plotting data as CSV or JSON files.
"""
