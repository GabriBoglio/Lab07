import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    def popola_dropdowns(self):
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for b in self._model.get_biblioteche():
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(b.nome))

        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for g in self._model.get_generi():
            self._view.dd_genere.options.append(ft.dropdown.Option(g))

        self._view.update()

    def seleziona_biblioteca(self, e):
        val = e.control.value
        if val == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = val

    def seleziona_genere(self, e):
        val = e.control.value
        if val == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = val

    def mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        self._view.lst_libri.controls.clear()

        if not libri:
            self._view.show_alert("Nessun libro soddisfa i criteri di ricerca.")
        else:
            for libro in libri:
                self._view.lst_libri.controls.append(ft.Text(str(libro)))

        self._view.update()