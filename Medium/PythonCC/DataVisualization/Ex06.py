# 06. Visualizing Sea Surface Temperatures
import numpy as np
import matplotlib.pyplot as plt

# Simulated realistic SST data (degrees Celsius)
# Warmer temperatures near the equator (-10 to 10 latitude) and cooler near the poles
latitudes = np.linspace(-90, 90, 180)  # 180 latitude points
longitudes = np.linspace(-180, 180, 360)  # 360 longitude points

# Generate SST values based on latitude
sst_data = np.zeros((180, 360))
for i, lat in enumerate(latitudes):
    # Simulate temperature as a function of latitude
    # Warmer near equator, cooler near poles
    equator_temp = 28 - abs(lat) * 0.2  # Base temperature
    sst_data[i, :] = np.random.normal(equator_temp, 1.5, size=360)

# Compute global mean SST
mean_sst = np.mean(sst_data)

# Identify hotspots (SST > 28°C)
hotspots = sst_data > 28

# Visualize the data
plt.figure(figsize=(12, 6))
plt.imshow(sst_data, cmap='coolwarm', extent=[-180, 180, -90, 90], aspect='auto')
plt.colorbar(label="Sea Surface Temperature (°C)")
plt.title(f"Sea Surface Temperature Map (Mean SST: {mean_sst:.2f}°C)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()