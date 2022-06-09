from scipy.io import wavfile
from IPython.display import Audio
from matplotlib import pyplot as plt

f_name = 'C:\\Users\\RED MERCY\\Desktop\\test\\mic1_open_61902046001136_02_03_22__15_08_47.wav'
fs, wav = wavfile.read(f_name)
print(fs)
plt.plot(wav)
