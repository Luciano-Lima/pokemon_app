from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.lang import Builder
import requests

Builder.load_file('frontend.kv')

class ShowPokemon(Screen):
    pokemon_image_source = StringProperty('')
    pokemon_description =  StringProperty('')

    def search(self, pokemon_name):
        pokemon_image_url = self.fetch_pokemon_image(pokemon_name)
        if pokemon_image_url:
            self.pokemon_image_source = pokemon_image_url
            self.fetch_pokemon_description(pokemon_name)
        else:
            self.pokemon_description = f'No data found for {pokemon_name}'

    def fetch_pokemon_image(self, pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            img_url = data['sprites']['other']['official-artwork']['front_default']
            return img_url
        return None


    def fetch_pokemon_description(self, pokemon_name):
        description_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}/"
        description_response = requests.get(description_url)
        if description_response.status_code == 200:
            description_data = description_response.json()
            description = description_data['flavor_text_entries'][0]['flavor_text']
            self.pokemon_description = description
        else:
            self.pokemon_description = f"Description not available for {pokemon_name}."


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
