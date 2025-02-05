""""
usuarios = []

while True:

 nombre = input("digita un nombre o x"  )

 if nombre == "X":
    break

usuarios.append(nombre)

print("usuarios resistrados", usuarios)
"""

frutas = tuple (("fresa","manzana","papaya","manzana"))
print(frutas)
frutas2=("fresa","manzana","papaya","manzana")
print(frutas2)
print(frutas.count("manzana"))
print(frutas.index("manzana"))


temporal =list(frutas)
print(temporal)
frutas = tuple(temporal)
print(frutas)



