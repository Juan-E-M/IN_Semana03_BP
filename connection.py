import mysql.connector
from sqlalchemy import create_engine

def connect():
    conexion = mysql.connector.connect(
    host="172.17.0.2", 
    user="root",       
    password="root",  
    database="sakila"  
    )
    return conexion

    
def define_engine() :
    engine = create_engine('mysql+mysqlconnector://', creator=lambda: connect())
    return engine
