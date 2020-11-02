class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError('value not string')
        self.__password = value


user = User('sfds', 123456)
