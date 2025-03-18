import sys
from PySide6.QtWidgets import QApplication
from utility.log import Logger_T, logging
from views.view import view_T


class candleApp_T:
	def __init__(self):
		self.__log = Logger_T()
		self.__log.log(message="Initializing [candleApp]", level=logging.INFO)
		self.qtApplication = QApplication(sys.argv)
		self.__view = view_T()
		self.__view.run()
		self.qtApplication.exec_()

	def run(self):
		pass