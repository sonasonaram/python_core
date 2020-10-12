import mysql.connector


class dbconnect:

    def __init__(self, username, password, databaseName):
        try:
            self.mydb = mysql.connector.connect(host="localhost",user=username,password=password,database=databaseName)
        except:
            self.mydb = mysql.connector.connect(host="localhost", user=username, password=password)
            print("The given DB does not exist, just connected to the DB Engine")

    def list_databases(self):
        c = self.mydb.cursor()
        c.execute("SHOW DATABASES;")

        for db in c:
            print(db)

    def create_database(self, dbName):
        try:
            c = self.mydb.cursor()
            c.execute("CREATE DATABASE " + dbName)
        except:
            print("DB with the given name already exists")

    def create_table(self, tableName, params):
        query = "CREATE TABLE " + tableName + " ("
        for param in params:
            query = query + param + ", "
        query = query[0:len(query)-2]
        query = query + ")"
        try:
            c = self.mydb.cursor()
            c.execute(query)
        except:
            print("CREATE TABLE FAILED")

    def insert_data_into_table(self, tableName, values):
        query = "INSERT INTO " + tableName + " ("
        values_list = []
        for key in values.keys():
            query = query + key + ", "
            values_list.append(values[key])
        query = query[0:len(query)-2]
        query = query + ") values ("

        for value in values_list:
            try:
                i_val = (int)(value)
                query = query + value + ", "
            except:
                query = query + '"' + value + '"' + ", "

        query = query[0:len(query) - 2]
        query = query + ")"

        print(query)

        try:
            c = self.mydb.cursor()
            c.execute(query)
            self.mydb.commit()
        except:
            print("INSERT DATA FAILED")


    def see_table_data(self, tableName):
        query = "Select * from " + tableName;
        try:
            c = self.mydb.cursor()
            c.execute(query)
            for row in c:
                print(row)
        except:
            print("NO DATA FOUND")
