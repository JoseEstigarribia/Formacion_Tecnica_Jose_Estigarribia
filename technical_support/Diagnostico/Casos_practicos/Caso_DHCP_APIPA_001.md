# Caso 001 – Error DHCP / IP 169.254 (APIPA)
## 🧩 Escenario

PC conectada por WiFi.
Ícono de red con signo de admiración.
Al ejecutar ipconfig, la PC obtiene una IP 169.254.x.x.

Un celular conectado a la misma red WiFi sí tiene acceso a Internet.

## ❓ Preguntas

¿Dónde se encuentra el problema?

¿Qué significa una IP 169.254.x.x?

¿Qué comandos se pueden utilizar para resolverlo?

¿Cómo validar que la solución fue exitosa?

## 🟢 Diagnóstico

El proveedor de Internet funciona correctamente (el celular navega).

El router se encuentra operativo, pero la PC no recibe una IP válida.

La dirección 169.254.x.x (APIPA) indica que Windows no recibió respuesta del servidor DHCP.

El problema se localiza en la asignación DHCP entre el router y la PC.

## 🛠️ Comandos / Herramientas
ipconfig /release
ipconfig /renew


Opcional:

ipconfig /flushdns

## 🔍 Pasos de verificación

Confirmar que la PC obtenga una IP válida (192.168.x.x).

Realizar ping al router:

ping 192.168.1.1


Probar conectividad a Internet:

ping 8.8.8.8


Probar resolución DNS:

ping google.com


Si falla la resolución DNS, limpiar caché con ipconfig /flushdns.

## 🏁 Conclusión

Se restableció correctamente la asignación DHCP.
La PC obtuvo una IP válida y recuperó el acceso a Internet.
Diagnóstico y resolución realizados de forma ordenada y efectiva.
