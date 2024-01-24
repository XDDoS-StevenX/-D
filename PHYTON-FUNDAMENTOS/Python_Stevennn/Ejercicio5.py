Ejercicio5

palabra = input("Ingresa una palabra: ")

palabra = palabra.replace(" ", "").lower()

if palabra == palabra[::-1]:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")