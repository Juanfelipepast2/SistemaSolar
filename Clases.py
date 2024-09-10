import pandas as pd

class Planeta:
    def __init__(self, nombre, diametro, distanciaAlSol):
        self.nombre = nombre
        self.diametro = diametro        
        self.distanciaAlSol = distanciaAlSol

    def __strsd__(self):
        return f"{self.nombre}\t{"%.2f" % self.diametro}\t\t{"%.2f" % self.distanciaAlSol}"
    


class MedidaAlternativa:
    def __init__(self, nombre, unidadDeMedida: str, valor):


        self.nombre = nombre
        self.unidadDeMedida = unidadDeMedida
        self.valor = valor
        self.valorKm = 1        
        self.diametroOriginal = 0
        self.idPlanetaElegido = 0

    def setValorKm(self, valor):
        self.valor = valor
        if self.unidadDeMedida == "cm":
            self.valorKm = valor/100000
        elif self.unidadDeMedida == "m":
            self.valorKm = valor/1000
        else:
            self.valorKm = valor                
    

class SistemaSolar:
    def __init__(self):   
        self.medidaAlternativa = MedidaAlternativa(None, "km", 1)

        self.planetas = [
            Planeta("Mercurio", 2439.7 * 2, 57910000),
            Planeta("Venus", 6051.8 * 2, 108200000),
            Planeta("Tierra", 6371 * 2, 149600000),
            Planeta("Marte", 3389.5 * 2, 227900000),
            Planeta("Júpiter", 69911 * 2, 778500000),
            Planeta("Saturno", 58232 * 2, 1434000000),
            Planeta("Urano", 25362 * 2, 2871000000),
            Planeta("Neptuno", 24622 * 2, 4495000000),
            Planeta("Luna", 3480, 149600000),
        ]                

    def cambioTamano(self, idPlaneta):
        self.medidaAlternativa.idPlanetaElegido = idPlaneta
        diametroTemp = (self.planetas[idPlaneta].diametro) #cambio de diametro        
        self.medidaAlternativa.diametroOriginal = self.planetas[idPlaneta].diametro
        for i in range(len(self.planetas)):
            if i == idPlaneta:
                self.planetas[i].diametro = self.medidaAlternativa.valor
                self.planetas[i].distanciaAlSol = (self.medidaAlternativa.valorKm * self.planetas[i].distanciaAlSol)/diametroTemp                
            else:
                self.planetas[i].diametro = ((self.medidaAlternativa.valor * self.planetas[i].diametro) / diametroTemp)
                self.planetas[i].distanciaAlSol = ((self.medidaAlternativa.valorKm * self.planetas[i].distanciaAlSol) / diametroTemp)                        


    def distanciaTierraLuna(self):

        return ((384400)* self.medidaAlternativa.valorKm) / self.medidaAlternativa.diametroOriginal if self.medidaAlternativa.valor != 1 else 384400

    def distanciaEntrePlanetas(self, idPlaneta1, idPlaneta2):

        return abs(self.planetas[idPlaneta1].distanciaAlSol - self.planetas[idPlaneta2].distanciaAlSol) if not (idPlaneta1 == 2 and idPlaneta2 == 8) else self.distanciaTierraLuna()

    
def imprimirPlanetas(planetas, medidaDiametro):
    df = pd.DataFrame([[x.nombre, x.diametro, x.distanciaAlSol] for x in planetas], columns=["Nombre", f"Diametro({medidaDiametro})", "Distancia al sol(km)"])
    df.index += 1
    print(df)



def main():
    #inicio del programa
    print("------------Bienvenido al sistema solar------------")
    print("------------------------------------------------")
    print("las caracteristicas de los planetas son las siguientes (si bien la luna no es un planeta, será tomada en cuenta como planeta para estas medidas):")    

    imprimirPlanetas(sistemaSolar.planetas, sistemaSolar.medidaAlternativa.unidadDeMedida)
    
    print("------------------------------------------------")
    print("Por favor, ingrese la medida alternativa que desea utilizar")

    sistemaSolar.medidaAlternativa.nombre = input("Ingrese el nombre de la medida alternativa: (algun objeto: ejemplo: pelota, canica, etc): ")
    sistemaSolar.medidaAlternativa.unidadDeMedida = medidaCorrecta()
    sistemaSolar.medidaAlternativa.setValorKm(float(input(f"Ingrese el valor de la medida alternativa en {sistemaSolar.medidaAlternativa.unidadDeMedida}: ")))
    
    idPlaneta = obtenerIdPlaneta()

    print(f"Si {sistemaSolar.planetas[idPlaneta].nombre} tuviera un diametro de un {sistemaSolar.medidaAlternativa.nombre}, las caracteristicas de los planetas serian las siguientes:")
    sistemaSolar.cambioTamano(idPlaneta)    
    imprimirPlanetas(sistemaSolar.planetas, sistemaSolar.medidaAlternativa.unidadDeMedida)


def medidaCorrecta() -> str:
    medida = ""
    while True:
        medida = input("Ingrese la unidad de medida (m, cm, km): ")
        if medida == "m" or medida == "cm" or medida == "km":
            return medida            
        else:
            print("La medida ingresada no es válida, por favor ingrese una medida válida")

def obtenerIdPlaneta() -> int:
    idPlaneta = 0
    while True:
        idTemp = int(input("Ingrese el indice del planeta deseado: ")) - 1
        if idPlaneta < 0 or idPlaneta > 8:
            print("El índice del planeta ingresado no es válido, por favor ingrese un índice válido")
        else:
            return idTemp    
        
def distanciaEntrePlanetas():
    print("Los indices de los planetas son los siguientes (si bien la luna no es un planeta, será tomada en cuenta como planeta para estas medidas): ")
    print("1. Mercurio", end="\t")
    print("2. Venus", end="\t")
    print("3. Tierra", end="\t")
    print("4. Marte", end="\t")
    print("5. Júpiter", end="\t")
    print("6. Saturno", end="\t")
    print("7. Urano", end="\t")
    print("8. Neptuno", end="\t")
    print("9. Luna")

    idPlaneta1 = obtenerIdPlaneta()
    idPlaneta2 = obtenerIdPlaneta()
    print(f"si {sistemaSolar.planetas[sistemaSolar.medidaAlternativa.idPlanetaElegido].nombre} fuera un/a {sistemaSolar.medidaAlternativa.nombre}, La distancia entre {sistemaSolar.planetas[idPlaneta1].nombre} y {sistemaSolar.planetas[idPlaneta2].nombre} es de {sistemaSolar.distanciaEntrePlanetas(idPlaneta1, idPlaneta2)} km")




def menu():
    print("------------SISTEMA SOLAR A ESCALA------------")
    print("------------------------------------------------")
    print("Bienvenido")
    while True:       
        print("1. Cambiar tamaño de un planeta")
        print("2. calcular Distancia entre planetas")
        print("3. Reestructurar sistema solar")
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            main()
        elif opcion == 2:
            distanciaEntrePlanetas()
        elif opcion == 3:
            global sistemaSolar
            sistemaSolar = SistemaSolar()
            print("Sistema solar reestructurado")
        elif opcion == 4:
            break
        else:
            print("Opción no válida, por favor ingrese una opción válida")
        print("------------------------------------------------")
    
sistemaSolar = SistemaSolar()
menu()