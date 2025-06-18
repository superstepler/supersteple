class User:
    def __init__(self, Login, Password):
        self.Login = Login
        self.Password = Password

Users = [User("login_1", "1111"), User("login_2", "2222"), User("login_3", "3333"), User("login_4", "4444"), User("login_5", "5555")]

def users(Users):
    Login = input("Введите логин: ")
    Password = input("Введите пароль: ")
    for u in Users:
        if u.Login == Login:
            if u.Password == Password:
                return u
found_user = users(Users)
print(f"Пользователь: {found_user.Login}, Пароль: {found_user.Password}")


