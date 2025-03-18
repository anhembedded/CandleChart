from abc import abstractmethod
from PySide6.QtWidgets import QMainWindow, QWidget
from utility.log import Logger_T, logging

class View_Abstract_T(QWidget):
    def __init__(self):
        super().__init__()
        self.__log = Logger_T()
        self.__log.log(message="Initializing [ViewAbstract_T]", level=logging.INFO)

    @abstractmethod
    def run(self):
        pass

