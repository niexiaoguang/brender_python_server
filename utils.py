import settings
import logging
import time
# def init():

# 	logFileName  = settings.logFilePath + str(int(time.time())) + '.log'
# 	if(settings.logLevel == 'debug'):
# 		logging.basicConfig(filename=logFileName,
# 							level=logging.DEBUG,
# 							format='%(asctime)s:%(levelname)s:%(message)s')

# 	else:
# 		logging.basicConfig(filename=logFileName,
# 							level=logging.DEBUG,
# 							format='%(asctime)s:%(levelname)s:%(message)s')

# 	# set log file


def initLogger():
	if settings.debugMode:
		logging.debug(info)



if __name__ != '__main__':

