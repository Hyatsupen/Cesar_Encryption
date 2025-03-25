# install_requirements.py
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Verifica que Python 3.8+ esté instalado"""
    if sys.version_info < (3, 8):
        print("\n❌ Se requiere Python 3.8 o superior")
        print(f"Versión actual: {sys.version.split()[0]}")
        sys.exit(1)

def install_requirements():
    """Instala las dependencias desde requirements.txt"""
    req_file = Path("requirements.txt")
    
    # Verificar si el archivo existe
    if not req_file.exists():
        print("\nℹ️  No se encontró requirements.txt")
        print("Creando archivo básico con Python 3.8+ como requisito...")
        with open(req_file, 'w') as f:
            f.write("python>=3.8\n")
        print("✅ Archivo creado: requirements.txt")
    
    print("\n🔍 Analizando dependencias...")
    
    try:
        # Instalar dependencias
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            stdout=subprocess.DEVNULL
        )
        print("✅ Todas las dependencias se instalaron correctamente")
        
    except subprocess.CalledProcessError:
        print("\n❌ Error al instalar dependencias. Solución:")
        print("1. Verifica que pip esté actualizado:")
        print("   python -m pip install --upgrade pip")
        print("2. Revisa el archivo requirements.txt")
        sys.exit(1)

def main():
    print("\n" + "═" * 50)
    print("  INSTALADOR AUTOMÁTICO - CIFRADO CÉSAR")
    print("═" * 50)
    
    check_python_version()
    install_requirements()
    
    # Verificación final
    print("\n" + "═" * 50)
    print("Versión de Python:", sys.version.split()[0])
    print("Ubicación:", sys.executable)
    print("═" * 50)

if __name__ == "__main__":
    main()