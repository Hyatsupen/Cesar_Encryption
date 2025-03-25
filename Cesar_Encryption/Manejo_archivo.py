from Progreso import barra_progreso

@barra_progreso("cifrando")
def cifrar_archivo(contenido, desplazamiento):
    from Cifrar_Cesar import cifrar
    return cifrar(contenido, desplazamiento)

@barra_progreso("descifrando")
def descifrar_archivo(contenido, desplazamiento):
    from Descifrar_Cesar import descifrar
    return descifrar(contenido, desplazamiento)

def manejar_archivo(operacion, ruta_archivo, desplazamiento):
    try:
        # Leer el contenido del archivo (el decorador manejará la barra de progreso)
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Procesar según la operación
        if operacion == "cifrar":
            resultado = cifrar_archivo(contenido, desplazamiento)
        else:
            resultado = descifrar_archivo(contenido, desplazamiento)
        
        return resultado
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None