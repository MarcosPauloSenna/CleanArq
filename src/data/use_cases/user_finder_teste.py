from src.infra.db.tests.user_repository import UsersRepositoriySpy
from .user_finder import UserFinder


def test_find():
    first_name = 'meuNome'

    repo = UsersRepositoriySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)


    assert repo.select_user_attibutes["first_name"] == first_name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []


def test_find_error_in_valid_name():
    first_name = 'meuNome123'

    repo = UsersRepositoriySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Nome invalido para a busca"

def test_find_error_in_long_name():
    first_name = 'meuNomesdfgsdfdfsdfasasdadfsdfasdasdfasasdasdasdasdasdas'

    repo = UsersRepositoriySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Nome muito grande para a busca"

def test_find_error_user_not_found():
    class UserRepositoryError(UsersRepositoriySpy):
        def select_user(self, first_name: str):
            return []

    first_name = 'meuNome'

    repo = UserRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Usuario nao encontrado"
