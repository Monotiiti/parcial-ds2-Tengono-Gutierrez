import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


class CampanaPruebas:
    # modelo de Goel-Okumoto: m(t) = a * (1 - e^(-b*t))

    def __init__(self, defectos):

        # defectos: lista de documentos de la colección Pruebas
        # (campos semana y ndefectos)
        datos = sorted(defectos, key=lambda d: d["semana"])
        self.semanas = np.array([d["semana"] for d in datos])
        self.por_semana = np.array([d["ndefectos"] for d in datos])
        self.acumulados = np.cumsum(self.por_semana)
        self.a = None
        self.b = None

    def goel(self, t, a, b):

        return a * (1 - np.exp(-b * np.asarray(t)))

    def ajustar(self):
        # a y b se buscan con curve_fit usando los acumulados reales
        total = self.acumulados[-1]

        (a, b), _ = curve_fit(
            self.goel, 
            self.semanas, 
            self.acumulados,
            #valores iniciales de busqueda: a = 1.5 * total, b = 0.1
            p0=[total * 1.5, 0.1])
        
        self.a, self.b = a, b

        return a, b

    def restantes(self, t=None):

        # defectos que faltan por encontrar: a - m(t)
        if t is None:
            t = self.semanas[-1]
        return self.a - self.goel(t, self.a, self.b)

    def semana_95(self):

        # m(t) = 0.95a  ->  t = ln(20) / b
        return math.log(20) / self.b

    def graficar(self, ruta):

        t = np.linspace(0, self.semana_95() + 2, 200)
        plt.figure(figsize=(8, 5))
        plt.scatter(
            self.semanas,
            self.acumulados,
            color="red",
            label="Acumulados reales")
        
        plt.plot(
            t, 
            self.goel(t, self.a, self.b), 
            label="Curva ajustada")
        
        plt.axhline(
            self.a, 
            color="gray", 
            linestyle="--",
            label=f"a = {self.a:.1f}")
        
        plt.axvline(
            self.semana_95(),
            color="green", 
            linestyle=":",
            label=f"95 % en la semana {self.semana_95():.1f}")
        
        plt.xlabel("Semana")
        plt.ylabel("Defectos acumulados")
        plt.title("Campaña de pruebas v11.0 - HuilaSoft")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.savefig(ruta, dpi=150)
        plt.close()
