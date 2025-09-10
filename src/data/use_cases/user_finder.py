#pylint: disable=no-name-in-module
#pylint: disable=unused-private-member
#pylint: disable=broad-exception-raised
from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserfinderInterface
from src.data.interfaces.user_repository import UsersRepositoriyInterface
from src.domain.models.users import Users


class UserFinder(UserfinderInterface):
    def __init__(self, users_repository : UsersRepositoriyInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name)

        users = self.__search_user(first_name)

        response = self.__format_response(users)

        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception('Nome invalido para a busca')
        if len(first_name) > 18:
            raise Exception('Nome muito grande para a busca')

    def __search_user(self, first_name: str) -> List:
        users = self.__users_repository.select_user(first_name)
        if users ==[]: raise Exception('Usuario nao encontrado')
        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        attributes = []
        for user in users:
            attributes.append({"first_name": user.first_name, "age": user.age}
                              )

            reponse = {
            "type": "Users",
            "count": len(users),
            "attributes": users
        }

        return reponse
