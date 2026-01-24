# Caso 001 - Organizador Automático de Archivos

## Escenario
Se necesita un script que ordene automáticamente archivos según su extensión.

## Solución
Se desarrolló un script en Python que:
- Recorre una carpeta específica
- Detecta archivos
- Identifica su extensión
- Crea carpetas por categoría si no existen
- Mueve los archivos a su carpeta correspondiente

## Herramientas utilizadas
- os
- shutil

## Aprendizajes
- Manejo de rutas con os.path.join
- Recorrido de directorios
- Uso de diccionarios con listas
- Creación dinámica de carpetas
