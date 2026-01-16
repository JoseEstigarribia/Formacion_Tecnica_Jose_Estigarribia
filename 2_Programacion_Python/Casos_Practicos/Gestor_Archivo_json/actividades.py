import json
print("SCRIPT GESTION ACTIVIDADES EN JSON   ")


def cargar_actividades():
        try:
            with open("Actividades.json","r") as archivo:
                return json.load(archivo)

        except FileNotFoundError:
            lista = []
            with open("Actividades.json","w") as archivo:
                json.dump(lista,archivo,indent=4)
                
                return lista 

def guardar_actividades(nueva_actividad):

        #Partiendo de los Actividades cargadas, si no son duplicada Agregamos, usamos funciones anidadas.
        actividades = cargar_actividades()
        if nueva_actividad not in actividades:
            actividades.append(nueva_actividad)

            with open("Actividades.json","w") as archivo:
                json.dump(actividades,archivo, indent=4)  
            print("Actividades actualizadas")
            return actividades
        else:
             print("Actividad no actualizada, Repetida")   
             return actividades  


nueva_actividad =  {
            "Nombre": "Estudiar python",
            "Fecha": "13/1/26",
            "Estado" : "Pendiente"

        }
print(guardar_actividades(nueva_actividad))
