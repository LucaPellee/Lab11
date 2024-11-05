from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def getYears(self):
        return DAO.getYear()

    def getColors(self):
        return DAO.getColors()

    def creaGrafo(self, color):
        self.grafo.clear()
        listaNodi = DAO.getProducts(color)
        self.grafo.add_nodes_from(listaNodi)

    def getNumNodes(self):
        return len(list(self.grafo.nodes()))
