# 3. MATPLOTLIB
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import alpha

# Subplots - multiple charts in one figure
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# fig, axs = plt.subplots(1, 2, figsize=(10, 4))
# axs[0].plot(x, y1, color='orange')
# axs[0].set_title("Sine Wave")
# axs[1].plot(x, y2, color='purple')
# axs[1].set_title("Cosine Wave")
# plt.suptitle("Sine & Cosine Plots (Side by Side)")
# plt.tight_layout()
#plt.show()

# Customizing styles + themes
plt.style.use('ggplot')
x = np.arange(0, 10, 0.5)
y = x ** 2

# plt.figure(figsize=(6, 4))
# plt.plot(x, y, label='x squared')
# plt.title("Custom Styled Plot")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.legend()
# plt.show()

# Annotations + text on plots
x = np.linspace(0, 10, 100)
y = np.sin(x)

# plt.figure(figsize=(8, 4))
# plt.plot(x, y)
# plt.title("Annotated Sine Wave")
#
# plt.annotate('Peak',
#              xy=(np.pi/2, 1),
#              xytext=(2, 1.3),
#              arrowprops=dict(facecolor='black', arrowstyle='->'))
# plt.text(7, -0.9, 'spot!', fontsize=10, color='blue')
# plt.show()

# Histogram customizations
data = np.random.randn(1000)

# plt.figure(figsize=(6, 4))
# plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.8)
# plt.title("Custom Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.grid(True)
# plt.show()

# Multiple lines on the same plot
x = np.linspace(0, 10, 100)

# plt.figure(figsize=(8, 4))
# plt.plot(x, np.sin(x), label='Sine')
# plt.plot(x, np.cos(x), label='Cosine')
# plt.plot(x, np.tan(x), label='Tangent', alpha=0.5)
#
# plt.ylim(-5, 5)  # Limit y-axis
# plt.title("Multiple Trig Functions")
# plt.legend()
# plt.grid(True)
# plt.show()

# Saving plots as images
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
plt.title("Saving This Plot")
plt.savefig("sine_plot.png", dpi=300)  # High-resolution save
plt.show()
