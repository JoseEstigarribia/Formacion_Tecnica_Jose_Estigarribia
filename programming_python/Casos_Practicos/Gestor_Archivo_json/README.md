# Script de Gestión de Actividades (JSON)

## 📌 Descripción
Este proyecto consiste en un script en Python que permite gestionar actividades diarias utilizando un archivo JSON como almacenamiento.

El script:
- Crea el archivo si no existe
- Lee actividades existentes
- Agrega nuevas actividades
- Guarda los cambios de forma persistente

## 🛠️ Tecnologías utilizadas
- Python 3
- Manejo de archivos
- JSON
- Control de errores con try/except

## 📂 Estructura del archivo JSON
```json
[
  {
    "Nombre": "Estudiar Python",
    "Fecha": "10/01/2026",
    "Estado": "Hecho"
  }
]

