from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.lang import Builder
import requests

Builder.load_file('frontend.kv')

class ShowPokemon(Screen):
    pokemon_image_source = StringProperty('')

    def search(self, pokemon_name):
        pokemon_image_url = self.fetch_pokemon_data(pokemon_name)
        if pokemon_image_url:
            Clock.schedule_once(lambda dt: setattr(self, 'pokemon_image_source', pokemon_image_url), 0)
        else:
            print('Image not found for this Pokémon', {pokemon_name})


    def fetch_pokemon_data(self, pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            img_url = data['sprites']['other']['official-artwork']['front_default']
            return img_url


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
