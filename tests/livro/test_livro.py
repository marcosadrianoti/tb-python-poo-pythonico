from src.livro.livro import Livro


def test_cria_livro():
    livro = Livro("O Hobbit", "J.R.R. Tolkien", 310)
    assert livro.titulo == "O Hobbit"
    assert livro.autor == "J.R.R. Tolkien"
    assert livro.paginas == 310
