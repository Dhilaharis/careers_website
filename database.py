from sqlalchemy import create_engine,text
# engine = create_engine("mysql+mysqlconnector://sql12647992:Cl3Vqb4Y4S@sql12.freesqldatabase.com/sql12647992") 
# connect_args={
#   'ssl':{  
#     "ssl_ca":"/etc/ssl/cert.pem"
#             }
#          }
                       
connection = mysql.connect()
result = connection.execute(text("SELECT * FROM users;")) 

 
# async with self.async_engine.connect() as con:
#     query = "SELECT * FROM users;"
#     result = await con.execute(text(query))

# with engine.connect() as conn:
#   result=conn.execute(text("select* from jobs"))
#   print(result.all())
# for row in result:
#     print(row)