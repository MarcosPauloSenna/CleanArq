from typing import List
from abc import ABC, abstractmethod
from src.domain.models.users import Users


#pylint: disable=no-self-argument
class UsersRepositoriyInterface(ABC):

    @abstractmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None: pass


    @abstractmethod
    def select_user(cls, fist_name: str) -> List[Users]: pass 