
class User:

    def __init__(self, lang, username, password):
        self.preferred_language = lang
        self.username = username
        self.password = password

    def __str__(self):
        """Returnerar klassens innehåll i strängformat"""
        return (f"user: {self.preferred_language}, {self.username}, "
                f"{self.__password}")


