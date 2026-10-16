# Ejercicio 1: Python básico
# Solución con listas, diccionarios, ciclos, condicionales y funciones.
# Sin NumPy ni Pandas. Lee el mismo calificaciones.csv que la versión 2.
import csv
import time


# ---------- Lectura de datos ----------
def leer_registros(ruta):
    """Lee el CSV y devuelve una lista de diccionarios con las notas como enteros."""
    registros = []
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            registros.append({
                "matricula": fila["Matricula"],
                "asignatura": fila["Asignatura"],
                "notas": [
                    float(fila["Calificación1"]),
                    float(fila["Calificación2"]),
                    float(fila["Calificación3"]),
                ],
            })
    return registros


# ---------- Procesamiento ----------
def calcular_finales(registros):
    """Calificación final de cada registro: promedio de las tres notas."""
    finales = []
    for reg in registros:
        notas = reg["notas"]
        finales.append((reg["matricula"], reg["asignatura"], sum(notas) / len(notas)))
    return finales


def clasificar(finales):
    """Clasifica cada registro como 'Aprobado' (>= 70) o 'Reprobado' (< 70)."""
    estado = []
    for matricula, asignatura, final in finales:
        if final >= 70:
            estado.append((matricula, asignatura, final, "Aprobado"))
        else:
            estado.append((matricula, asignatura, final, "Reprobado"))
    return estado


def promedio_por_asignatura(registros):
    """Promedio de las calificaciones finales agrupadas por asignatura."""
    acumulado = {}
    conteo = {}
    for reg in registros:
        final = sum(reg["notas"]) / len(reg["notas"])
        asig = reg["asignatura"]
        acumulado[asig] = acumulado.get(asig, 0.0) + final
        conteo[asig] = conteo.get(asig, 0) + 1
    return {asig: acumulado[asig] / conteo[asig] for asig in acumulado}


def porcentaje_aprobacion(registros):
    """Porcentaje de registros aprobados (final >= 70) por asignatura."""
    totales = {}
    aprobados = {}
    for reg in registros:
        final = sum(reg["notas"]) / len(reg["notas"])
        asig = reg["asignatura"]
        totales[asig] = totales.get(asig, 0) + 1
        if final >= 70:
            aprobados[asig] = aprobados.get(asig, 0) + 1
    return {asig: 100.0 * aprobados[asig] / totales[asig] for asig in totales}


def asignatura_menor_promedio(promedios):
    """Asignatura con el promedio más bajo."""
    menor = None
    for asig, prom in promedios.items():
        if menor is None or prom < promedios[menor]:
            menor = asig
    return menor


def reprobados_inferiores_70(registros):
    """Matrículas y asignaturas con calificación final inferior a 70."""
    casos = []
    for reg in registros:
        final = sum(reg["notas"]) / len(reg["notas"])
        if final < 70:
            casos.append((reg["matricula"], reg["asignatura"], final))
    return casos


def procesar(ruta):
    """Ejecuta todo el procesamiento. Lo que se mide en el benchmark."""
    registros = leer_registros(ruta)
    finales = calcular_finales(registros)
    clasificados = clasificar(finales)
    promedios = promedio_por_asignatura(registros)
    porcentajes = porcentaje_aprobacion(registros)
    menor = asignatura_menor_promedio(promedios)
    casos = reprobados_inferiores_70(registros)
    return registros, clasificados, promedios, porcentajes, menor, casos


if __name__ == "__main__":
    inicio = time.perf_counter()
    registros, clasificados, promedios, porcentajes, menor, casos = procesar(
        "calificaciones.csv"
    )
    tiempo = time.perf_counter() - inicio

    # ---------- Resultados (excluido de la medición) ----------
    print("Primeros 5 registros clasificados:")
    for item in clasificados[:5]:
        print(" ", item)
    print("\nPromedio por asignatura:")
    for asig, prom in promedios.items():
        print(f"  {asig}: {prom:.2f}")
    print("\nPorcentaje de aprobación por asignatura:")
    for asig, pct in porcentajes.items():
        print(f"  {asig}: {pct:.1f}%")
    print(f"\nAsignatura con menor promedio: {menor} ({promedios[menor]:.2f})")
    print(f"\nRegistros con calificación < 70: {len(casos)} (primeros 5):")
    for item in casos[:5]:
        print(" ", item)
    print(f"\nTiempo de lectura + procesamiento: {tiempo * 1000:.2f} ms")
