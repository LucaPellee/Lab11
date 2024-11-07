import copy

from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.solBest = []

    def getYears(self):
        return DAO.getYear()

    def getColors(self):
        return DAO.getColors()

    def creaGrafo(self, color, anno):
        self.grafo.clear()
        listaNodi = DAO.getProducts(color)
        self.productMap = {}
        for n in listaNodi:
            self.productMap[n.Product_number] = n
        self.grafo.add_nodes_from(listaNodi)
        listCoppie = DAO.getArchi(anno)
        for c in listCoppie:
            if c[0] in self.productMap and c[1] in self.productMap:
                prod1 = self.productMap[c[0]]
                prod2 = self.productMap[c[1]]
                peso = c[2]
                self.grafo.add_edge(prod1, prod2, weight=peso)

    def cercaArchi(self):
        listaArchi = self.grafo.edges(data = True)
        listaArchiOrd = sorted(listaArchi, key=lambda x: x[2].get('weight', 0), reverse=True)
        listaFin = []
        for i in range(3):
            listaFin.append(listaArchiOrd[i])
        return listaFin

    def cercaNodiRip(self, listaArchi):
        listaNodi = []
        listaNodiTop = []
        for a in listaArchi:
            for i in range(2):
                if a[i] not in listaNodi:
                    listaNodi.append(a[i])
                else:
                    listaNodiTop.append(a[i])
        return listaNodiTop

    def getProducts(self, colore):
        return DAO.getProducts(colore)

    def getNumNodes(self):
        return len(list(self.grafo.nodes()))

    def getNumEdges(self):
        return len(list(self.grafo.edges()))

    def getPercorso(self,v0):
        parziale =[]
        self.ricorsione(parziale, v0)
        print (self.solBest)

    def ricorsione(self, parziale, nodo):
        archiVicini = list(self.grafo.edges(nodo, data=True))
        if len(archiVicini) == 0:
            if len(parziale) > len(self.solBest):
                self.solBest = list(parziale)


        for a in archiVicini:
            if len(parziale) < 2 or (len(parziale) >= 2 and a[2]['weight'] >= parziale[-1][2]['weight']):
                aInv = (a[1], a[0], a[2])
                print("ciao")
                if (a not in parziale) and (aInv not in parziale):
                    print("mela")
                    parziale.append(a)
                    self.ricorsione(parziale, a[1])
                    parziale.pop()