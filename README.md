# FACTURACION-Simon-Yepes-Cano---Cesar-Junior-Ramirez

# 🧾 Sistema de Facturación por Sensores

## 📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema básico para calcular el **valor a pagar por la facturación de servicios de sensores de una empresa**.

El programa fue desarrollado tomando como referencia **facturas reales proporcionadas por la empresa**. A partir de estas facturas se obtuvieron los datos utilizados para realizar las pruebas, principalmente el **número de servicios**, el **valor unitario** y el **valor correspondiente a pagar**.

El objetivo principal es comprobar mediante pruebas que el cálculo realizado por el programa coincida con los valores registrados en las facturas.

Además, en este repositorio se encuentra un **audio en el que se explica el proceso de facturación por sensores de la empresa**, permitiendo conocer el contexto del proceso que se está representando mediante el programa.

---

## 🎯 Objetivo

Desarrollar y probar una función que permita calcular de manera sencilla el valor total a pagar por los servicios de sensores, teniendo en cuenta la cantidad de servicios, el valor unitario y el IVA correspondiente.

También se busca utilizar pruebas unitarias para verificar que el sistema funcione correctamente tanto con datos válidos como frente a diferentes casos de error.

---

## ⚙️ Funcionamiento

El programa recibe dos valores principales:

1. **Número de servicios:** cantidad de servicios de sensores que serán facturados.
2. **Valor unitario:** valor correspondiente a cada servicio.

Con estos datos se realiza el cálculo del valor a pagar, teniendo en cuenta un **IVA del 19%**.

### 🧮 Fórmula utilizada

**Valor a pagar = (Número de servicios × Valor unitario) + ((Número de servicios × Valor unitario) × 19%)**

De esta manera, primero se obtiene el valor correspondiente a los servicios y posteriormente se agrega el IVA del 19%.

---

## 📥 Valores de entrada

El programa recibe los siguientes datos:

| Entrada                    | Descripción                                             |
| -------------------------- | ------------------------------------------------------- |
| 🔢 **Número de servicios** | Cantidad de servicios de sensores que se deben facturar |
| 💰 **Valor unitario**      | Valor correspondiente a cada servicio                   |

Estos valores fueron obtenidos principalmente a partir de las **facturas utilizadas como referencia para el proyecto**.

---

## 📤 Valor de salida

El programa genera como resultado:

| Salida               | Descripción                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| 💵 **Valor a pagar** | Valor total que debe ser pagado por los servicios, incluyendo el IVA del 19% |

---

## 🧾 IVA

Para el proceso de facturación analizado en este proyecto se utiliza un **IVA del 19%**.

El IVA se aplica sobre el valor obtenido de multiplicar el número de servicios por el valor unitario.

---

## 🧪 Pruebas unitarias

Para comprobar el funcionamiento del programa se realizaron diferentes **pruebas unitarias utilizando Python y `unittest`**.

Las pruebas se construyeron utilizando información de **facturas reales de la empresa**, con diferentes clientes, cantidades de servicios y valores unitarios.

El objetivo de estas pruebas es verificar que el valor calculado por el programa corresponda al valor esperado de cada factura.

### 📊 Pruebas realizadas

Se realizaron pruebas con diferentes registros de facturación, entre ellos:

* Gamma
* Corlanc
* Locería
* Enka
* Cryogas
* Suministros de Colombia S.A.S.
* Materiales y Pinturas Sabaneta
* Moldes Itagüí
* Calcinación

Estas pruebas permiten comprobar el funcionamiento de la fórmula con diferentes valores y cantidades de servicios.

---

## ❌ Casos de error

Además de las pruebas con datos de las facturas, se desarrollaron **5 casos de error** con el objetivo de comprobar cómo se comporta el sistema cuando recibe datos de entrada incorrectos.

Entre los casos considerados se encuentran:

* 🔴 **Número de servicios igual a `0`.**
* 🔴 **Valor unitario igual a `0`.**
* 🔴 **Número de servicios con un valor inválido.**
* 🔴 **Valor unitario con un valor inválido.**
* 🔴 **Validaciones adicionales relacionadas con los datos de entrada.**

