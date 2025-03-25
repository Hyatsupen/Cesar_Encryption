import datetime

def exportar_resultado(texto_original, resultado, operacion, desplazamiento, nombre_archivo="resultado_cesar.txt"):
    """
    Guarda los resultados en un archivo con formato legible
    """
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    contenido = f"""
=== REGISTRO DE CIFRADO CÉSAR ===
Fecha: {fecha}
Operación: {operacion.upper()}
Desplazamiento: {desplazamiento}

--- TEXTO ORIGINAL ---
{texto_original}

--- RESULTADO ---
{resultado}
"""
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as f:
            f.write(contenido)
        print(f"✓ Resultado exportado en '{nombre_archivo}'")
    except Exception as e:
        print(f"Error al exportar: {str(e)}")