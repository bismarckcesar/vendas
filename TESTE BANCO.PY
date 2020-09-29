import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_teste"
)
cursor= banco.cursor()
#cursor.execute("CREATE DATABASE python_teste")
cursor.execute("CREATE TABLE clientes (nome VARCHAR(255),telefone INT(11), cpf INT(11))")