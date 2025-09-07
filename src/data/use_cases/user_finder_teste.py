from src.infra.db.repositories.users_repository import UsersRepositoriy
from .user_finder import UserFinder


def test_find():
    repo = UsersRepositoriy
    user_finder = UserFinder(repo)

