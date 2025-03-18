from utility.log import Logger_T, logging
from views.mainWindow.autoGen_mainWindow import Ui_mainWindow_autoGen_T
from PySide6.QtWidgets import QMainWindow

import pandas as pd
from lightweight_charts.widgets import QtChart


class mainWindow_init_T(QMainWindow,Ui_mainWindow_autoGen_T):
    def __init__(self):
        super().__init__()
        self.__log = Logger_T()
        self.__log.log(message="Initializing [mainWindow_init_T]", level=logging.INFO)
        self.setupUi(self)
        self.__addWidget()


    def __addWidget(self):
        self.resize(1920, 1080)
        self.chart = QtChart(self)
        self.chart.time_scale(right_offset = 10)
        self.df = pd.read_csv(r'C:\Users\hoang\Documents\WorkDir\CandleChart\data\ohlcv.csv')
        self.layoutTab1.addWidget(self.chart.get_webview())
        self.chart.set(self.df)
