from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('frontend.ky')


class ShowPokemon(Screen):
    def search(self):
        pass

class RootWidget(ScreenManager):
    pass

#buil class will return screenManager class
class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()