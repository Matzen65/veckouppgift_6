
# ---- 2.1.a ----
class Country:
    def __init__(self, name, pop, area = None): #om area ej anges så får parametern default None
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__language_list = []

    def print_info(self):
        print(f"I {self.__name} bor det {self.__population} miljoner invånare")
        if self.__area is not None:
            print(f"{self.__name} har en area på {self.__area} tusen km2.")
        for language in self.__language_list:
            print(language)
    def add_language(self, lang):
        self.__language_list.append(lang)


se = Country("Sverige", 10.5, 10)
no = Country("Norge", 5.5)
il = Country("Island", 0.38)   #avrundat från 382726
dk = Country("Danmark", 5.96)   #avrundat från 5961249
fi = Country("Finland", 5.6)   #avrundat från 5636521

# ---- 2.1.b ----
#printar info för Norge (se)
print()
se.print_info()

# ---- 2.1.c ----
# print()
# se.print_info()

# ---- 2.1.f ----
fi.add_language("svenska")
fi.add_language("finska")
print()
fi.print_info()