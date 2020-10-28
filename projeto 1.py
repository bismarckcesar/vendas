from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro"
)

def excluir():
    linha = listar_produtos.tableWidget.currentRow()
    listar_produtos.tableWidget.removeRow(linha)
    
    cursor = banco.cursor()
    cursor.execute("Select id FROM produtos")
    dados_lidos = cursor.fetchall()
    print(dados_lidos)
    valor_id = dados_lidos[linha][0]
   
    cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))
    

def chamar_telas():
    cliente_tela.show()

def chamar_telas2():
    produtos_tela.show()

#listar clientes cadastrados
def chamar_telas3():
    listar_clientes.show()

    cursor= banco.cursor()
    comando_SQL = "SELECT * FROM clientes "
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    

    listar_clientes.tableWidget.setRowCount(len(dados_lidos))
    listar_clientes.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0,3):
            listar_clientes.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

#listar produtos cadastrados
def chamar_telas4():
    listar_produtos.show()
    cursor= banco.cursor()
    comando_SQL = "SELECT * FROM produtos "
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    

    listar_produtos.tableWidget.setRowCount(len(dados_lidos))
    listar_produtos.tableWidget.setColumnCount(4)
    
    for i in range(0, len(dados_lidos)):
        for j in range(0,4):
            listar_produtos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

#função da segunda tela    
def botoes_produtos():
    linha1 = produtos_tela.lineEdit.text()
    linha2 = produtos_tela.lineEdit_2.text()
    linha3 = produtos_tela.lineEdit_3.text()
    cursor= banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco) VALUES (%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    #banco.close()
    produtos_tela.lineEdit.setText("")
    produtos_tela.lineEdit_3.setText("")
    produtos_tela.lineEdit_2.setText("")

def botoes_clientes():
    linha1 = cliente_tela.lineEdit.text()
    linha2 = cliente_tela.lineEdit_3.text()
    linha3 = cliente_tela.lineEdit_2.text()
    cursor= banco.cursor()
    comando_SQL = "INSERT INTO clientes (nome,cpf,telefone) VALUES (%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    #banco.close()
    cliente_tela.lineEdit.setText("")
    cliente_tela.lineEdit_3.setText("")
    cliente_tela.lineEdit_2.setText("")


   
#arquivos das telas
app=QtWidgets.QApplication([])
tela_inicial=uic.loadUi("tela_inicial.ui")
cliente_tela=uic.loadUi("cliente_tela.ui")
produtos_tela=uic.loadUi("produtos_tela.ui")
listar_clientes=uic.loadUi("listar_clientes.ui")
listar_produtos=uic.loadUi("listar_produtos.ui")
#chamando telas principais
tela_inicial.pushButton.clicked.connect(chamar_telas)
tela_inicial.pushButton_2.clicked.connect(chamar_telas2)

#telas secundarias 
cliente_tela.pushButton.clicked.connect(botoes_clientes)
cliente_tela.pushButton_2.clicked.connect(chamar_telas3)
produtos_tela.pushButton.clicked.connect(botoes_produtos)
produtos_tela.pushButton_2.clicked.connect(chamar_telas4)
listar_produtos.pushButton.clicked.connect(excluir)




tela_inicial.show()
app.exec()
