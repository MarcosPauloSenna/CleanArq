#pylint: disable=no-name-in-module
#pylint: disable=unused-private-member
from typing import Dict
from src.domain.use_cases.user_finder import UserFinder as UserfinderInterface
from src.data.interfaces.user_repository import UsersRepositoriyInterface


class UserFinder(UserfinderInterface):
    def __init__(self, users_repository : UsersRepositoriyInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        pass
