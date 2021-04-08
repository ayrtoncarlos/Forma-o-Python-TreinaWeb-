from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class TelaApp(FloatLayout):
    pass

class Float(App):
    def build(self):
        return TelaApp()

Float().run()
