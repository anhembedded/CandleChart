from candleApp import candleApp_T
from utility.log import Logger_T, logging

if __name__ == '__main__':
	candleApp = candleApp_T()
	logger = Logger_T()
	logger.log(message="Run [candleApp]", level=logging.INFO)
	candleApp.run()
