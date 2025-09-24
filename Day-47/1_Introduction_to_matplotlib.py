"""
📌 Matplotlib – Step 1 (Introduction to matplotlib)

This file covers:
    - Creating a basic line plot using plt.plot()
    - Adding title, x and y labels
    - Customizing line style, color, marker, linewidth, markerfacecolor, markeredgecolor
    - Saving figure as PNG and PDF
    - Listing all possible options for quick reference

📝 Summary:
    - plt.plot(x, y) → creates a line plot
    - plt.title(), plt.xlabel(), plt.ylabel() → set plot title and axis labels
    - plt.grid(True) → show grid
    - plt.legend() → show legend
    - plt.savefig("file.png") → save figure
    - Line customization options: color, linestyle, linewidth
    - Marker customization: marker, markersize, markerfacecolor, markeredgecolor
"""

import matplotlib.pyplot as plt

# =====================================================
# =============-===== SAMPLE DATA =====================
# =====================================================
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

# =====================================================
# ==================== BASIC PLOT =====================
# =====================================================
plt.plot(x, y)  # Basic line plot
plt.title("Basic Line Plot")
plt.xlabel("X-axis Values")
plt.ylabel("Y-axis Values")
# plt.grid(True)

# Grids,
# plt.grid(True)                     # Default grid (solid lines)
# plt.grid(False)                    # Turns off the grid
# plt.grid(color='gray')             # Change grid color
# plt.grid(linestyle='--')           # Dashed lines
# plt.grid(linewidth=0.5)            # Thinner lines
# plt.grid(alpha=0.7)                # Transparency (0.0 to 1.0)
# plt.grid(True, which='both')       # Show grid for major + minor ticks

plt.show()

# =====================================================
# ================== CUSTOMIZED LINE ==================
# =====================================================
plt.plot(
    x, y,
    color='blue',  # Line color
    linestyle='--',  # Dashed line
    linewidth=2,  # Line thickness
    marker='o',  # Marker shape
    markersize=8,  # Marker size
    markerfacecolor='yellow',  # Marker fill color
    markeredgecolor='red',  # Marker border color
    label='My Custom Line'  # Legend label
)
plt.title("Customized Line Plot")
plt.xlabel("X-axis Values")
plt.ylabel("Y-axis Values")
plt.grid(True)
plt.legend()
plt.show()

# =====================================================
# =================== SAVE FIGURE =====================
# =====================================================
plt.plot(x, y, color='blue', linestyle='--', marker='o')
plt.savefig("custom_line_plot.png", dpi=300)
plt.savefig("custom_line_plot.pdf", dpi=300)

# =====================================================
# =================== CHEAT SHEET =====================
# =====================================================
"""
Line Styles (linestyle):
    '-'    → solid line
    '--'   → dashed line
    '-.'   → dash-dot line
    ':'    → dotted line

Markers (marker):
    'o' → circle
    's' → square
    '^' → triangle up
    'v' → triangle down
    'x' → cross
    '+' → plus
    '*' → star
    'D' → diamond
    'p' → pentagon
    'H' → hexagon
    '.' → point

Colors (color):
    Short names → 'b','g','r','c','m','y','k'
    Full names → 'blue','green','red','cyan','magenta','yellow','black'
    Hex codes → '#FF5733','#33FF57','#3357FF'

Marker Customizations:
    markerfacecolor / mfc → fill color
    markeredgecolor / mec → border color
    markersize / ms → size

Other Options:
    linewidth / lw → thickness of the line
    alpha → transparency (0.0 to 1.0)
    label → legend text
"""

# =====================================================
# =================== QUICK RECAP =====================
# =====================================================

""" 📝 Quick Recap:
- plt.plot(x, y) → create a line plot
- plt.title(), plt.xlabel(), plt.ylabel() → set title and axis labels
- plt.grid(True) → show grid, customizable with color, linestyle, linewidth, alpha
- color, linestyle, linewidth, alpha → line customizations
- marker, markersize, markerfacecolor, markeredgecolor → marker customizations
- plt.legend() → show legend using label
- plt.savefig("file.png"/"file.pdf", dpi=300) → save figure
"""
