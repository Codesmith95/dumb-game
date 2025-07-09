# logger.pu
# writes logs to the console and saves them to a file

from datetime import datetime
import platform
import psutil
import os

# Does the backbone of the work
def main():
	date = str(datetime.now())
	logName = createLogName(date)
	createLog(logName)

# Creates a new log with the system date
def createLogName(date):
	name = "log_" + date[:10] + ".log"
	return name

# Creates a new log file and writes all of the info to it
def createLog(filename):
	# parses system RAM info
	ram = str(round(psutil.virtual_memory().total / (1024.0 **3))) + " GB"
	# gets raw date
	rawDate = str(datetime.now())
	# parses date
	date = rawDate[:10]
	# open/create the log file
	log = open("logs/" + filename, "w")

	print("Logging...")

  # Writes log lines to the file
	log.write("---- Running program ---\n")
	log.write("------ " + date + " ------\n\n")
	log.write("System: " + platform.platform()[:10] + "\n")
	log.write("Python Version: " + platform.python_version() + "\n")
	log.write("Processor Architecture: " + str(platform.processor()) + "\n")
	log.write("RAM: " + ram + "\n")



main()