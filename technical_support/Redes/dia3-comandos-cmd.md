# 🖥️ Día 3 — Comandos de diagnóstico de red en CMD

Práctica real de comandos avanzados ejecutados en Windows.
Todos los outputs son de ejecución propia.

---

## 📋 Comandos practicados hoy

| Comando | Para qué sirve |
|---------|---------------|
| `netstat -an` | Ver todas las conexiones activas |
| `netstat -b` | Ver qué proceso usa cada conexión |
| `nslookup` | Diagnosticar problemas de DNS |

---

## 1. netstat -an

**¿Para qué sirve?**
Muestra todas las conexiones de red activas en el equipo
con IPs numéricas. Útil para ver qué puertos están 
escuchando y detectar conexiones sospechosas.

**Requiere:** CMD normal (sin administrador)

![netstat -an](./cmd-netstat-an.png)

**Las 4 columnas:**
- **Proto** → protocolo usado, TCP o UDP
- **Dirección local** → tu equipo y puerto
- **Dirección remota** → servidor destino y puerto
- **Estado** → situación de la conexión

**Estados importantes:**

| Estado | Significado |
|--------|------------|
| LISTENING | Puerto abierto esperando conexiones |
| ESTABLISHED | Conexión activa ahora mismo |
| TIME_WAIT | Conexión cerrándose ordenadamente |
| CLOSE_WAIT | El servidor cerró, esperando que cierre el cliente |

**Puertos importantes que reconocí:**
- `:445` → SMB, carpetas compartidas Windows
- `:135` → RPC, servicios internos Windows
- `:443` → HTTPS, navegación segura

**Uso real en soporte:**
Usuario no puede conectarse a un sistema. Ejecuto
`netstat -an` y busco conexión ESTABLISHED hacia ese
servidor. Si no aparece → problema de red o firewall.
Si aparece TIME_WAIT → el servidor está rechazando.

---

## 2. netstat -b

**¿Para qué sirve?**
Igual que `-an` pero además muestra qué programa
está usando cada conexión. Requiere permisos de
administrador — aprendí qué es UAC con este comando.

**Requiere:** CMD como administrador (clic derecho → 
"Ejecutar como administrador")

![netstat -b](./cmd-netstat-b.png)

**Lo que aprendí analizando el output:**
- `Theft_Deterrent_agent.exe` → sistema antirrobo
  institucional, conexiones locales normales
- `AVGBrowser.exe` → navegador, conexiones HTTPS
  a servidores externos normales
- `RiotClientServices.exe` → cliente de juego en
  CLOSE_WAIT, instalación incompleta en segundo plano

**¿Cómo detecto una conexión sospechosa?**
Tres criterios:
1. ¿El proceso tiene nombre reconocible?
2. ¿La IP destino es de empresa conocida?
3. ¿Tiene sentido que ese proceso se conecte afuera?

Si las tres respuestas son NO → investigar más.

**Dato importante — UAC:**
Al ejecutar `netstat -b` sin permisos de admin recibí:
`La operación solicitada requiere elevación`
UAC (User Account Control) es el sistema de Windows
que controla qué acciones necesitan permisos elevados.
En entornos empresariales los usuarios no tienen admin
— el técnico usa sus propias credenciales para escalar.

---

## 3. nslookup

**¿Para qué sirve?**
Consulta el servidor DNS para resolver nombres de dominio
a IPs. Herramienta clave para diagnosticar problemas de
DNS en segundos.

**Requiere:** CMD normal

![nslookup google.com](./cmd-nslookup.png)

**Análisis del output:**
```
Servidor:  dns.google
Address:   8.8.8.8
```
Mi PC usa el DNS público de Google (8.8.8.8) para
resolver nombres. Configuración común y confiable.
```
Respuesta no autoritativa:
Nombre:  google.com
Addresses: 142.251.128.238
```
"No autoritativa" = respuesta desde caché, no del
servidor DNS original. Normal en la práctica.
Dos IPs devueltas: una IPv4 y una IPv6 — Google tiene
servidores distribuidos globalmente.

**Variantes útiles:**
```
nslookup google.com          → nombre a IP
nslookup 142.251.128.238     → IP a nombre (inverso)  
nslookup google.com 1.1.1.1  → consultar DNS específico
```

**Uso real en soporte:**
Usuario no puede abrir páginas pero tiene internet.
Ejecuto `nslookup google.com`:
- Si devuelve IP → DNS funciona, problema en otro lado
- Si falla → problema de DNS → cambiar a 8.8.8.8
  manualmente en configuración de red

---

## 🔑 Resumen del día

| Comando | Cuándo lo uso | Necesita admin |
|---------|--------------|----------------|
| `netstat -an` | Ver conexiones y puertos | No |
| `netstat -b` | Identificar procesos sospechosos | Sí |
| `nslookup dominio` | Diagnosticar DNS | No |

## 📌 Aprendizajes clave
- Los puertos efímeros (49152-65535) los asigna Windows
  automáticamente para conexiones salientes
- HTTP no es malicioso por ser HTTP — importa el proceso
  y la IP destino
- UAC protege el sistema requiriendo elevación para
  comandos sensibles
- nslookup en 5 segundos dice si el problema es de DNS
