import wave
import numpy as np
import sys
from matplotlib import pyplot as plt

# Open the audio file
wav = wave.open('relaxing_guitar_loop.wav', "r")

# Check if the audio is stereo (2 channels)
if wav.getnchannels() == 2:
    print("Stereo channel is not supported. Only mono is supported.")
    sys.exit(0)

# Read the raw audio data
raw = wav.readframes(-1)
raw = np.frombuffer(raw, dtype="int16")

# Get sample rate (frames per second)
sample_rate = wav.getframerate()

# Generate time axis values
_time = np.linspace(0, len(raw) / sample_rate, num=len(raw))

# Plot the waveform
plt.title("Audio Wave")
plt.plot(_time, raw, color="blue")
plt.ylabel("Amplitude")
plt.xlabel("Time [s]")
plt.show()
