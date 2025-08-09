from .users_repository import UsersRepositoriy

def test_insert_user():
    mocked_first_name = '01first'
    mocked_last_name = '01last'
    mocked_age = 55

    users_repository = UsersRepositoriy()

    users_repository.insert_user( mocked_first_name, mocked_last_name, mocked_age)
