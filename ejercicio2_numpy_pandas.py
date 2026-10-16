# Ejercicio 2: NumPy y Pandas
# Mismos requerimientos que el ejercicio 1, con NumPy (arreglos) y Pandas (leer,
# organizar, filtrar y agrupar). Lee el mismo calificaciones.csv.
import time

import numpy as np
import pandas as pd


def procesar(ruta):
    """Ejecuta la lectura y todo el procesamiento. Lo que se mide en el benchmark."""
    # ---------- Lectura y organización con Pandas ----------
    df = pd.read_csv(ruta)
    notas = df[["Calificación1", "Calificación2", "Calificación3"]].to_numpy(dtype=float)

    # ---------- Cálculos con NumPy ----------
    df["Final"] = notas.mean(axis=1)                # promedio de las tres notas
    df["Estado"] = np.where(df["Final"] >= 70, "Aprobado", "Reprobado")

    # ---------- Agrupaciones con Pandas ----------
    promedios = df.groupby("Asignatura")["Final"].mean()
    aprobacion = (
        df.assign(aprobado=(df["Estado"] == "Aprobado"))
        .groupby("Asignatura")["aprobado"].mean() * 100
    )
    menor = promedios.idxmin()
    casos = df.loc[df["Final"] < 70, ["Matricula", "Asignatura", "Final"]]

    return df, promedios, aprobacion, menor, casos


if __name__ == "__main__":
    inicio = time.perf_counter()
    df, promedios, aprobacion, menor, casos = procesar("calificaciones.csv")
    tiempo = time.perf_counter() - inicio

    # ---------- Resultados (excluido de la medición) ----------
    print("Primeros 5 registros clasificados:")
    print(df[["Matricula", "Asignatura", "Final", "Estado"]].head().to_string(index=False))
    print("\nPromedio por asignatura:")
    print(promedios.round(2).to_string())
    print("\nPorcentaje de aprobación por asignatura:")
    print(aprobacion.round(1).to_string())
    print(f"\nAsignatura con menor promedio: {menor} ({promedios[menor]:.2f})")
    print(f"\nRegistros con calificación < 70: {len(casos)} (primeros 5):")
    print(casos.head().to_string(index=False))
    print(f"\nTiempo de lectura + procesamiento: {tiempo * 1000:.2f} ms")
