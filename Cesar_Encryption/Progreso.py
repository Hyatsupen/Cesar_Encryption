import sys
import os
from time import time
from functools import wraps

def barra_progreso(operacion):
    """
    Decorador para mostrar barra de progreso durante operaciones con archivos
    Uso: @barra_progreso("cifrando")  # o "descifrando"
    """
    def decorador(func):
        @wraps(func)
        def wrapper(ruta_archivo, *args, **kwargs):
            try:
                # Configuración inicial
                tamano = os.path.getsize(ruta_archivo)
                inicio = time()
                procesados = 0
                
                print(f"\n⌛ {operacion.capitalize()} archivo...")
                print(f"📏 Tamaño: {tamano/1024:.2f} KB")
                
                # Función que actualiza el progreso
                def actualizar_progreso(chunk):
                    nonlocal procesados
                    procesados += len(chunk)
                    porcentaje = min(100, (procesados/tamano)*100)
                    barra = '█' * int(porcentaje/2) + ' ' * (50 - int(porcentaje/2))
                    sys.stdout.write(f"\r[{barra}] {porcentaje:.1f}% ({procesados/1024:.1f}/{tamano/1024:.1f} KB)")
                    sys.stdout.flush()
                
                # Procesar con actualización de progreso
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    resultado = []
                    while chunk := f.read(1024):  # Leer en bloques de 1KB
                        resultado.append(func(chunk, *args, **kwargs))
                        actualizar_progreso(chunk)
                
                tiempo = time() - inicio
                print(f"\n✅ {operacion.capitalize()} completado en {tiempo:.2f} segundos")
                return ''.join(resultado)
                
            except Exception as e:
                print(f"\n❌ Error al {operacion}: {str(e)}")
                return None
                
        return wrapper
    return decorador
