import psycopg2 as ps
import pprint as pp

class sqlQueryTool:
	connection  = None
	cursor = None

	def connect(self,password):
		try:
			self.connection=ps.connect(password= password, sslmode='require')
			print "Success getting connection!"
			pp.pprint(self.connection)
			self.cursor = self.connection.cursor()
		except ps.Error as e:
			print "Connection Error:",e
			print "PgCode:",e.pgcode,"PgError",e.pgerror
			print "Dagnostics:",e.diag
			out = {}
			for prop in dir(e.diag):
				if not re.match(r'__', prop):
					out[prop] = getattr(e.diag, prop)
			pp.pprint(out)
			os._exit(1)

	def close(self):
		if self.cursor is not None:
			print "Closing Cursor"
			self.cursor.close()
		if self.connection is not None:
			print "Closing Connection"
			self.connection.close()

	def getTableNames(self):
		queryListAllTables = ("SELECT table_schema, table_name "
			"FROM information_schema.tables "
			"WHERE table_schema = 'public' "
			"ORDER BY table_schema,table_name;")
		self.cursor.execute(queryListAllTables)
		return self.cursor.fetchall()

	def getColumnNames(self, tablename):
		queryShowColumnNames = ("SELECT column_name "
			"FROM information_schema.columns "
			"WHERE table_name = (%s);")
		self.cursor.execute(queryShowColumnNames, [tablename])
		return self.cursor.fetchall()	

	def getFirstAccounts(self, nbrRows):
		queryGetFirstLines = ("SELECT * FROM account LIMIT (%s);")
		data = (nbrRows,)
		self.cursor.execute(queryGetFirstLines, data)
		return self.cursor.fetchall()

	def getFirstAccountTransactions(self, nbrRows):
		queryGetFirstLines = ("SELECT * FROM account_tx LIMIT (%s);")
		data = (nbrRows,)
		self.cursor.execute(queryGetFirstLines, data)
		return self.cursor.fetchall()		
	
