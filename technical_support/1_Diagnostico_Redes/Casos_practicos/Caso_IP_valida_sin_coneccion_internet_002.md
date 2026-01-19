## Caso 002- Sin conexion a internet IP Valida

# Escenario
PC conectada por WiFi o cable Ethernet.
El ícono de red indica conexión activa (sin signo de error).
Al ejecutar ipconfig, la PC obtiene una IP válida (192.168.1.x).

Sin embargo:

*No navega por Internet
*Las páginas no cargan

Otros dispositivos en la red sí tienen Internet.

# ❓ Preguntas

¿Dónde se encuentra el problema?

¿Qué indica tener IP válida pero no Internet?

¿Qué comandos se pueden utilizar para diagnosticar?

¿Cómo validar que la solución fue exitosa?

# Diágnostico
Otros dispositivos conectados la misma red, funcionan bien. Por lo cual me da un indicio de que es un problema local (mi PC).
Con esa misma información descartamos un problema Gateway, el router funciona bien en otros dispositivos.
El IP es Valido nos dice que DHCP Funciona correctamente.
Verifico ping a 8.8.8.8 funciona.
El ping a un nombre de dominio (google.com) no responde.

Esto indica un problema en la resolución DNS, ya que la PC puede comunicarse por IP pero no resolver nombres de dominio.


# 🛠️ Comandos / Herramientas 
ipconfig
ping 192.168.1.1
ping 8.8.8.8
ping google.com
ipconfig /flushdns

# 🔍 Pasos de verificación 

Verificar IP, gateway y DNS

Ping al router

Ping a IP pública (8.8.8.8)

Ping por nombre de dominio

Detectar si el fallo es DNS

Aplicar solución:
- Ejecutar ipconfig /flushdns
- (Opcional) Configurar DNS manuales (8.8.8.8 / 1.1.1.1)

Revalidar conectividad

# Conclusion
El problema no era la conectividad a Internet, sino un fallo en la resolución DNS local de la PC.

La conexión a la red y el acceso a Internet estaban operativos, El servidor DNS configurado en la PC no respondía correctamente
a las consultas de resolución de nombres.
Esto se comprobó al poder hacer ping a direcciones IP públicas, pero no a dominios.
