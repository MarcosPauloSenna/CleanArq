from typing import List
from src.domain.models.users import Users


class UsersRepositoriySpy:

    def __init__(self) -> None:
        self.insert_user_attibutes = {}
        self.select_user_attibutes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attibutes["first_name"] = first_name
        self.insert_user_attibutes["last_name"] = last_name
        self.insert_user_attibutes["age"] = age

    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_attibutes["first_name"] = first_name
        return[
            Users(23, first_name, 'last', 43),
            Users(23, first_name, 'last_2', 12)
        ]
