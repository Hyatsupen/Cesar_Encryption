import os
from pathlib import Path

def validar_texto(texto):
    """
    Muestra advertencias para caracteres no cifrables (emojis, tabs, etc.)
    pero NO filtra ningún carácter. Devuelve el texto intacto.
    """
    caracteres_no_cifrables = [c for c in texto if ord(c) < 32 or ord(c) > 126]
    
    if caracteres_no_cifrables:
        print("\n═" * 50)
        print("⚠️  ADVERTENCIA: Caracteres no cifrables detectados")
        for char in caracteres_no_cifrables:
            print(f" - '{char}' (ASCII: {ord(char)})")
        print("═" * 50 + "\n")
    
    return texto

def validar_archivo(ruta_archivo, max_mb=5):
    """
    Valida: existencia, formato .txt y tamaño máximo (5MB por defecto)
    """
    path = Path(ruta_archivo)
    
    if not path.exists():
        print(f"❌ Error: El archivo no existe")
        return False
        
    if not path.is_file():
        print(f"❌ Error: No es un archivo válido")
        return False
        
    if path.suffix.lower() != '.txt':
        print(f"❌ Error: Solo se permiten archivos .txt")
        return False
        
    tamano_mb = os.path.getsize(ruta_archivo) / (1024 * 1024)
    if tamano_mb > max_mb:
        print(f"❌ Error: Archivo demasiado grande ({tamano_mb:.2f}MB > {max_mb}MB)")
        return False
        
    return True