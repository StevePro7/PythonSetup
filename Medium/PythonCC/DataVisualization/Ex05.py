# 05. Analyzing Audio Frequencies
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import requests
from io import BytesIO

# URL of the audio file
audio_url = "https://github.com/schreibfaul1/ESP32-audioI2S/raw/master/additional_info/Testfiles/Pink-Panther.wav"

# Fetch the audio file from the URL
response = requests.get(audio_url)
if response.status_code == 200:
    audio_data = BytesIO(response.content)
else:
    raise Exception(f"Failed to fetch audio file. HTTP Status Code: {response.status_code}")

# Read the audio file
sample_rate, audio_data = wavfile.read(audio_data)

# Convert to mono if stereo
if audio_data.ndim > 1:
    audio_data = np.mean(audio_data, axis=1)

# Perform FFT to get frequency domain
frequencies = np.fft.rfftfreq(len(audio_data), d=1/sample_rate)
fft_magnitude = np.abs(np.fft.rfft(audio_data))

# Plot the frequency spectrum
plt.figure(figsize=(10, 6))
plt.plot(frequencies, fft_magnitude)
plt.title("Frequency Spectrum of Pink Panther Audio")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()