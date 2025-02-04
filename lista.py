
"""""
edad = 52
lista = ["hola", 58, True , 3.1416]
print(lea(lista1))


frutas = ["papaya","fresa","mango"]
print(frutas)
print(frutas [1])
"""
""""
frutas = ["papaya","fresa","mango"]
print(frutas)
frutas.append("naranja")
print(frutas)
frutas.insert(2,"uva")
print(frutas)

frutas [2]="mandarina"
print(frutas)

verduras = ["espinaca","tomate","lechuga"]

frutas.extend(verduras)
print(frutas)

#frutas.clear()
print(frutas)
#del frutas
print(frutas)

copia = frutas.copy()
print(copia)
copia.append("perro")
print(copia)
print(frutas)


verduras = ["espinaca","tomate","lechuga"]
copiaverduras = verduras
copiaverduras.append("paqueteco de mani")
print(copiaverduras)
copiaverduras.clear()
print(copiaverduras)


verduras = ["espinaca","tomate","lechuga"]
print(verduras.count("tomate"))
print(verduras.index("lechuga"))
verduras.pop()
print(verduras)
verduras.pop(1)
print(verduras)
verduras.remove("lechuga")
print(verduras)
"""
verduras = ["espinaca","tomate","lechuga","tomate", "zanahorias"]
verduras.reverse()
print(verduras)
verduras.sort()
print(verduras)