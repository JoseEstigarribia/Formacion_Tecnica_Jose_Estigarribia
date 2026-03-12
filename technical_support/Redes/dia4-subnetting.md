# 🌐 Día 4 — Subnetting y VLSM

Práctica de cálculo de subredes aplicado a casos reales
de diseño de redes en entornos empresariales.

---

## ¿Para qué sirve el subnetting?

Dividir una red grande en subredes más chicas para:
- Reducir el tráfico broadcast
- Mejorar la seguridad separando sectores
- Organizar la red por departamentos

---

## La máscara de red

Cada IP tiene dos partes — red y host.
La máscara indica dónde termina una y empieza la otra.
```
IP:      192.168.1.56
Máscara: 255.255.255.0  =  /24
Red:     192.168.1
Host:    .56
```

---

## Tabla de referencia rápida

| Notación | Máscara | Hosts disponibles |
|----------|---------|-------------------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

Regla: cada vez que sumás 1 al prefijo, 
los hosts disponibles se dividen a la mitad.

---

## Las tres IPs especiales de cada red

| IP | Función | Se asigna a dispositivos |
|----|---------|--------------------------|
| Primera (.0) | Dirección de red | No |
| Segunda (.1) | Gateway (router) | No — es del router |
| Última (.255 en /24) | Broadcast | No |

---

## Ejercicio resuelto — Red para PyME

**Situación:** empresa con 50 empleados, red 192.168.5.0/24

| Campo | Valor |
|-------|-------|
| Red | 192.168.5.0 |
| Máscara | 255.255.255.0 /24 |
| Gateway | 192.168.5.1 |
| Rango usable | 192.168.5.2 — 192.168.5.254 |
| Broadcast | 192.168.5.255 |
| Hosts disponibles | 254 — sobran ~200 slots |

**Conclusión:** Una /24 alcanza. Si quisiera optimizar
podría usar /26 y dividir en 3 subredes separadas.

---

## VLSM — Subredes de tamaño variable

Cuando cada sector necesita una cantidad distinta de hosts
usamos VLSM para no desperdiciar IPs.

**Situación:** empresa con 3 sectores en 192.168.1.0/24

| Sector | Empleados | Máscara elegida | Hosts disponibles |
|--------|-----------|-----------------|-------------------|
| Ventas | 30 | /27 | 30 — justo |
| IT | 10 | /28 | 14 — alcanza |
| Gerencia | 5 | /29 | 6 — alcanza |

**Cálculo de cada subred:**

**Ventas /27**
- Red: 192.168.1.0
- Gateway: 192.168.1.1
- Rango usable: 192.168.1.2 — 192.168.1.30
- Broadcast: 192.168.1.31

**IT /28**
- Red: 192.168.1.32
- Gateway: 192.168.1.33
- Rango usable: 192.168.1.34 — 192.168.1.46
- Broadcast: 192.168.1.47

**Gerencia /29**
- Red: 192.168.1.48
- Gateway: 192.168.1.49
- Rango usable: 192.168.1.50 — 192.168.1.54
- Broadcast: 192.168.1.55

**El router tiene una IP en cada subred** — una interfaz
por cada red que conecta. Es el que permite la
comunicación entre sectores.

---

## 📌 Aprendizajes clave

- /24 = 254 hosts, la más común en redes domésticas y PyMEs
- VLSM permite usar la máscara justa para cada sector
- Cada subred tiene su propia IP de red, gateway y broadcast
- El router tiene una interfaz en cada subred que conecta
- La IP .0 es la red, la última es broadcast — nunca se asignan
