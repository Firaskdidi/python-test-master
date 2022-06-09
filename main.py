import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QVBoxLayout, QPushButton

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from PyQt5.uic import loadUi
from pathlib import Path
from convert import Convert
from plot import Plot
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        loadUi("main.xml", self)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.convasGridLayout.addWidget(self.toolbar)
        self.convasGridLayout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button_sftp.clicked.connect(self.open_sftp)
        self.button_browse.clicked.connect(self.browse)
        self.button_convert.clicked.connect(self.convert)
        self.button_afficher.clicked.connect(self.afficher)

    def browse(self):
        file = QFileDialog.getOpenFileNames(self, 'open file', '', 'log file (*.log)')
        file_path = Path(file[0][0])
        file_name = file[0][0]
        file_type = "distortion"
        if "Level" in file_name:
            file_type = "level"
        if "Steepness" in file_name:
            file_type = "steepness"
        self.file_name.setText(str(file_path))
        self.file_type.setText(str(file_type))

    def convert(self):
        file_path = self.file_name.text()
        convert_type = self.file_type.text()
        if convert_type == "distortion":
            Convert().convert_distortion(file_path)
        if convert_type == "level":
            Convert().convert_level(file_path)
        if convert_type == "steepness":
            Convert().convert_steepness(file_path)

    def open_sftp(self):
        os.system('"C:\\Program Files (x86)\\WinSCP\\WinSCP.exe"')

    def afficher(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        file_path = self.file_name.text()
        convert_type = self.file_type.text()
        if convert_type == "distortion":
            Plot().plot_distortion(ax, file_path)
        if convert_type == "level":
            Plot().plot_level(ax, file_path)
        if convert_type == "steepness":
            Plot().plot_steepness(ax, file_path)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(windows)
    widget.setFixedWidth(1400)
    widget.setFixedHeight(1200)
    widget.show()
    sys.exit(app.exec_())
