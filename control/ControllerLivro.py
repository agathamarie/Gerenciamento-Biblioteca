from model.Livro import Livro
from config.database import Database

class Controllerlivro():
    def __init__(self):
        self.bd = Database("Localhost","root", "","biblioteca")

    def cadastarlivro(self):
        self.bd.conectar()
        self.bd.cursor.execute(self.livro.create())
        self.bd.conexao.commit()
        self.bd.desconectar()

    def procurarlivro(self):
        self.bd.conectar()
        self.bd.cursor.execute(self.livro.read())
        self.bd.conexao.commit()
        self.bd.desconectar()

    def atualizarlivro(self, novotitulo):
        self.bd.conectar()
        self.bd.cursor.execute(self.livro.update(novotitulo))
        self.bd.conexao.commit()

    def deletarlivro(self):
        self.bd.conectar()
        self.bd.cursor.execute(self.livro.delete())
        self.bd.conexao.commit()