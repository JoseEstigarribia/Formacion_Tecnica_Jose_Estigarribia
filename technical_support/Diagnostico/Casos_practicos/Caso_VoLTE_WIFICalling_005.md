## Caso 005 – Falla intermitente en llamadas entrantes

Tecnologías involucradas: VoLTE / Wi-Fi Calling / Red móvil

## 🧩 Síntoma

El usuario no recibe llamadas entrantes.
Las llamadas derivan directamente al buzón de voz, sin notificación ni registro de llamadas perdidas.

## 🌐 Contexto

Dispositivo móvil con chip nuevo

VoLTE habilitado

Llamadas por Wi-Fi habilitadas

Zona con cobertura móvil deficiente

## 🔍 Observaciones iniciales

Redes 2G y 3G sin señal (modo “solo llamadas de emergencia”)

Red 4G disponible, con señal inestable en interiores

Señal más estable en exteriores

De 10 llamadas de prueba, solo 1 ingresó correctamente

## ❓ Preguntas de diagnóstico

¿Se trata de una falla de hardware o configuración?

¿La calidad de cobertura afecta los servicios de voz avanzada?

¿Qué configuración prioriza estabilidad por sobre calidad de llamada?

## 🧠 Diagnóstico

Se descarta falla de hardware, ya que:

El equipo funciona correctamente para datos móviles

La señal varía según el entorno

El problema se asocia a:

Cobertura deficiente

Uso de servicios de voz avanzada (VoLTE / Wi-Fi Calling), que requieren mayor estabilidad de red

La falla afecta exclusivamente al servicio de voz.

## 🛠️ Acciones realizadas

Selección manual de tipo de red (2G / 3G / 4G)

Desactivación de llamadas por Wi-Fi

Desactivación de VoLTE

Pruebas de llamadas entrantes para validación

## 🏁 Resultado y validación

Configuración más estable:

4G activo solo para datos

VoLTE desactivado

Llamadas por Wi-Fi desactivadas

Resultado:

4/4 llamadas entrantes recibidas correctamente

Notificaciones y registros funcionando con normalidad

## 📌 Conclusión técnica

En entornos con cobertura deficiente, los servicios de voz avanzada pueden degradar la recepción de llamadas. Priorizar configuraciones simples mejora la estabilidad del servicio.