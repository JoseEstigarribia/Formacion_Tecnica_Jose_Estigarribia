🧠 Metodologías de Diagnóstico de Redes
(Nivel Inicial → Intermedio)
📌 1. Metodología “De adentro hacia afuera”

Este es el método más usado por técnicos de soporte porque te ordena mentalmente para no saltarte pasos.

1) Revisar el Dispositivo (PC / Celular)

¿Está conectado al WiFi o al cable?

Abrir Símbolo del sistema
ipconfig /all

Verificar:

IPv4 válida (ej: 192.168.x.x)

DNS configurado

Adaptador sin errores

Probar:

ping 192.168.1.x → router

ping 8.8.8.8 → internet

nslookup google.com → DNS

👉 Si falla acá, el problema es local del dispositivo.

2) Revisar el Router / Red Local

¿Responde al ping?
ping 192.168.1.x

¿Hay muchos equipos conectados al WiFi saturando?

¿Está repartiendo IP el DHCP?

¿Se puede entrar al panel del router (192.168.1.1)?*

👉 Si falla acá, el problema es de la red del hogar.

3) Revisar el Proveedor (ISP)

Ping a Google:
ping 8.8.8.8

Probar navegar con datos del celular (descartar PC)

Preguntar si hay cortes en la zona

Reiniciar ONT / módem

👉 Si falla acá, es problema del servicio externo.

📌 2. Metodología “Capa por capa” (OSI Simplificado)
1) Capa Física

Cable suelto o roto

Placa de red apagada

Señal WiFi débil

2) Capa Red

Dirección IP

Máscara

Gateway

DHCP

DNS

3) Capa Transporte

Ping

Latencia

Pérdida de paquetes

4) Capa Aplicación

Navegador

Programas específicos

Servidores web caídos

👉 Este método te ordena para saber dónde está realmente la falla.

📌 3. Fallas frecuentes y soluciones rápidas
🔥 A) IP inválida 169.254.x.x

Significa: DHCP falló, el router no te dio una IP.

Soluciones:

ipconfig /release
ipconfig /renew


Desactivar/activar WiFi

Reiniciar router

Cambiar cable

🔥 B) WiFi conectado pero sin internet

Ping al router

Ping a Google

Cambiar DNS

Desactivar VPN

Probar con otro dispositivo

🔥 C) DNS no funciona

Síntomas:

Google abre por IP (8.8.8.8) pero no por nombre ("google.com")

Soluciones:

Cambiar DNS manual:
8.8.8.8
8.8.4.4

Ejecutar:
ipconfig /flushdns

🔥 D) Página específica no abre

Puede ser un servidor caído

Problema de caché

Problema de DNS de la operadora

Solución:

Probar modo incógnito

Probar otro navegador

Cambiar DNS

📌 4. Checklist rápido para técnicos 

Este es paso a paso universal:

¿El dispositivo está conectado?

¿Tiene una IP válida?

¿Hay ping al router?

¿Hay ping a internet?

¿DNS responde?

¿Otro dispositivo funciona?

¿Router responde?

¿Proveedor está caído?

Si respondés estas preguntas, encontrás la falla siempre.

📌 5. Cómo practicar con estos métodos
✔ Resolver ejercicios 

✔ Hacer pruebas en PC:

Cambiar DNS

Desactivar adaptador y reactivarlo

Ver logs del Router

Hacer pings a distintas IP

Simular fallas desconectando el cable

Revisar el ipconfig varias veces

✔ Usar laboratorios online 

Cisco Packet Tracer

TryHackMe (redes básicas)

Netlab


📌 6. Cómo documentar lo aprendido


📁 /1_Soporte_Tecnico
 📄 teoria_metodologias_diagnostico.md (este archivo)
 📄 ejercicios_resueltos.md
 📄 comandos-practicos.md
 📄 casos_reales_resueltos.md
