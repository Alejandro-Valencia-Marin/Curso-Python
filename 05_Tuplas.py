## Tuplas ##

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (53, 1.70, "Alejandro", "Valencia")
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Alejandro"))

print(my_tuple.count("Alejandro"))
print(my_tuple.index("Valencia"))
print(my_tuple + my_other_tuple)

sum_tuple = my_tuple + my_other_tuple
print(sum_tuple)
print(sum_tuple[3:6]) #asi tomamos 2 elementos concretos de las 2 tuplas

my_tuple = list(my_tuple)
print(type(my_tuple))


my_tuple[4] = "Nuevo caracter"
my_tuple.insert(2, "caraacter nuevo en la posicion 2")
