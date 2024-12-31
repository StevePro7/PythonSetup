# 01. Analyzing Daily Temperatures
import numpy as np

# Simulated daily temperatures (in Celsius) for a month
temperatures = np.array([22, 21, 23, 25, 26, 27, 24, 22, 20, 19, 23, 24, 28, 30])

# Calculate basic statistics
mean_temp = np.mean(temperatures)
median_temp = np.median(temperatures)
std_dev_temp = np.std(temperatures)

# Round to two decimal places
mean_temp_rounded = round(mean_temp, 2)
median_temp_rounded = round(median_temp, 2)
std_dev_temp_rounded = round(std_dev_temp, 2)

# Convert to Fahrenheit (no rounding)
mean_temp_f = (mean_temp * 9/5) + 32
median_temp_f = (median_temp * 9/5) + 32
std_dev_temp_f = (std_dev_temp * 9/5) + 32

# Convert to Fahrenheit (rounded)
mean_temp_f_rounded = round(mean_temp_f, 2)
median_temp_f_rounded = round(median_temp_f, 2)
std_dev_temp_f_rounded = round(std_dev_temp_f, 2)

# Print the results
print("### Actual Numbers ###")
print(f"Mean Temperature (C): {mean_temp}")
print(f"Median Temperature (C): {median_temp}")
print(f"Standard Deviation (C): {std_dev_temp}")

print("\n### Rounded Numbers ###")
print(f"Mean Temperature (C, Rounded): {mean_temp_rounded}")
print(f"Median Temperature (C, Rounded): {median_temp_rounded}")
print(f"Standard Deviation (C, Rounded): {std_dev_temp_rounded}")

print("\n### Fahrenheit Conversion ###")
print(f"Mean Temperature (F): {mean_temp_f} (Rounded: {mean_temp_f_rounded})")
print(f"Median Temperature (F): {median_temp_f} (Rounded: {median_temp_f_rounded})")
print(f"Standard Deviation (F): {std_dev_temp_f} (Rounded: {std_dev_temp_f_rounded})")