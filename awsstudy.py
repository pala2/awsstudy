import os
import sys
import getopt
import sqlQueryTool

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hu:p:")
	except getopt.GetoptError:
		print "No input options, exiting"
		os._exit(1)

	for opt, arg in opts:
	    if opt == '-h':
			print 'awsstudy.py -p <password>'
			os._exit(1)
	    elif opt == '-p':
	    	dbPassword = arg

	query = sqlQueryTool.sqlQueryTool()
	query.connect(dbPassword)

	query.close()
	
if __name__ == '__main__':
	main(sys.argv[1:])
