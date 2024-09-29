#Variables
my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)

suma = 3+2
print(suma)

my_bool_variable = False
print(my_bool_variable)

#concadenar variables dentro de un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

#variables de una sola linea
name, surname, alias, age = "Brais", "Moure", "pepe", 35 
print("me llamo: ", name, surname, "Mi alias es: ", alias,"Mi edad es: ", age  )

#Funciones del sistema
print(len("hola"))

#scanner
nombre = input("Cual es tu nombre?")
edad=input("Cual es tu edad? ")
print(nombre)
print(edad)