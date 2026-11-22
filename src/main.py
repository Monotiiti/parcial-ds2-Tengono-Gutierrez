import json
import os

from pymongo import MongoClient

from modelo import CampanaPruebas

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# si el servidor pide usuario y clave, se define la variable de entorno MONGO_URI
URI = os.environ.get("MONGO_URI", "mongodb://127.0.0.1:27017")


def leer_pruebas():


    try:
        cliente = MongoClient(URI, serverSelectionTimeoutMS=3000)
        docs = list(cliente["HuilaSoft"]["Pruebas"].find({}, {"_id": 0}))
        print(f"Datos leídos de MongoDB: {len(docs)} documentos")

    except Exception as error:

        print("No se pudo leer MongoDB:", error)
        print("Se usa la exportación de mongo/exportaciones/")
        ruta = os.path.join(RAIZ, "mongo", "exportaciones", "HuilaSoft.Pruebas.json")
        with open(ruta, encoding="utf-8") as f:
            docs = json.load(f)

    return docs


def main():
    
    campana = CampanaPruebas(leer_pruebas())
    a, b = campana.ajustar()
    print("Acumulados reales:", campana.acumulados.tolist())
    print(f"a = {a:.4f}  b = {b:.6f}")
    print(f"Defectos restantes si se libera hoy: {campana.restantes():.2f}")
    print(f"Semana en que se descubre el 95 %: {campana.semana_95():.2f}")
    campana.graficar(os.path.join(RAIZ, "graficas", "resultado.png"))
    print("Gráfica guardada en graficas/resultado.png")


if __name__ == "__main__":
    main()
