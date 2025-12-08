# 3. MATPLOTLIB
import matplotlib.pyplot as plt
import numpy as np

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

plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title("Annotated Sine Wave")

plt.annotate('Peak',
             xy=(np.pi/2, 1),
             xytext=(2, 1.3),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.text(7, -0.9, 'spot!', fontsize=10, color='blue')
plt.show()