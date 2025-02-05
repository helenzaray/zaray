""""
conjunto = {" carro","casa","beca","empresa"}
conjunto2 = set((" carro","casa","beca","empresa"))
print(conjunto)
print(conjunto2)
"""

frutas = {"manzana","piña","naranja","mandarina"}
carros = {"toyota","fiat","ferrary","fiat", "piña"}


print(frutas)
print(carros)

frutas.add("guanabanaa")
print(frutas)

copia = frutas.copy()
print(copia)

print(frutas.difference(carros))
frutas.discard("guanabana")
print(frutas)
frutas.discard("piña")
print(frutas.pop())

frutas.intersection(carros)
frutas.difference(carros)
