from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class ShowPokemon(Screen):
    def search(self):
        pass

class RootWidgets(ScreenManager):
    pass

#buil class will return screenManager class
class MainApp(App):

    def build(self):
        return RootWidgets()

MainApp().run()