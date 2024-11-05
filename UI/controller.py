import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

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
            self._model.creaGrafo(colore)
            nNodes = self._model.getNumNodes()
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {nNodes}"))
            self._view.update_page()




    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
