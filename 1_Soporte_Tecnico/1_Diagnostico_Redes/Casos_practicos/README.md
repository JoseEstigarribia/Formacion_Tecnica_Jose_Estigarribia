
Caso 001 – Error DHCP / IP 169.254 (APIPA)
🧩 Escenario
PC conectada por WiFi. Ícono de red con signo de admiración.
Al ejecutar ipconfig, aparece IP 169.254.x.x.

Un celular conectado al mismo WiFi sí tiene Internet.

❓ Preguntas
¿Dónde está el problema?
¿Qué significa esa IP?
¿Qué comandos usarías?
¿Qué pasos seguirías para validar la solución?
🟢 Respuestas
1. Ubicación del problema:
El proveedor funciona (el celular tiene Internet).
El router funciona parcialmente.
El problema es la asignación DHCP entre router y PC.

2. Significado de la IP:
169.254.x.x es APIPA, una IP autogenerada por Windows cuando no recibe IP por DHCP.

3. Comandos a usar: ipconfig /release ipconfig /renew

markdown Copiar código

4. Pasos:

Verificar que ahora tome una IP válida (192.168.x.x)
Hacer ping al router (192.168.1.1)
Hacer ping a Internet (8.8.8.8)
Hacer ping por DNS (google.com)
Si falla DNS → ipconfig /flushdns
🏁 Conclusión
La PC recuperó IP válida y volvió a tener acceso a Internet.
Diagnóstico correcto y ordenado.
