
## 🔄 Modelo TCP/IP

Modelo práctico de 4 capas. Es el que realmente
usan las redes hoy.

| TCP/IP | Equivale a OSI | Protocolos |
|--------|---------------|------------|
| Aplicación | Capas 5-6-7 | HTTP, HTTPS, DNS, DHCP |
| Transporte | Capa 4 | TCP, UDP |
| Internet | Capa 3 | IP, ICMP |
| Acceso a red | Capas 1-2 | Ethernet, WiFi |

### TCP vs UDP

| | TCP | UDP |
|--|-----|-----|
| Confiabilidad | Confirma entrega | No confirma |
| Velocidad | Más lento | Más rápido |
| Uso | Web, email, archivos | Streaming, llamadas, juegos |

### Three-way handshake
Antes de enviar datos TCP confirma la conexión en 3 pasos:
- **SYN** — "Quiero conectarme, ¿me escuchás?"
- **SYN-ACK** — "Te escucho, yo también estoy listo."
- **ACK** — "Perfecto, arrancamos."

Si el handshake no completa → no hay conexión TCP.
Causa probable: servidor caído, firewall bloqueando, puerto cerrado.

### Puertos importantes
| Puerto | Protocolo | Uso |
|--------|-----------|-----|
| 80 | HTTP | Web sin cifrado |
| 443 | HTTPS | Web con cifrado |
| 3389 | RDP | Escritorio remoto |
| 22 | SSH | Acceso remoto Linux |
| 21 | FTP | Transferencia archivos |
