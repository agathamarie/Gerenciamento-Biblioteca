from model.Livro import Livro
from model.usuario import Usuario

class Biblioteca:
    Acervo:list[Livro] = []

    @staticmethod
    def emprestar(usuario: Usuario, livros: list[Livro]):
        for item in Livro:
            if len(usuario.lista_livros) == usuario.MAX_EMPRESTIMO:
                return
            usuario.pegar_emprestado(item)
            item.emprestar_livro(usuario)

    @staticmethod
    def devolver(usuario: Usuario, livros: list[Livro]):
        for item in Livro:
            if len(usuario.lista_livros) == 0:
                return
            usuario.devolver_emprestado(item)
            item.emprestar_livro(usuario)