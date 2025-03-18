from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from utility.log import Logger_T, logging
from views.mainWindow.mainWindow_init import mainWindow_init_T

class mainWindow_T(mainWindow_init_T):
    def __init__(self):
        super().__init__()
        self.log = Logger_T()
        self.log.log(message="Initializing [mainWindow_T]", level=logging.INFO)
        self.__signalAndSlot()
    def __signalAndSlot(self):
        pass