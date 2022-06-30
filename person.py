
class Person:
    """Class Person. Could be customer or veterinarian."""
    def __init__(self, name, last_name, cc, age, tell, email):
        if type(name) != str:
            raise TypeError('El nombre debe ser una cadena de caracteres')
        if type(last_name) != str:
            raise TypeError('El apellido debe ser una cadena de caracteres')
        if type(cc) != str:
            raise TypeError('La cédula debe ser una cadena de caracteres')
        if type(age) != str:
            raise TypeError('La edad debe ser una cadena de caracteres')
        if type(tell) != str:
            raise TypeError('El teléfono debe ser una cadena de caracteres')
        if type(email) != str:
            raise TypeError('El correo debe ser una cadena de caracteres')
        self.__name = name
        self.__last_name = last_name
        self.__cc = cc
        self.__age = age
        self.__tell = tell
        self.__email = email
 