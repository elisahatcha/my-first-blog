print('Hello, Django girls!')
nombre_de_films = 50
if nombre_de_films < 20:
    print("pas mal!")
elif 20 <= nombre_de_films < 40:
    print("bravo!")
elif 40 <= nombre_de_films < 60:
    print("wow")
else:
    print("Tant mieux pour toi")


def Hola (name):
    if name == 'Claire':
        print('Hola Claire')
    elif name == 'Flo':
        print('Hola Flo!')
    else:
        print('Hola anonymous!')
Hola('Flo')
Hola('Claire')
Hola('Rosa')

def Hola (name):
    print('Hola ' + name + '!')
Hola ("Pedro")
