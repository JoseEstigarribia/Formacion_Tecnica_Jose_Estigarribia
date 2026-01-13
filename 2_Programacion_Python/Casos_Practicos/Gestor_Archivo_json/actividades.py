import json

try:
    with open("Actividades.json", "r", encoding="utf-8") as archivo:
        actividades = json.load(archivo)

except FileNotFoundError:
    actividades = []

nueva_actividad = {
    "Nombre": "Estudiar Python",
    "Fecha": "10/01/2026",
    "Estado": "Hecho"
}

if nueva_actividad not in actividades:
    actividades.append(nueva_actividad)

with open("Actividades.json", "w", encoding="utf-8") as archivo:
    json.dump(actividades, archivo, indent=4, ensure_ascii=False)

print("Actividades guardadas correctamente.")

