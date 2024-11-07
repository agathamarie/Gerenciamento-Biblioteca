class Livro():
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self. autor = autor
        self. genero = genero
        self. cod_livro = cod_livro

        self.status = "Disponivel"

    def create(self):
        return f'INSERT INTO livro (titulo, autor, genero, cod_livro) VALUES ("{self.titulo}", "{self.autor}", "{self.genero}", {self.cod_livro});'
    
    def read(self):
        return f'SELECT * FROM livro where cod_livro = {self.cod_livro};'
    
    def update(self, novotitulo):
        return f'UPDATE livro SET titlo = "{novotitulo}" WHERE cod_livro = {self.cod_livro};'
    
    def delete(self):
        return f'DELETE FROM livro where cod_livro = {self.cod_livro};'