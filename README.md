# Análisis de rendimiento académico: Python básico vs. NumPy/Pandas

**Estudiante:** Adán Estévez (22-1944) **Asignatura ficticia agregada:** `Programación-AE-1944` (12
registros, notas entre 0 y 100)

## Descripción

La coordinación académica necesita identificar las asignaturas con menor rendimiento y los
estudiantes que requieren apoyo. Este proyecto resuelve los mismos seis requerimientos con dos
alternativas y las compara para recomendar una:

1. **`ejercicio1_python_basico.py`** — solo listas, diccionarios, ciclos, condicionales y funciones
   (sin NumPy ni Pandas). Lee el CSV con el módulo `csv`.
2. **`ejercicio2_numpy_pandas.py`** — NumPy para los cálculos sobre arreglos (`notas.mean(axis=1)`,
   `np.where`) y Pandas para leer, filtrar y agrupar (`read_csv`, `groupby`).
3. **`benchmark.py`** — mide lectura + procesamiento (excluye importaciones e impresiones), 5
   mediciones por versión, reporta la mediana, y verifica que ambas versiones produzcan resultados
   idénticos.
4. **`calificaciones.csv`** — los 1,000 registros originales del Excel + los 12 registros ficticios
   de la asignatura `Programación-AE-1944`.

## Requerimientos resueltos (ambas versiones)

- Calificación final de cada registro (promedio de las tres notas).
- Clasificación en aprobados (final ≥ 70) y reprobados (< 70).
- Promedio por asignatura.
- Porcentaje de aprobación por asignatura.
- Asignatura con menor promedio.
- Matrículas y asignaturas con calificación inferior a 70.

## Resultados académicos

| Asignatura                       | Promedio  | % Aprobación |
| -------------------------------- | --------- | ------------ |
| Bases de Datos                   | 76.13     | 65.5%        |
| Matemática Discreta              | 73.47     | 61.0%        |
| Programación web                 | 71.52     | 55.0%        |
| Estructura de datos Y Algoritmos | 69.34     | 47.0%        |
| Métodos estadísticos             | 65.97     | 41.0%        |
| **Programación-AE-1944**         | **46.78** | **8.3%**     |

- **Asignatura con menor promedio:** `Programación-AE-1944` (46.78), seguida de Métodos estadísticos
  (65.97). Ambas requieren intervención de la coordinación.
- **Registros con calificación < 70:** 472 de 1,012 (46.6%), es decir, 472 casos de estudiantes que
  requieren apoyo.

## Tabla comparativa

Ambas mediciones en el mismo equipo y con el mismo archivo. La medición incluye la lectura y el
procesamiento de los datos; excluye importaciones e impresiones.

| Criterio                                                      | Python básico                                                                                                                                                                      | NumPy / Pandas                                                                                                                                                              |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mediana de tiempo (5 corridas)                                | **2.2 ms**                                                                                                                                                                         | **1.7 ms**                                                                                                                                                                  |
| Líneas dedicadas al procesamiento (sin comentarios ni vacías) | 100                                                                                                                                                                                | 31                                                                                                                                                                          |
| Facilidad para comprender y modificar                         | Alta para quien solo conoce Python puro: cada paso es explícito (ciclos y diccionarios), pero cada nuevo requerimiento exige escribir una función nueva con acumuladores manuales. | Alta una vez se conocen Pandas: cada requerimiento son 1-2 líneas declarativas (`groupby`, `np.where`); agregar un requerimiento nuevo rara vez cambia el resto del código. |
| Dificultades encontradas                                      | Acumuladores manuales (`get`, conteo aparte) propensos a errores y repetitivos; el código crece rápido con cada requerimiento.                                                     | Curva de aprendizaje de la API (`axis`, `groupby`); sobrecarga en la primera ejecución mientras Pandas inicializa su código interno (visible en la primera medición).       |

Corridas individuales (segundos):

- Python básico: `[0.0026, 0.0020, 0.0022, 0.0021, 0.0023]` → mediana **0.0022 s**
- NumPy/Pandas: `[0.0028, 0.0017, 0.0015, 0.0019, 0.0015]` → mediana **0.0017 s**

Verificación: `benchmark.py` compara promedios, porcentajes, asignatura de menor promedio y cantidad
de casos < 70 entre ambas versiones y confirma que **coinciden exactamente**.

