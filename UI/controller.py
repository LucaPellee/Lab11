import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []
        self.prodotto = None

    def fillDD(self):
        anni = self._model.getYears()
        for a in anni:
            self._view._ddyear.options.append(ft.dropdown.Option(a))

        colori = self._model.getColors()
        for c in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(c))

        self._view.update_page()


    def handle_graph(self, e):
        anno = self._view._ddyear.value
        colore = self._view._ddcolor.value
        if anno is None or colore is None:
            self._view.create_alert("Inserire entrambi i valori")
            return
        else:
            self._model.creaGrafo(colore, anno)
            nNodes = self._model.getNumNodes()
            nEdges = self._model.getNumEdges()
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nNodes}"))
            self._view.txtOut.controls.append(ft.Text(f"Numero di archi: {nEdges}"))
            listaTopArchi = self._model.cercaArchi()
            listaNodiRip = self._model.cercaNodiRip(listaTopArchi)
            for a in listaTopArchi:
                self._view.txtOut.controls.append(ft.Text(f"Arco da {a[0]} a  {a[1]}, peso = {a[2]}"))
            self._view.txtOut.controls.append(ft.Text(f"I nodi ripetuti sono: {[str(p.Product_number) for p in listaNodiRip]}"))
            self.fillDDProduct()
            self._view.btn_search.disabled = False
            self._view.update_page()




    def fillDDProduct(self):
        colore = self._view._ddcolor.value
        listaProduct = self._model.getProducts(colore)
        for p in listaProduct:
            self._view._ddnode.options.append(ft.dropdown.Option(data = p, text = p.Product_number, on_click=self.readProd))
        self._view.update_page()

    def readProd(self, e):
        if e.control.data is None:
            self._view.create_alert("Inserire prodotto")
        else:
           self.prodotto = e.control.data

    def handle_search(self, e):
        self._model.getPercorso(self.prodotto)
        self._view.txtOut2.controls.append(ft.Text(f"Numero archi percorso più lungo: {len(self._model.solBest)}"))
        self._view.update_page()
