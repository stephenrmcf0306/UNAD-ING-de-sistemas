# Datos iniciales de los empleados 
#Para este primer error, encontramos que se asignó el valor de las horas como string pero es un dato INT
#También analizo que el nombre DATOS_EMPLEADOS viene en mayúscula al ser utilizada para una variable global
DATOS_EMPLEADOS = [ 
{"nombre": "Ana García", "horas": 160, "tarifa": 15.5}, 
{"nombre": "Luis Pérez", "horas": 150, "tarifa": 18.0}, # Error 1: Horas como string 
{"nombre": "Marta López", "horas": 165, "tarifa": 12.0} ] 
TASA_DESCUENTO = 0.15 
def calcular_bruto(h, t): 
    """Calcula el salario bruto.""" 
#Error 2: Están concatenando un sting "bruto" con una función matemática, lo cual no es correcto.
#Se elimina el string para que la función retorne un valor numérico aparte que no está identidado
    return h * t  

#Error 3: En el siguiente bloque hay error de identación, y la variable que está declarada 
# como TASA_DESCUENTO_INCORRECTA no existe, se corrige a TASA_DESCUENTO
def calcular_neto(salario_bruto): 
    """Calcula el salario neto aplicando el descuento.""" 
    descuento = salario_bruto * TASA_DESCUENTO 
    return salario_bruto - descuento 

#El número 9 esta agregado por error, se elimina para que la función se declare correctamente
def generar_informe(lista_empleados): 
    for empleado in lista_empleados: # Nombre de la variable mal escrito, se corrige. Phyton reconoce mayús y minúscula.
        nombre = empleado['nombre'] #Declara una variable que no existe, se corrige a 'nombre' que es el nombre correcto del campo en el diccionario.
        horas = empleado['horas'] 
        tarifa = empleado['tarifa'] 
        salario_bruto = calcular_bruto(horas, tarifa) 
        salario_neto = calcular_neto(salario_bruto) 
        print(f"Informe de {nombre}: Salario Neto: ${salario_neto:.2f}") #Estaba sin identación, se corrige para que esté dentro del bloque de la función.
generar_informe(DATOS_EMPLEADOS)
