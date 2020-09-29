from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro"
)

def chamar_telas():
    cliente_tela.show()

def chamar_telas2():
    produtos_tela.show()

#função da segunda tela    
def botoes_produtos():
    linha1 = cliente_tela.lineEdit.text()
    linha2 = cliente_tela.lineEdit_2.text()
    linha3 = cliente_tela.lineEdit_3.text()
    print(linha1)
    print(linha2)
    print(linha3)
    cursor= banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco) VALUES (%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3))
    cursor.execute(comando_SQL,dados)
    banco.commit()

def botoes_clientes():
    linha1 = cliente_tela.lineEdit.text()
    linha2 = cliente_tela.lineEdit_2.text()
    linha3 = cliente_tela.lineEdit_3.text()
    print(linha1)
    print(linha2)
    print(linha3)
    cursor= banco.cursor()
    comando_SQL = "INSERT INTO clientes (nome,cpf,telefone) VALUES (%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3))
    cursor.execute(comando_SQL,dados)
    banco.commit()

app=QtWidgets.QApplication([])
tela_inicial=uic.loadUi("tela_inicial.ui")
cliente_tela=uic.loadUi("cliente_tela.ui")
produtos_tela=uic.loadUi("produtos_tela.ui")
tela_inicial.pushButton.clicked.connect(chamar_telas)
tela_inicial.pushButton_2.clicked.connect(chamar_telas2)

#botão limpar como teste de envio de informações
cliente_tela.pushButton.clicked.connect(botoes_clientes)
produtos_tela.pushButton.clicked.connect(botoes_produtos)


#banco de dados 



tela_inicial.show()
app.exec()
