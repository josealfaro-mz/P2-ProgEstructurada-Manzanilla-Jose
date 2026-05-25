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
def analizar_rendimiento(lista_loss): 
    """ 
Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento. 
Requisitos: 3 llamadas distintas a la biblioteca 'statistics'. 
""" 
# TODO: Implementar lógica 
pass 
def calcular_rmse(predicciones, reales): 
    """ 
Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE). 
Requisitos: 3 llamadas distintas a la biblioteca 'math'. 
""" 
# TODO: Implementar lógica 
pass 
# ========================================== 
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA) 
# ========================================== 
def main():
    print("=== INICIANDO SIMULADOR DE AGENTES DE IA ===")
# TODO: Invocar las funciones, orquestar el flujo y mostrar reportes ordenados. 
    obtener_info_sistema()
    
if __name__ == "__main__": 
    main()
