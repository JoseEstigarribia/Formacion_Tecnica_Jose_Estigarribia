## Caso 005 – Falla intermitente en llamadas entrantes (VoLTE / Wi-Fi Calling)

### 🧩 Escenario

El usuario informa que no recibe llamadas entrantes.  
Las llamadas no generan notificaciones ni registros de llamadas perdidas, derivando directamente al buzón de voz.

Características del entorno:
- Dispositivo móvil con chip nuevo
- Llamadas por Wi-Fi habilitadas
- VoLTE habilitado
- Zona con cobertura móvil deficiente

Observaciones iniciales:
- Redes 2G y 3G seleccionadas manualmente no registran señal (modo “solo llamadas de emergencia”)
- Red 4G disponible, pero con señal inestable en interiores
- En exteriores la señal mejora
- De 10 llamadas de prueba, solo 1 fue recibida correctamente



### ❓ Preguntas de diagnóstico

- ¿El problema está relacionado con hardware o software?
- ¿Influye la cobertura de red en los servicios de voz avanzada?
- ¿Qué configuraciones permiten estabilizar las llamadas entrantes?
- ¿Cómo validar objetivamente la solución?



### 🔍 Diagnóstico

Se descarta inicialmente una falla de hardware, ya que:
- El dispositivo funciona correctamente para datos móviles
- La señal aparece y desaparece según el entorno

El problema se orienta a una **configuración de red y servicios de voz**, agravada por:
- Cobertura deficiente en la zona
- Uso de VoLTE y llamadas por Wi-Fi, que requieren estabilidad de red

Se observa que:
- Los datos móviles funcionan correctamente
- La falla se presenta principalmente en el servicio de voz



### 🛠️ Herramientas / Configuraciones utilizadas

- Configuración de redes móviles del dispositivo
- Selección manual de tipo de red (2G / 3G / 4G)
- Activación y desactivación de:
  - VoLTE (llamadas sobre 4G)
  - Llamadas mediante Wi-Fi



### 🔎 Pasos de verificación

1. Acceso a **Configuración → Redes móviles**
2. Pruebas manuales de conexión a redes 2G, 3G y 4G
3. Evaluación de recepción de señal en interiores y exteriores
4. Desactivación de llamadas por Wi-Fi
5. Desactivación de VoLTE
6. Realización de llamadas entrantes de prueba para validación



### 🏁 Conclusión

Tras múltiples pruebas, la configuración más estable fue:
- Red 4G activa **solo para datos**
- VoLTE desactivado
- Llamadas por Wi-Fi desactivadas

Resultados:
- 4 llamadas entrantes de prueba
- 4/4 llamadas recibidas correctamente
- Notificaciones y registros de llamadas funcionando con normalidad

**Conclusión técnica:**  
En entornos con cobertura deficiente, los servicios de voz avanzada (VoLTE / Wi-Fi Calling) pueden generar fallas en la recepción de llamadas. En estos casos, una configuración más simple ofrece mayor estabilidad.

