
class User:

    def __init__(self, lang, username, password):
        self.preferred_language = lang
        self.username = username
        self.__password = password

    def __str__(self):
        """Returnerar klassens innehåll i strängformat"""
        return (f"user: {self.preferred_language}, {self.username}, "
                f"{self.__password}") #__ betyder ej publict = dolt

    # Ett alternativ är att skapa en "getter" med dekoratorn @property
    def get_password(self):
        return self.__password

    @property
    def password(self):
        print("nu anropas 'password' getter")
        return self.__password

    def is_correct_login(self, username, password):
        if username == self.username and password == self.__password:
            return True
        else:
            return False
