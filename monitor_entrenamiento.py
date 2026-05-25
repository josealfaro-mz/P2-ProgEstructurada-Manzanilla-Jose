""" 
Nombre del Alumno: José Alberto Manzanilla Alfaro
Matrícula: UX25II353
Fecha: 25-Mayo-2026 
Examen Segundo Parcial - Programación Estructurada 
""" 
# ========================================== 
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR 
# ========================================== 
import datetime 
import math 
import random 
import statistics 
import sys 
# ==========================================
# 2. DEFINICIÓN DE CONSTANTES 
# ========================================== 
MAX_EPOCHS = 10 
UMBRAL_ERROR_CRITICO = 0.95 
# ========================================== 
# 3. FUNCIONES DEFINIDAS POR EL USUARIO 
# ========================================== 
def obtener_info_sistema(): 
    """ 
Usa la biblioteca 'sys' para validar el entorno de ejecución. 
Requisitos: Realizar 3 llamadas distintas a la biblioteca 'sys'. 
    """ 
    plataforma = sys.platform
    version = sys.version
    ruta = sys.executable

    print("--- INFO DEL SISTEMA ---")
    print("Plataforma:", plataforma)
    print("Version de Python:", version)
    print("Ruta del ejecutable:", ruta)

def simular_metricas_entrenamiento(cantidad_epochs): 
    """ 
Usa las bibliotecas 'random' y 'datetime' para simular los datos de entrenamiento. 
Requisitos: 3 llamadas a 'random' y 3 llamadas a 'datetime'. 
""" 
    lista_loss = []
    lista_latencia = []
    eventos = ["Epoch exitoso", "Gradiente inestable", "Actualizacion de pesos"]

    inicio = datetime.datetime.now()
    fecha_formateada = inicio.strftime("%d/%m/%Y %H:%M:%S")
    print("\n--- SIMULACION DE ENTRENAMIENTO ---")
    print("Inicio:", fecha_formateada)

    contador = 0
    while contador < cantidad_epochs:
        loss = random.uniform(0.1, 1.0)
        probabilidad = random.random()
        evento = random.choice(eventos)

        latencia = random.uniform(0.5, 3.0)
        lista_loss.append(loss)
        lista_latencia.append(latencia)

        print("Epoch", contador + 1, "| Loss:", round(loss, 4), "| Evento:", evento, "| Prob exito:", round(probabilidad, 2))
        contador = contador + 1

    fin = datetime.datetime.now()
    diferencia = fin - inicio
    print("Fin:", fin.strftime("%d/%m/%Y %H:%M:%S"))
    print("Duracion total:", diferencia)

    return lista_loss, lista_latencia

def analizar_rendimiento(lista_loss, lista_latencia): 
    """ 
    Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento. 
    Requisitos: 3 llamadas distintas a la biblioteca 'statistics'. 
    """ 
    media = statistics.mean(lista_loss)
    desviacion = statistics.stdev(lista_loss)
    mediana_latencia = statistics.median(lista_latencia)

    print("\n--- ANALISIS DE RENDIMIENTO ---")
    print("Media de loss:", round(media, 4))
    print("Desviacion estandar:", round(desviacion, 4))
    print("Mediana de latencia:", round(mediana_latencia, 4), "seg")

    return media

def calcular_rmse(predicciones, reales): 
    """ 
    Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE). 
    Requisitos: 3 llamadas distintas a la biblioteca 'math'. 
    """ 
    suma = 0
    i = 0
    while i < len(predicciones):
        diferencia = predicciones[i] - reales[i]
        suma = suma + math.pow(diferencia, 2)
        i = i + 1

    promedio = suma / len(predicciones)
    rmse = math.sqrt(promedio)
    rmse_redondeado = math.fabs(rmse)

    print("\n--- CALCULO DE RMSE ---")
    print("RMSE:", round(rmse_redondeado, 4))

    return rmse_redondeado
# ========================================== 
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA) 
# ========================================== 
def main():
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")
    # TODO: Invocar las funciones, orquestar el flujo y mostrar reportes ordenados. 

    obtener_info_sistema()

    lista_loss, lista_latencia = simular_metricas_entrenamiento(MAX_EPOCHS)

    media_loss = analizar_rendimiento(lista_loss, lista_latencia)

    predicciones = lista_loss
    reales = []
    i = 0
    while i < len(lista_loss):
        valor_real = lista_loss[i] + random.uniform(-0.05, 0.05)
        reales.append(valor_real)
        i = i + 1

    rmse = calcular_rmse(predicciones, reales)

    print("\n--- REVISION FINAL ---")
    if media_loss >= UMBRAL_ERROR_CRITICO:
        print("ERROR CRITICO: El loss promedio supera el umbral permitido.")
        sys.exit(1)
    else:
        print("Entrenamiento completado sin errores criticos.")

if __name__ == "__main__": 
    main()

"""
    CUESTIONARIO DE ANALISIS DE BIBLIOTECAS

    1. Uso de Objetos y Métodos:
        Al usar datetime.datetime.now(), 'datetime' es el nombre del modulo que
        importamos, el segundo 'datetime' es la clase que contiene los datos de
        fecha y hora, y 'now()' es el metodo que llamamos para obtener la fecha
        actual. Se relaciona con biblioteca externa porque nosotros no escribimos
        ese codigo, lo reutilizamos desde la biblioteca que Python ya tiene instalada.

    2. Diferenciación Técnica:
        Cuando usamos 'import math' tenemos que escribir el nombre del modulo cada
        vez que usamos una funcion, por ejemplo math.sqrt(). Si usaramos
        'from math import sqrt' podriamos llamar solo sqrt() sin el prefijo. En este
        codigo usamos 'import math' para que quede claro de donde viene cada funcion.

    3. Flujo y Lógica:
        Primero la funcion simular_metricas_entrenamiento genera la lista de loss con
        valores aleatorios. Esa lista se pasa a analizar_rendimiento para sacar la
        media y la desviacion. Tambien se usa esa lista como predicciones en
        calcular_rmse, donde se compara contra valores reales simulados con una
        pequeña variacion aleatoria, y se calcula el error final.

    4. Mapeo de Tipos de Datos:
        Use listas para guardar los valores de loss y de latencia de cada epoch.
        Elegi listas porque necesitaba guardar multiples valores en orden para despues
        pasarlos a las funciones de statistics. Si hubiera usado variables simples
        solo podria guardar un valor a la vez y perderia la informacion de todos los epochs.

    5. Autoevaluación de Abstracción:
        No tuve que programar la formula de la desviacion estandar. Solo llame
        statistics.stdev() y la biblioteca hizo todo el calculo internamente. Esto es
        Abstraccion porque la biblioteca nos oculta la complejidad de la formula y
        nosotros solo necesitamos saber que funcion llamar y que datos darle, sin
        preocuparnos por como funciona por dentro.
"""