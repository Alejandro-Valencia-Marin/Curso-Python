## SETS ##

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Al inicio es un diccionario

my_other_set = {"Alejandro", "Valencia",19}
print(type(my_other_set))

my_other_set.add("Marin") #Un set no admite repetidos
print(my_other_set)

print("Alejandro" in my_other_set)
print("Alejandri" in my_other_set )

my_other_set.remove("Valencia")
print(my_other_set)

my_other_set.clear() 
print(len(my_other_set))

del my_other_set


my_set = {"Alejandro", "Valencia",19}
my_other_set = {"Juan", "Alvarez", "si no? "}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))