from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from utility.log import Logger_T, logging
from views.mainWindow.autoGen_mainWindow import Ui_mainWindow_autoGen_T
from PySide6.QtWidgets import QMainWindow


class mainWindow_init_T(QMainWindow,Ui_mainWindow_autoGen_T):
    def __init__(self):
        super().__init__()
        self.__log = Logger_T()
        self.__log.log(message="Initializing [mainWindow_init_T]", level=logging.INFO)
        self.setupUi(self)
        self.__addWidget()


    def __addWidget(self):
        pass