from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class TelaApp(GridLayout):
    pass

class Grid(App):
    def build(self):
        return TelaApp()

Grid().run()
