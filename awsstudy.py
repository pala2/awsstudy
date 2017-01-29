import psycopg2 as ps
import pprint as pp
import numpy as np
import os
import sys
import getopt

dbHost = 'examplecluster.c9jdxebmx23p.us-west-2.redshift.amazonaws.com'
dbPort = '5439'
dbName = 'dev'

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hu:p:")
	except getopt.GetoptError:
		print "No input options, exiting"
		os._exit(1)

	for opt, arg in opts:
	    if opt == '-h':
			print 'awsstudy.py -u <username> -p <password>'
			os._exit(1)
	    elif opt == '-u':
	    	dbUser = arg
	    elif opt == '-p':
	    	dbPassword = arg

	#Connect to Redshift
	#Driver={Amazon Redshift (x64)}; Server=examplecluster.c9jdxebmx23p.us-west-2.redshift.amazonaws.com; Database=dev; UID=username; PWD=insert_your_master_user_password_here; Port=5439
	try:
		con=ps.connect(dbname= dbName, host=dbHost, port= dbPort, user= dbUser, password= dbPassword)
		print "Success getting connection!"
		pp.pprint(con)
	except ps.Error as e:
		print "Connection Error:",e.pgerror
		os._exit(1)

	#Get cursor 
	cur = con.cursor()

	#Query for all tables
	queryListAllTables = ("SELECT table_schema, table_name "
		"FROM information_schema.tables "
		"WHERE table_schema = 'public' "
		"ORDER BY table_schema,table_name;")

	#query = "SELECT * FROM pg_table_def WHERE tablename = 'sales';"
	cur.execute(queryListAllTables)
	pp.pprint(cur.fetchall())

	#queryExample = ("SELECT firstname, lastname, total_quantity "
	#		"FROM   (SELECT buyerid, sum(qtysold) total_quantity "
	#        "FROM  sales "
	#        "GROUP BY buyerid "
	#        "ORDER BY total_quantity desc limit 10) Q, users "
	#		"WHERE Q.buyerid = userid "
	#		"ORDER BY Q.total_quantity desc;")		

	#cur.execute(queryExample)
	#queryResults = cur.fetchall()
	#data = np.array(queryResults)
	#pp.pprint(data)

	cur.close()
	con.close()

if __name__ == '__main__':
	main(sys.argv[1:])
