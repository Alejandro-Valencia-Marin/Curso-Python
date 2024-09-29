 ### Strings ###
 
string = "Mi string"
my_other_string= "my other string"

print(len(string))
print(len(my_other_string))

print(string + ""  + my_other_string)

new_string = "Nuevo String con un \n salto de linea incluido " 
print(new_string)

tab_String = "\t Este String tiene tabulacion" 
print(tab_String)

scape_string = "\t Este estring \n tiene un escapado"
print(scape_string)

#Formateo

name, surname, edad = "Alex", "Valencia", 19
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,edad))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,edad))
print(f"Mi nombre es {name} {surname} y mi edad es {edad}")

## Desempaquetado ## 
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# Division #
language_slice = language[1:3]
print(language_slice)

# Reverse
reverse_language = language [::-1]
print(reverse_language)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print("1".isnumeric())
print(language.isnumeric())
print(language.lower())
print(language.upper().isupper())
