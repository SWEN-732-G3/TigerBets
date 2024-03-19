from dataclasses import dataclass

from ..db_utils import *


def rebuild_user_tables():
    exec_sql_file("src/db/sql/user.sql")


def populate_user_table():
    exec_sql_file("data/populate_user.sql")


def recreate_user_table():
    """
    recreate user table if need
    """
    rebuild_user_tables()
    populate_user_table()


def init_user_table(force_rebuild=False):
    """
    init user table
    """
    if force_rebuild:
        recreate_user_table()
    else:
        try:
            get_user_by_username("test")
        except psycopg2.errors.UndefinedTable:
            recreate_user_table()


class User:
    """
    class for user
    """
    def __init__(self, username: str, password: str, full_name: str, email: str, is_deleted: bool = False):
        """
        constructor
        :param username:
        :param password:
        :param is_admin:
        """
        if username is None or password is None or full_name is None or email is None:
            raise ValueError

        self.username = username.strip()
        self.password = password.strip()
        self.full_name = full_name.strip()
        self.email = email.strip()
        self.is_deleted = is_deleted

        if len(self.username) == 0 or len(self.password) == 0 or len(self.full_name) == 0 or len(self.email) == 0:
            raise ValueError

    def to_json(self):
        return {"username": self.username, "full_name": self.full_name, "email": self.email}


def get_user_by_username(username: str) -> int:
    """
    get user by username
    :param username:
    :return: user
    """
    select_sql = "SELECT * FROM users WHERE user_name = %s"
    res = exec_get_one(select_sql, (username,))
    if res is None:
        return res

    return User(res[0], res[1], res[2], res[3], res[4])


def get_user_by_username_password(username: str, password: str) -> User:
    """
    get user by username and password
    :param username:
    :param password:
    :return: user
    """
    user = get_user_by_username(username)
    if user is not None and user.password == password:
        return user


def clear_users():
    sql = "delete from users"
    exec_commit(sql)


def create_user(user: User) -> bool:
    """
    create a new account
    :param user:
    :return: True if create success
    """
    if get_user_by_username(user.username) is not None:
        return False

    insert_sql = """
        insert into users (user_name, password, full_name, email, is_deleted) VALUES (%s, %s, %s, %s, %s)
    """
    exec_commit(insert_sql, (user.username, user.password, user.full_name, user.email, user.is_deleted))

    return True


init_user_table()
