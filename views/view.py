from typing import override
from views.view_abstract import View_Abstract_T
from views.mainWindow.mainWindow_T import mainWindow_T
from utility.log import Logger_T,logging

class view_T(View_Abstract_T):
	def __init__(self):
		super().__init__()
		self.__log=Logger_T()
		self.__log.log(message="Initializing [view_T]", level=logging.INFO)
		self.__mainWindow = mainWindow_T()
	@override
	def run(self):
		self.__log.log(message="Show [mainWindow]", level=logging.INFO)
		self.__mainWindow.show()
