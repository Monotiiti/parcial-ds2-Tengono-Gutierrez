import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "src"))

from modelo import CampanaPruebas

DATOS = [{"semana": i + 1, "ndefectos": n}
         for i, n in enumerate([28, 23, 22, 17, 16, 12, 12, 9])]


def test_goel_en_cero():
    campana = CampanaPruebas(DATOS)
    assert campana.goel(0, 200, 0.15) == 0


def test_ajuste():
    campana = CampanaPruebas(DATOS)
    a, b = campana.ajustar()
    assert campana.acumulados[-1] == 139
    assert abs(a - 198.06) < 0.5
    assert abs(b - 0.1519) < 0.001
    assert abs(campana.restantes() - 58.77) < 0.5
    assert abs(campana.semana_95() - 19.73) < 0.1
