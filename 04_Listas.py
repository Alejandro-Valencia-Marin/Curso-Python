my_list = list()
my_other_list =[]

print(len(my_list))

my_list = [35, 52 , 24, 62, 60, 45]

print(my_list)
print(len(my_list))

my_other_list = [25, 1.77, "Alex", "Valencia"]
print(type(my_list))
print(type(my_other_list))

print(my_other_list[1])
print(my_list.count(30))

edad, peso, nombre, apellido = my_other_list
print(nombre)

print(my_list + my_other_list)

#Insertar al final

my_other_list.append("Final")
print(my_other_list)

#Usar inser para intruducir en la lista 

my_other_list.insert(1, "azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.clear()
print(my_list)

my_other_list.reverse()
print(my_list)

