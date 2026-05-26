# FASE 5
# Johan Stephen Ulloa León
# CC 1031161291
# Código: 213022

#MATRIZ DE DATOS
clientes = [
    ["Cliente 1", 200, 10],
    ["Cliente 2", 45, 2],
    ["Cliente 3", 120, 5],
    ["Cliente 4", 300, 15],
    ["Cliente 5", 50, 7],
]
#FUNCION PARA CALCULAR CLASIFICACIÓN DE COMPROMISO DE LOS CLIENTES
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

#En esta parte del código primero imprimo el título ‘Informe Final’. Luego utilizo un ciclo for para 
# recorrer cada fila de la matriz de clientes. De cada fila extraigo tres datos: 
# el ID del cliente, la duración de la sesión y la cantidad de clics. Después llamo a la función clasificar_compromiso(), que analiza esos datos y devuelve si el compromiso es Alto, Medio o Bajo. Finalmente imprimo el ID del cliente junto con su clasificación.”
print("INFORME FINAL")

for cliente in clientes:
    id_cliente = cliente[0]
    duracion = cliente[1]
    clics = cliente[2]

    resultado = clasificar_compromiso(duracion, clics)

    print(id_cliente, "-", resultado)