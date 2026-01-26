## Caso 004 - PC Lenta / Alto Consumo CPU o RAM

# Escenario

El usuario comenta que el arranque de la PC es muy lento.

Los programas que usa Demoran mas de lo normal en abrirse.

El ventilador de la PC anda mas fuerte que siempre, como que se fuerza mas.

Los demas equipos de la oficina son iguales en especificacion tecnicas y mismo uso,

pero funcionan mejor.


# ❓ Preguntas

¿Dónde se encuentra el problema?

¿es software?¿es hardware?¿es arranque?¿es malware?

¿Qué comandos se pueden utilizar para diagnosticar?

¿Cómo validar que la solución fue exitosa?

# Diágnostico

Observando alrededor los demas dispositivos de la empresa todos funcionan correctamente, teniendo misma

capacidad CPU, RAM, Disco, el problema es local de mi PC.

Al ir a revisar los programas de inicio de Windows (msconfig), Detecto que Abre automaticamente las 

Apps, Google Sheet, Gmail, CRM, Whatsapp, Spotify. 

Por medio de Administrador de tareas Verifico que las multiples ventanas de navegador dan picos de 

consumos elevados en RAM y CPU. Se debe a limitada memoria 4GB RAM y Menos de 20% del Disco duro libre.

Se revisaron cuales servicios necesarios se mantienen activos y cuales no (services.msc)



# 🛠️ Comandos / Herramientas 

Administrador de Tareas

msconfig

services.msc

Antivirus / Defender



## 🔍 Pasos de verificación

Verificar las aplicaciones necesarias para el Arranque de Windows, las que no son necesarias 

se quitaran del arranque sin tocar nada del sistema.(msconfig)

Verificaremos las Apps poco usadas las desinstalaremos para aumentar el espacio del 

disco.(Panel de control / Aplicaciones)

Verificamos el Navegador consume mucho, buscarmos desinstalar extensiones pesadas e innecesarias.

Ejecutaremos un analisis profundo del Antivirus para buscar y eliminar archivos malware.

Verificaremos que Servicos del sistemas no sean prioridad que esten activos o en segundo plano y no 

deberian, servicios desconocidos, etc.. los desactivaremos.(services.msc) 



## 🏁 Conclusión

El bajo rendimiento se debía a un alto consumo de recursos causado por aplicaciones en el inicio y 

procesos activos innecesarios.

Tras optimizar el arranque, liberar espacio en disco y descartar malware mediante escaneo, el sistema 

recuperó un funcionamiento normal.