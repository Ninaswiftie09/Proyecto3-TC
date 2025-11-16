# Proyecto 3 — Simulador de Máquina de Turing

## Integrantes
- **Nina Nájera — 231088**
- **Jorge Palacios — 231385**
  
## Link al video explicativo 

https://youtu.be/hssKuYobyHw 

## Descripción del proyecto
En este proyecto se implementó un simulador de Máquina de Turing de una cinta, capaz de leer una definición formal en un archivo YAML, cargar su conjunto de estados, alfabeto, transiciones y entradas, y luego ejecutar cada cadena paso por paso.

El simulador genera las descripciones instantáneas (IDs) en cada paso de la ejecución, mostrando cómo avanza el cabezal en la cinta, qué estado toma la máquina y cuándo se detiene. Al finalizar la ejecución de cada cadena, se indica si fue aceptada o rechazada.

---

## Requisitos

### Python
El proyecto se desarrolló utilizando **Python 3.13 (64 bits)**.

### Librerías necesarias
Solo se utiliza una librería externa:

- `pyyaml`
  Se instala con:
  ```
  pip install pyyaml
  ```

---

## Estructura del proyecto

A continuación se muestra una breve descripción de cada archivo:

### `parser_mt.py`
Se encarga de leer y procesar el archivo YAML. Extrae los estados, alfabetos, transiciones y cadenas que serán simuladas.

### `tape.py`
Implementa la cinta de la Máquina de Turing. Se maneja la lectura, escritura, movimientos del cabezal y la forma en que se muestran las IDs.

### `turing_machine.py`
Guarda la definición formal de la Máquina de Turing y proporciona la función que permite buscar la transición correspondiente según el estado actual y el símbolo leído.

### `simulator.py`
Simula la ejecución de la máquina. Aplica las transiciones, mueve el cabezal, genera las IDs y determina si la cadena es aceptada o rechazada.

### `main.py`
Es el archivo principal. Carga la configuración del YAML, crea la máquina y ejecuta la simulación sobre todas las entradas definidas.

### `mt_reconocedora.yaml`
Archivo que contiene la definición formal de la Máquina de Turing usada para el proceso reconocedor.  
Se implementó una MT que reconoce cadenas del lenguaje {aⁿbⁿ | n ≥ 1}.  

### `mt_alteradora.yaml`
Archivo que contiene la definición formal de la Máquina de Turing usada para el proceso alterador.  
Esta MT toma la cadena original y genera su versión invertida en la misma cinta.  

---

## Cómo correr el proyecto

1. Clonar el repositorio:
   ```
   git clone https://github.com/Ninaswiftie09/Proyecto3-TC
   ```

2. Instalar la librería necesaria:
   ```
   pip install pyyaml
   ```

3. Ejecutar el archivo principal:
   ```
   python main.py
   ```

4. El programa correrá todas las entradas del archivo `mt.yaml`, imprimirá todas las IDs y el resultado final para cada cadena.

---

## Notas finales
- El simulador funciona únicamente para Máquinas de Turing de una cinta, como lo solicita el proyecto.
- La arquitectura se diseñó para ser clara y modular, cumpliendo con todos los requisitos de parsing, ejecución y visualización de IDs.
- Para cambiar de máquina o modificar el lenguaje a reconocer, se debe escoger entre los 2 archivos .yaml.

## Enlace del vídeo de Youtube
- 
