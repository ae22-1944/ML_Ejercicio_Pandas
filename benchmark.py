# Benchmark: 5 mediciones por versión, reporta la mediana.
# Mide lectura + procesamiento, excluyendo importaciones e impresiones.
import statistics
import time

import ejercicio1_python_basico as e1
import ejercicio2_numpy_pandas as e2

RUTA = "calificaciones.csv"
N = 5

tiempos1 = []
for _ in range(N):
    t0 = time.perf_counter()
    e1.procesar(RUTA)
    tiempos1.append(time.perf_counter() - t0)

# primera corrida de pandas carga código interno; el enunciado pide 5 mediciones
tiempos2 = []
for _ in range(N):
    t0 = time.perf_counter()
    e2.procesar(RUTA)
    tiempos2.append(time.perf_counter() - t0)

print("Python básico (s):", [round(t, 4) for t in tiempos1])
print("  mediana:", round(statistics.median(tiempos1), 4))
print("NumPy/Pandas (s):", [round(t, 4) for t in tiempos2])
print("  mediana:", round(statistics.median(tiempos2), 4))

# Verificación de coincidencia de resultados
_, c1, p1, a1, m1, casos1 = e1.procesar(RUTA)
df, p2, a2, m2, casos2 = e2.procesar(RUTA)
assert set(p1) == set(p2.index), "asignaturas distintas"
assert all(abs(p1[k] - p2[k]) < 1e-9 for k in p1), "promedios distintos"
assert all(abs(a1[k] - a2[k]) < 1e-9 for k in a1), "porcentajes distintos"
assert m1 == m2, "asignatura menor distinta"
assert len(casos1) == len(casos2), "cantidad de casos < 70 distinta"
print("\nVERIFICACIÓN: resultados de ambas versiones coinciden ✓")
