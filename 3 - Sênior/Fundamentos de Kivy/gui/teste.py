from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class Principal(BoxLayout):
    texto_principal = StringProperty('Eu sou uma label')
    tamanho_texto_principal = NumericProperty(20)
    def teste(self):
        self.texto_principal = 'Fui clicado'
        self.tamanho_texto_principal += 10
        if self.tamanho_texto_principal == 60:
            self.tamanho_texto_principal = 10

class Secundario(Widget):
    pass

class Teste(App):
    def build(self):
        return Principal()

Teste().run()
