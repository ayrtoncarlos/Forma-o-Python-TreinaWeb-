from kivy.app import App
from kivy.uix.stacklayout import StackLayout


class TelaApp(StackLayout):
    pass

class Stack(App):
    def build(self):
        return TelaApp()

Stack().run()
