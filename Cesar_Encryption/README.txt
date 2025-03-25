# 🔐 Cifrado César Avanzado

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub](https://img.shields.io/badge/Status-Activo-brightgreen)

Herramienta profesional de cifrado/descifrado César con interfaz interactiva y manejo de archivos.

## 📌 Tabla de Contenidos

⚠️ Limitaciones
Máximo 5MB por archivo
❓ FAQ
P: ¿Cómo cifro un archivo grande?
R: Divide el archivo en partes <5MB o modifica Validar_entrada.py

P: ¿Por qué no funcionan los emojis?
R: El algoritmo solo procesa caracteres ASCII estándar



## 🌟 Características

| Función               | Descripción                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Cifrado/Descifrado**| Soporte para texto y archivos con desplazamiento personalizado              |
| **Interfaz intuitiva**| Menú interactivo con validación de entradas                                 |
| **Progreso visual**   | Barra de progreso para operaciones con archivos grandes                     |
| **Exportación**       | Genera reportes con metadatos (fecha, operación, desplazamiento)            |
| **Seguridad**         | Valida archivos y caracteres no cifrables (emojis, tabs, etc.)              |



## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Hyatsupen/Cesar_Encryption.git

# Navegar al directorio
cd cifrado-cesar

# (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows



##🚀 Uso

python main.py


Menú Principal:
═🔐 CIFRADO CÉSAR AVANZADO═
1. Cifrar texto manual
2. Descifrar texto manual
3. Cifrar archivo (.txt)
4. Descifrar archivo (.txt)
5. Salir

📝 Ejemplos
1. Cifrado manual
Texto original:  "Python es genial!"
Desplazamiento: 5
Resultado:      "Udymts jx ljsnfq%"


🗂️ Estructura del Proyecto

├── main.py                 # Interfaz principal
├── Cifrar_Cesar.py         # Algoritmo de cifrado
├── Descifrar_Cesar.py      # Algoritmo de descifrado
├── Manejo_archivo.py       # Gestión de archivos
├── Validar_entrada.py      # Validación de inputs
├── Exportar_resultado.py   # Sistema de exportación
├── Obtener_desplazamiento.py # Control de claves
├── Progreso.py            # Barra de progreso
├── README.md              # Este archivo
└── requirements.txt       # Dependencias (si aplica)