## Recomendación

**Se recomienda la alternativa de Python con NumPy y Pandas.**

Razones:

1. **Rendimiento:** la versión con Pandas procesó el archivo ~23% más rápido (mediana de 1.7 ms vs.
   2.2 ms). La ventaja crece con el volumen: las operaciones vectorizadas de NumPy no escalan
   linealmente con el tamaño del código, mientras que los ciclos de Python puro sí.
2. **Mantenibilidad:** el mismo trabajo requiere 31 líneas frente a 100. Cada nuevo requerimiento
   (otro filtro, otro agrupamiento) se resuelve con una línea declarativa en lugar de una función
   con acumuladores nuevos, lo que reduce directamente el riesgo de errores en reportes que la
   coordinación pedirá recurrentemente.
3. **Legibilidad para el propósito:** aunque los ciclos explícitos son más transparentes para un
   principiante, el equipo académico que mantendrá estos reportes se beneficia más de código corto y
   estándar del ecosistema de análisis de datos.
4. **Resultados idénticos:** la verificación automática confirma que la elección no altera los
   resultados académicos, solo la forma de obtenerlos.

Python básico sigue siendo válido como herramienta didáctica y para conjuntos de datos diminutos sin
dependencias externas, pero para el flujo de trabajo recurrente de la coordinación, NumPy y Pandas
es la alternativa más eficiente.

## Cómo ejecutar

```bash
python3 ejercicio1_python_basico.py    # versión Python básico
python3 ejercicio2_numpy_pandas.py     # versión NumPy y Pandas
python3 benchmark.py                   # mediciones y verificación
```

Requisitos: Python 3 con `numpy` y `pandas` (instalables con `pip install numpy pandas`). El archivo
`calificaciones.csv` debe estar en la misma carpeta.

## Bitácora de uso de IA

- **Agente utilizado:** Hermes Agent, modelo GLM vía OpenRouter.
- **Consultas relevantes realizadas** (textos con los que trabajé la asignación):
  1. "Analizar y solucionar esta problemática: la coordinación académica necesita identificar las
     asignaturas con menor rendimiento y los estudiantes que requieren apoyo, y determinar si es más
     eficiente procesar sus registros con Python básico o con Python + NumPy y Pandas. Debo
     desarrollar ambas soluciones, comparar resultados y tiempos de ejecución, y recomendar una
     alternativa basada en los datos y las mediciones."
  2. "El enunciado exige que la medición incluya la lectura y el procesamiento de los datos,
     excluyendo las importaciones y la impresión de resultados. ¿Cómo estructuro el código con
     `time.perf_counter()` para que el cronómetro cubra exactamente lo que pide, sin contaminar la
     medición con el `import pandas` ni con los `print`?"
  3. "Tengo dos implementaciones del mismo procesamiento, una con ciclos y diccionarios y otra con
     `groupby` de Pandas. ¿Cómo verifico de forma automática que ambas producen exactamente los
     mismos promedios por asignatura y porcentajes de aprobación sobre los 1,012 registros?"
  4. "¿Por qué la primera ejecución de la versión con Pandas es más lenta que las siguientes si el
     `import` está fuera del cronómetro? ¿Reportar la mediana de cinco corridas es suficiente para
     dar un tiempo representativo?"
- **Qué parte de la respuesta incorporé o modificué:**
  - Incorporé la estructura general: dos scripts paralelos con una función `procesar()` medible y un
    CSV único para ambas versiones.
  - Modifiqué la propuesta inicial del agente: en la versión básica separé la lectura del
    procesamiento en funciones nombradas para que el benchmark solo cronometre lectura +
    procesamiento; en la versión de Pandas usé `df.assign()` con una columna booleana para el
    porcentaje de aprobación en lugar de dos `groupby` separados.
- **Cómo comprobé que funcionaba correctamente:**
  - `benchmark.py` incluye aserciones que comparan promedios por asignatura, porcentajes de
    aprobación, la asignatura de menor promedio y la cantidad de casos < 70 entre ambas versiones:
    los resultados coinciden.
  - Revisé manualmente los primeros registros: la matrícula `26-0001` con notas 54/60/69 produce
    final 61.0 y estado "Reprobado" en ambas versiones.
  - Las 12 filas ficticias de `Programación-AE-1944` aparecen en los reportes de ambas versiones con
    promedio 46.78.
