import os
import pandas as pd


class Plot:

    def plot_distortion(self, ax, file_path):
        filepath = os.path.abspath(file_path)
        path = os.path.dirname(filepath)
        base = os.path.basename(filepath)
        base = os.path.splitext(base)
        file_path = f"{path}/{base[0]}.xlsx"
        df = pd.read_excel(file_path)
        df.head()
        ax.plot(df['Frequency'], df['Amplitude'], "r", label=' Amplitude en fonction de la fréquence')
        ax.plot(df['Frequency'], df['Upper Limit PASSED'], "g", label=' Upper limit en fonction de la fréquence')
        ax.legend(loc='upper left')

    def plot_level(self, ax, file_path):
        filepath = os.path.abspath(file_path)
        path = os.path.dirname(filepath)
        base = os.path.basename(filepath)
        base = os.path.splitext(base)
        file_path = f"{path}/{base[0]}.xlsx"
        df = pd.read_excel(file_path)
        df.head()
        ax.plot(df['Frequency'], df['Amplitude'], "r", label=' Amplitude en fonction de la fréquence')
        ax.plot(df['Frequency'], df['Upper Limit PASSED'], "g", label=' Upper limit en fonction de la fréquence')
        ax.plot(df['Frequency'], df['Lower Limit PASSED'], "b", label=' Lower limit en fonction de la fréquence')
        ax.legend(loc='lower left')

    def plot_steepness(self, ax, file_path):
        filepath = os.path.abspath(file_path)
        path = os.path.dirname(filepath)
        base = os.path.basename(filepath)
        base = os.path.splitext(base)
        file_path = f"{path}/{base[0]}.xlsx"
        df = pd.read_excel(file_path)
        ax.plot(df['Frequence'], df['Amplitude 1'], label=' Amplitude en fonction de la fréquence')
        ax.plot(df['Frequence'], df['Amplitude 2'], label=' Amplitude en fonction de la fréquence')
        ax.plot(df['Frequence'], df['Amplitude 3'], label=' Amplitude en fonction de la fréquence')
        ax.plot(df['Frequence'], df['Amplitude 4'], label=' Amplitude en fonction de la fréquence')
        ax.plot(df['Frequence'], df['Amplitude 5'], label=' Amplitude en fonction de la fréquence')
        ax.plot(df['Frequence'], df['Amplitude 6'], label=' Amplitude en fonction de la fréquence')
        ax.legend(loc='upper right')