Estos casos permiten comprobar que el programa no solamente funciona con los valores normales de las facturas, sino que también se tienen en cuenta posibles errores al ingresar los datos.

---

## 🎧 Explicación del proceso

Dentro del repositorio se encuentra un **audio relacionado con el proyecto**.

En este audio se explica el **proceso de facturación por sensores de la empresa**, proporcionando el contexto necesario para comprender de dónde provienen los datos utilizados y cómo funciona el proceso que se está representando mediante el programa.

Por esta razón, se recomienda escuchar el audio como complemento de la información presentada en el código y en las pruebas.

---

## 📂 Contenido del repositorio

| Elemento         | Descripción                                                                     |
| ---------------- | ------------------------------------------------------------------------------- |
| 🐍 **Código**    | Contiene la implementación utilizada para realizar el cálculo de la facturación |
| 🧪 **Pruebas**   | Contiene las pruebas unitarias realizadas sobre la función                      |
| 🧾 **Facturas**  | Documentos utilizados como referencia para obtener los datos de las pruebas     |
| 🎧 **Audio**     | Explicación del proceso de facturación por sensores de la empresa               |
| 📄 **README.md** | Documento con la explicación general del proyecto                               |

---

## 🚀 Futuras implementaciones

Actualmente, el proyecto utiliza como referencia los datos encontrados en las **facturas reales proporcionadas por la empresa**. Por esta razón, los datos utilizados para las pruebas se encuentran relacionados con las situaciones y periodos registrados en dichas facturas.

Como una futura mejora, se busca implementar los **meses del servicio como una variable de entrada adicional**.

Actualmente, los meses no hacen parte de las entradas de la función, por lo que el sistema tiene una capacidad limitada para adaptarse a diferentes periodos de facturación.

### 🔮 ¿Qué permitiría esta mejora?

Al incluir los meses como una variable de entrada, el sistema podría:

* 📅 Trabajar con diferentes periodos de facturación.
* 🔄 Adaptarse a una cantidad variable de meses.
* 🧮 Realizar cálculos más dinámicos.
* 📈 Permitir una mayor variedad de casos de prueba.
* ⚙️ Representar de una manera más completa el proceso real de facturación de la empresa.

Esta implementación permitiría que el sistema no dependa únicamente de los valores establecidos a partir de las facturas utilizadas para este proyecto.

---

## 🛠️ Tecnologías utilizadas

| Tecnología      | Uso                                           |
| --------------- | --------------------------------------------- |
| 🐍 **Python**   | Desarrollo del programa                       |
| 🧪 **unittest** | Creación y ejecución de las pruebas unitarias |
| 🐙 **GitHub**   | Repositorio y almacenamiento del proyecto     |

---

## 📚 Metodología

El desarrollo del proyecto se realizó siguiendo un proceso basado en:

**Facturas de la empresa → Identificación de datos → Implementación del cálculo → Pruebas unitarias → Casos de error → Análisis de resultados**

De esta manera, el programa no se construyó únicamente a partir de datos ficticios, sino que se utilizaron **datos reales de facturación como referencia para las pruebas**.

---

## 👥 Autores

**Simon Yepes Cano**
**Cesar Junior Ramirez**

---

## 📌 Conclusión

El proyecto permite representar de manera sencilla el cálculo de la **facturación de servicios de sensores de una empresa**, utilizando como base información obtenida de facturas reales.

Mediante las pruebas unitarias se verifica que los resultados obtenidos por el programa sean consistentes con los valores esperados y, mediante los casos de error, se consideran diferentes situaciones en las que los datos de entrada pueden ser incorrectos.

Como siguiente paso, se plantea ampliar el sistema mediante la incorporación de los **meses del servicio como variable de entrada**, permitiendo que el programa sea más flexible y pueda adaptarse a diferentes periodos y situaciones de facturación.
