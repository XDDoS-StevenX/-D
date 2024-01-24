eleccion_comida = input("¿Qué tipo de comida prefieres? (italiana, mexicana, china): ")

if eleccion_comida.lower() == 'italiana':
    print("Te recomendaría ir a 'La Trattoria' para disfrutar de comida italiana.")
elif eleccion_comida.lower() == 'mexicana':
    print("Te sugiero probar 'La Taquería' para disfrutar de auténtica comida mexicana.")
elif eleccion_comida.lower() == 'china':
    print("Para comida china, te recomendaría 'El Dragón Dorado'.")
else:
    print("Lo siento, no puedo recomendar un restaurante para ese tipo de comida.")
