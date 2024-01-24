Ejercicio2

calificacion_numerica = float(input("Ingresa tu calificación numérica: "))

if calificacion_numerica >= 90:
    letra = 'A'
elif calificacion_numerica >= 80:
    letra = 'B'
elif calificacion_numerica >= 70:
    letra = 'C'
elif calificacion_numerica >= 60:
    letra = 'D'
else:
    letra = 'F'

print(f"Tu calificación en letras es: {letra}")