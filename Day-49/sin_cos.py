import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tck

# Generate data
x = np.linspace(0, 2 * np.pi, 500)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(10, 6))
# Plot sin(x) and cos(x) with different styles
ax.plot(x, y_sin, label="sin(x)", color="blue", linestyle="-", linewidth=2)
ax.plot(x, y_cos, label="cos(x)", color="red", linestyle="--", linewidth=2)

ax.set_title("Sin and Cos Waves with Styling", fontsize=16, fontweight="bold")
ax.set_xlabel("x (radians)", fontsize=12)
ax.set_ylabel("Amplitude", fontsize=12)

# Legend
ax.legend(loc="upper right", fontsize=10)

# Axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.2, 1.2)

# Custom ticks
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"], fontsize=10)
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.yaxis.set_minor_locator(tck.MultipleLocator(0.1))  # Minor ticks every 0.1
ax.xaxis.set_minor_locator(tck.MultipleLocator(np.pi/8))  # Minor ticks every π/8

# Grid customization
ax.grid(which="major", color="gray", linestyle="-", linewidth=0.8)
ax.grid(which="minor", color="lightgray", linestyle="--", linewidth=0.5)

# Annotation
ax.annotate("Peak of sin(x)", xy=(np.pi/2, 1), xytext=(np.pi/2+0.5, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Tight layout for better spacing
plt.tight_layout()

# Show plot
plt.show()