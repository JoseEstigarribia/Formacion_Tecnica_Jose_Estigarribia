## Caso 003 - Algunas Paginas no Cargan

# Escenario

La PC esta Conectada a Wifi sin Problemas aparentes, Icono wifi Marca conexión OK.
Los demas disposítivos Funcíonando correctamente en misma red.
La PC carga la mayoría de de Paginas Webs Correctamente, pero al querer loguarse al Instagram de la
empresa, no deja ingresar.
Chequeo mi Gateway si puedo conectarme a internet.


# ❓ Preguntas

¿Dónde se encuentra el problema?

¿Qué indica tener IP válida pero que no me Carguen paginas?

¿Qué comandos se pueden utilizar para diagnosticar?

¿Cómo validar que la solución fue exitosa?

# Diágnostico

Observando alrededor los demas dispositivos de la empresa todos funcionan correctamente,

Pienso que el problema es local de mi PC.

Al ir probando Mi conexion Gateway, Detecto que IP es Valido. 

Por medio de ping Verifico que Funciona por nombre de Dominio y por IP, DNS OK. 

Me queda Revisar el FireWall quizas esta bloqueando algunos Apps, Puertos, Dominios.



# 🛠️ Comandos / Herramientas 

ipconfig
ping 192.168.1.1
ping 8.8.8.8
ping google.com
netsh advfirewall show allprofiles

## 🔍 Pasos de verificación

Verificar IP, gateway y DNS

Ping al router

Ping a IP pública (8.8.8.8)

Ping por nombre de dominio

Detectar si el fallo es DNS

Aplicar solución:

Restablecer Conexión


## 🏁 Conclusión

no pude sacar una conclucion por que no se que procedimiento hacer para solucionar este problema 
ni que esperar al ejecurar comando netsh advfirewall show allprofiles