#!python3

import logging,datetime,os

def recordTime(logfile):
    
    logging.basicConfig(filename=logfile,format='%(asctime)s %(message)s',level=logging.INFO)
    logging.info('is called.')


today = datetime.date.today()
logPath = 'c:\\var\\log\\python-' + str(today.strftime('%Y%m%d'))
logFile = logPath + '\\weeko1.log'

if not os.path.exists(logPath):
    os.makedirs(logPath)


recordTime(logFile)
