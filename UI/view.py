import flet as ft
from UI.alert import AlertManager
import flet as ft
from UI.alert import AlertManager


class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        self.alert = AlertManager(page)
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        self.dd_biblioteca = ft.Dropdown(
            label="Seleziona Biblioteca",
            on_select=self.controller.seleziona_biblioteca
        )

        self.dd_genere = ft.Dropdown(
            label="Seleziona Genere",
            on_select=self.controller.seleziona_genere
        )

        self.btn_mostra_libri = ft.ElevatedButton(
            text="Mostra Libri",
            on_click=self.controller.mostra_libri
        )

        self.lst_libri = ft.ListView(expand=1, spacing=10, padding=20)

        self.toggle_cambia_tema = ft.Switch(
            label="Tema scuro",
            value=True,
            on_change=self.cambia_tema
        )

        self.page.add(
            self.toggle_cambia_tema,
            self.txt_titolo,
            ft.Divider(),
            ft.Row(
                [self.dd_biblioteca, self.dd_genere],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            self.btn_mostra_libri,
            self.lst_libri
        )

        self.controller.popola_dropdowns()
        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()