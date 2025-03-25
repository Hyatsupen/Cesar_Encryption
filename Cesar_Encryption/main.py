from Cifrar_Cesar import cifrar
from Descifrar_Cesar import descifrar
from Manejo_archivo import manejar_archivo
from Validar_entrada import validar_texto, validar_archivo
from Obtener_desplazamiento import obtener_desplazamiento
from Exportar_resultado import exportar_resultado
import os
import sys
import time
from functools import wraps

def barra_progreso(operacion):
    """
    Decorador para mostrar barra de progreso durante operaciones
    """
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                print(f"\n⌛ {operacion.capitalize()}...")
                inicio = time.time()
                
                # Mostrar barra de progreso animada
                for i in range(101):
                    time.sleep(0.03)  # Simula progreso
                    sys.stdout.write(f"\r[{('█' * i).ljust(100)}] {i}%")
                    sys.stdout.flush()
                
                resultado = func(*args, **kwargs)
                
                tiempo = time.time() - inicio
                print(f"\n✅ {operacion.capitalize()} completado en {tiempo:.2f} segundos")
                return resultado
                
            except Exception as e:
                print(f"\n❌ Error al {operacion}: {str(e)}")
                return None
        return wrapper
    return decorador

def mostrar_menu():
    print("\n═" * 50)
    print(" " * 18 + "🔐 CIFRADO CÉSAR AVANZADO 🔐")
    print("═" * 50)
    print("1. Cifrar texto manual")
    print("2. Descifrar texto manual")
    print("3. Cifrar archivo")
    print("4. Descifrar archivo")
    print("5. Salir")
    print("═" * 50)

@barra_progreso("procesando")
def procesar_texto(texto, desplazamiento, operacion):
    if operacion == "cifrar":
        return cifrar(texto, desplazamiento)
    else:
        return descifrar(texto, desplazamiento)

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == "1":  # Cifrado manual
            texto = input("\nIngrese el texto a cifrar:\n> ")
            validar_texto(texto)
            desplazamiento = obtener_desplazamiento()
            resultado = procesar_texto(texto, desplazamiento, "cifrar")
            
            print("\n═" * 50)
            print(f"🔒 TEXTO CIFRADO (Desplazamiento: {desplazamiento}):")
            print("═" * 50)
            print(resultado)
            
            if input("\n¿Exportar resultado? (s/n): ").lower() == 's':
                exportar_resultado(texto, resultado, "Cifrado", desplazamiento)
        
        elif opcion == "2":  # Descifrado manual
            texto = input("\nIngrese el texto a descifrar:\n> ")
            validar_texto(texto)
            desplazamiento = obtener_desplazamiento()
            resultado = procesar_texto(texto, desplazamiento, "descifrar")
            
            print("\n═" * 50)
            print(f"🔓 TEXTO DESCIFRADO (Desplazamiento: {desplazamiento}):")
            print("═" * 50)
            print(resultado)
            
            if input("\n¿Exportar resultado? (s/n): ").lower() == 's':
                exportar_resultado(texto, resultado, "Descifrado", desplazamiento)
        
        elif opcion in ("3", "4"):  # Manejo de archivos
            archivo = input("\nIngrese la ruta del archivo (.txt):\n> ").strip()
            
            if validar_archivo(archivo):
                desplazamiento = obtener_desplazamiento()
                resultado = manejar_archivo(
                    "cifrar" if opcion == "3" else "descifrar",
                    archivo,
                    desplazamiento
                )
                
                if resultado:
                    print("\n═" * 50)
                    print(f"🔍 PRIMEROS 300 CARACTERES:")
                    print("═" * 50)
                    print(resultado[:300])
                    
                    if input("\n¿Exportar resultado completo? (s/n): ").lower() == 's':
                        nombre_export = f"{'cifrado' if opcion == '3' else 'descifrado'}_{os.path.basename(archivo)}"
                        exportar_resultado(
                            f"Contenido de {archivo}",
                            resultado,
                            "Cifrado" if opcion == "3" else "Descifrado",
                            desplazamiento,
                            nombre_export
                        )
        
        elif opcion == "5":
            print("\n¡Hasta pronto! 👋")
            break
            
        else:
            print("\n❌ Opción no válida")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()