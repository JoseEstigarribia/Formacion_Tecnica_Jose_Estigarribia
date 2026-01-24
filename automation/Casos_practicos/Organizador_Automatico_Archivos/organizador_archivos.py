"""
Se necesita un script en Python que:

Recorra una carpeta

Identifique archivos por su extensión

Cree carpetas si no existen

Mueva los archivos según su tipo

Ejemplo:

.txt → Textos

.jpg / .png → Imágenes

.pdf → Documentos
"""

#Para trabajar con archivos necesito 2 cosas Ruta del archivo a explorar y lista 
# de extensiones a buscar
import os
import shutil
print(os.getcwd())
#ruta ="Archivos"
base = os.path.dirname(__file__)
ruta = os.path.join(base,"Archivos")

extensiones = {

    "textos" : ".txt",
    "imagenes" : [".jpg",".png"] ,
    "documentos" : ".pdf"
}
#Armar lista de archivos
archivos = os.listdir(ruta)


#nose detectar si es un archivo o carpeta

#como detecto la extension
#itero cada elemento de mi lista comparo con mis extensiones
for e in archivos:
    rutacompleta = os.path.join(ruta,e)#ruta del archivo en cada vuelta 1.2.3...
    
    if os.path.isfile(rutacompleta):#verifico que sea un archivo no carpeta
        nombre , extension = os.path.splitext(e)#obtengo nombre de archivo y su extension
        for categoria, valor in extensiones.items():#categoria y valor/es de las extensiones que quiero ordenar

            
            carpeta_destino = os.path.join(ruta,categoria)
            
            if isinstance(valor,list):
                 if extension in valor:
                    if os.path.exists(carpeta_destino):
                        shutil.move(rutacompleta, os.path.join(carpeta_destino, e))
                    else:
                        os.makedirs(carpeta_destino)
                 
                        shutil.move(rutacompleta, os.path.join(carpeta_destino, e))
                    break
            else:
                if extension == valor:
                    if os.path.exists(carpeta_destino):
                        shutil.move(rutacompleta, os.path.join(carpeta_destino, e))
                    else:
                        os.makedirs(carpeta_destino)
                        shutil.move(rutacompleta, os.path.join(carpeta_destino, e))
                    break                

        print("Archivo", nombre)
        print("Extension", extension)
