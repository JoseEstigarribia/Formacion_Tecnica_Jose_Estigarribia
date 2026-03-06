
## 📡 Modelo OSI

Modelo teórico de 7 capas para diagnosticar problemas de red.
Se analiza de abajo hacia arriba.

| Capa | Nombre | Qué hace | Ejemplo real |
|------|--------|----------|--------------|
| 7 | Aplicación | Lo que ve el usuario | Chrome, Outlook |
| 6 | Presentación | Cifrado y formato | HTTPS, JPG |
| 5 | Sesión | Abre y mantiene conexiones | Login Gmail |
| 4 | Transporte | Divide datos, puertos | TCP, UDP |
| 3 | Red | Direccionamiento IP | Router, IP |
| 2 | Enlace | Comunicación local | Switch, MAC |
| 1 | Física | Hardware y señal | Cable, WiFi |

### 🔧 Cómo uso OSI para diagnosticar
Cuando un usuario no tiene internet arranco desde abajo:
1. ¿Está el cable conectado? ¿Enciende la luz? → Capa 1
2. ¿El switch reconoce el dispositivo? → Capa 2
3. ¿Tiene IP correcta? ¿Hace ping al gateway? → Capa 3
4. ¿El servicio responde en el puerto correcto? → Capa 4
5. ¿La aplicación funciona? → Capa 7
