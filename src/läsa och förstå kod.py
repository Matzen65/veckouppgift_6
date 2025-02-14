"""
1 Läsa och förstå kod - diskutera i grupp
Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?
"""

#====================== 1 =================================
# 1 Vad gör följande kod?
# Svar: Det printas ut orden Anakonda Boaorm, Anakonda läggs till i x, boaorm läggs i y
# SafeStorage.__data = Anakonda
# SafeStorage.__data = Boaorm

print('----- 1 -----')
class SafeStorage:
    __data = None

    def get(self):
        return self.__data

    def put(self, data):
        self.__data = data


safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)

#====================== 2a =================================
# 2a Vad gör följande kod? Fixa eventuella fel.
# Svar: Koden skapar en klass för Animal med två underklasser som ärver från Animal - Hund och Katt.
# När "make_noise" anropas skrivs djurets läte ut.

# Fel jag funnit i koden är:
# Indentering saknas vid print för dog.
# Man har angett "shelf" på make noise för Cat, (def make_noise(shelf):)
# sound_off(animal) bör göras om till en loop för uppräkning till lista.

print('----- 2a -----')

class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(self):
        super().make_noise()
        print("Mjau!")

class Rooster(Animal): # Rooster saknades.
    def make_noise(self):
        print("Kuckeliku!")

#print('----- 2b  lagt till Lion -----')
class Lion(Animal):
    def make_noise(self):
        print("ROAHRRRR!")

def sound_off(animal):
    for item in animal:
        item.make_noise()

c = Cat()
d = Dog()
h = Rooster()
g = Lion()
sound_off([c, d, h])

#====================== 2b =================================

# 2b Lägg till en klass för ett annat djur, till exempel en guldfisk.
# Svar: lade till Lion.
print('----- 2b -----')

class Lion(Animal):
    def make_noise(self):
        print("ROAHRRRR!")

sound_off([g])