from sqlalchemy import create_engine,text
engine = create_engine("mysql+mysqlconnector://sql12647992:Cl3Vqb4Y4S@sql12.freesqldatabase.com/sql12647992") 
# connect_args={
#   'ssl':{  
#     "ssl_ca":"/etc/ssl/cert.pem"
#             }
#          }
                       
connection = engine.connect()
result = connection.execute("SELECT * FROM sql12647992")  

# with engine.connect() as conn:
#   result=conn.execute(text("select* from jobs"))
#   print(result.all())