from model.Livro import Livro
from model.usuario import Usuario
from model.biblioteca import Biblioteca
from control.ControllerLivro import Controllerlivro

livro = Livro("A metamorfose", "Franz Kafka", "Ficção/Critica", 123)

controladora = Controllerlivro()
controladora.atualizarlivro("Agatha")