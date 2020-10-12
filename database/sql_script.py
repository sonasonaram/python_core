from database.mysql_lib import dbconnect

db = dbconnect("root", "root", "hemanth_db")

# db.create_table("student", {"name VARCHAR(100)", "roll INTEGER", "address VARCHAR(200)"})

# db.insert_data_into_table("student", {"name" : "vishal","roll" : "10","address" : "Bangalore"} )
# db.insert_data_into_table("student", {"name" : "ram","roll" : "10","address" : "Delhi"} )
# db.insert_data_into_table("student", {"name" : "sharma","roll" : "10","address" : "Calcutta"} )
# db.insert_data_into_table("student", {"name" : "rahul","roll" : "10","address" : "Chennai"} )
# db.insert_data_into_table("student", {"name" : "lakshmi","roll" : "10","address" : "Lucknow"} )

db.see_table_data("student")