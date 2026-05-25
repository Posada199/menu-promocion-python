
# Promociones de Menú - Restaurante

#Este proyecto resuelve un problema de programación donde se aplican promociones a productos de un menú.

## Funcionalidad

# Se almacena un menú en una matriz
# Se aplica un 15% de descuento si:
# - El producto pertenece a la categoria "Bebidas"
# - Si su precio supera un umbral definido de 10j000
# - Se muestra el precio final de cada producto después de aplicar la promoción

## Lenguaje (Python)

# MATRIZ DE PRODUCTOS 
# [Nombre, Categoria, Precio Base]

menu = [
    ["Pizza", "Comida", 15000],
    ["Hamburguesa", "Comida", 20000],
    ["Ensalada", "Comida", 13000],
    ["Jugo Natural", "Bebidas", 12000],
    ["Café", "Bebidas", 3000],
    ["Gaseosa", "Bebidas", 5000]
]

# PARAMETROS DE PROMOCION
categoria_objetivo = "Bebidas"
umbral = 10000
    
# FUNCION PARA CALCULAR PRECIO FINAL
def calcular_precio_final(producto):
    nombre, categoria, precio = producto

    if categoria == categoria_objetivo and precio > umbral:
        descuento = precio * 0.15
        precio_final = precio - descuento
    else:
        precio_final = precio

    return precio_final


# PROCESO Y SALIDA
print("===== MENÚ CON PROMOCIÓN =====")

for producto in menu:
    precio_base = producto[2]
    precio_final = calcular_precio_final(producto)

    print(f"Producto: {producto[0]}")
    print(f"Categoría: {producto[1]}")
    print(f"Precio Base: ${precio_base:.0f}")
    print(f"Precio Final: ${precio_final:.0f}")
    print("-----------------------------")  
    
    